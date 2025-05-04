#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import hashlib
import json
import logging
import re
import uuid
from argparse import ArgumentParser
from http.server import BaseHTTPRequestHandler, HTTPServer
from types import FunctionType
from typing import Any

from src.scoring import get_interests, get_score
from src.store import Store

SALT = "Otus"
ADMIN_LOGIN = "admin"
ADMIN_SALT = "42"
OK = 200
BAD_REQUEST = 400
FORBIDDEN = 403
NOT_FOUND = 404
INVALID_REQUEST = 422
INTERNAL_ERROR = 500
ERRORS = {
    BAD_REQUEST: "Bad Request",
    FORBIDDEN: "Forbidden",
    NOT_FOUND: "Not Found",
    INVALID_REQUEST: "Invalid Request",
    INTERNAL_ERROR: "Internal Server Error",
}
UNKNOWN = 0
MALE = 1
FEMALE = 2
GENDERS = {
    UNKNOWN: "unknown",
    MALE: "male",
    FEMALE: "female",
}


class Field:

    def __init__(
        self,
        required: bool = False,
        nullable: bool = False,
    ) -> None:
        self.required = required
        self.nullable = nullable
        self.name = "Field"

    def __set_name__(self, owner, name) -> None:
        self.name = name

    def __set__(self, instance, value) -> None:
        self.validate(value)
        instance.__dict__[self.name] = value

    def validate(self, value) -> None:
        # match-case галлюцинирует
        if value is None:
            if self.required:
                raise ValueError(f"{self.name} is required")
            if not self.nullable:
                raise ValueError(f"{self.name} isn't nullable")
        elif value in ("", (), {}, []) and not self.nullable:
            raise ValueError(f"{self.name} isn't nullable")
        else:
            self.sub_field_validate(value)

    def sub_field_validate(self, value) -> None:
        pass


class CharField(Field):
    def sub_field_validate(self, value) -> None:
        if not isinstance(value, str):
            raise ValueError(f"{self.name} must be a string")


class ArgumentsField(Field):
    def sub_field_validate(self, value) -> None:
        if not isinstance(value, dict):
            raise ValueError(f"{self.name} must be a dictionary")


class EmailField(CharField):
    REGEX_EMAIL = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    def sub_field_validate(self, value) -> None:
        super().sub_field_validate(value)
        if not re.match(self.REGEX_EMAIL, value):
            raise ValueError(f"{self.name} must be email")


class PhoneField(Field):
    REGEX_PHONE_NUMBER = r"^7\d{10}$"

    def sub_field_validate(self, value) -> str:

        if not isinstance(value, str | int):
            raise ValueError(f"{self.name} must be number or string")

        if isinstance(value, int):
            value = str(value)

        if not re.match(self.REGEX_PHONE_NUMBER, value):
            raise ValueError(
                f'{self.name} must starts with "7" and be no longer than 11 characters'
            )
        return value


class DateField(Field):
    REGEX_DATE = r"^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.\d{4}$"

    def sub_field_validate(self, value) -> None:
        if not re.match(self.REGEX_DATE, value):
            raise ValueError(f"{self.name} must be in the DD.MM.YYYY format")


class BirthDayField(DateField):
    MAX_AGE = 70

    def sub_field_validate(self, value) -> None:
        super().sub_field_validate(value)
        birth_date = datetime.datetime.strptime(value, "%d.%m.%Y").year
        date_now = datetime.datetime.now().year
        if date_now - birth_date > 70:
            raise ValueError(f"{self.name} too many years old, must be <= 70")
        if date_now - birth_date < 0:
            raise ValueError(f"{self.name} must be positive amount years")


class GenderField(Field):
    VALUES = [UNKNOWN, MALE, FEMALE]

    def sub_field_validate(self, value) -> None:
        if value not in self.VALUES:
            raise ValueError(f"{self.name} must be 0 - UNKNOWN, 1 - MALE, 2 - FEMALE")


class ClientIDsField(Field):
    def sub_field_validate(self, value) -> None:
        if not isinstance(value, list) or not all(
            isinstance(client_id, int) for client_id in value
        ):
            raise ValueError(f'Field "{self.name}" must be list of integers')


class BaseRequest:
    def __init__(self, data: dict):
        for field_name, field in self.__class__.__dict__.items():
            if not isinstance(field, property | FunctionType):
                value = data.get(field_name)
                setattr(self, field_name, value)

        if hasattr(self, "validate"):
            self.validate()

    def to_dict(self) -> dict[str, Any]:
        return {
            attr: value
            for attr, value in self.__dict__.items()
            if not attr.startswith("__") and not attr.startswith("_")
        }


class MethodRequest(BaseRequest):
    account: str = CharField(required=False, nullable=True)
    login: str = CharField(required=True, nullable=True)
    token: str = CharField(required=True, nullable=True)
    arguments: dict[str, Any] = ArgumentsField(required=True, nullable=True)
    method: str = CharField(required=True, nullable=False)

    @property
    def is_admin(self):
        return self.login == ADMIN_LOGIN


class ClientsInterestsRequest(BaseRequest):
    client_ids: list[int] = ClientIDsField(required=True)
    date: str = DateField(required=False, nullable=True)


class OnlineScoreRequest(BaseRequest):
    first_name: str = CharField(required=False, nullable=True)
    last_name: str = CharField(required=False, nullable=True)
    email: str = EmailField(required=False, nullable=True)
    phone: str | int = PhoneField(required=False, nullable=True)
    birthday: str = BirthDayField(required=False, nullable=True)
    gender: int = GenderField(required=False, nullable=True)

    def validate(self):
        if not (
            (self.first_name is not None and self.last_name is not None)
            or (self.email is not None and self.phone is not None)
            or (self.birthday is not None and self.gender is not None)
        ):
            raise ValueError(
                '"online_score" request must have at least one pair with non-empty values: '
                "phone - email, first_name - last_name, birthday - gender."
            )


def check_auth(request):
    if request.is_admin:
        digest = hashlib.sha512(
            (datetime.datetime.now().strftime("%Y%m%d%H") + ADMIN_SALT).encode("utf-8")
        ).hexdigest()
    else:
        digest = hashlib.sha512(
            (request.account + request.login + SALT).encode("utf-8")
        ).hexdigest()
    return digest == request.token


def online_score_method(request_obj, ctx, store):
    online_score_request_obj = OnlineScoreRequest(request_obj.arguments)

    if not request_obj.is_admin:
        response = {"score": get_score(store, **online_score_request_obj.to_dict())}
    else:
        response = {"score": 42}

    ctx["has"] = []
    for field, value in online_score_request_obj.__dict__.items():
        if value is not None:
            ctx["has"].append(field)

    return response, OK


def clients_interests_method(request_obj, ctx, store):
    clients_interests_request_obj = ClientsInterestsRequest(request_obj.arguments)
    response = {
        client_id: get_interests(store, client_id)
        for client_id in clients_interests_request_obj.client_ids
    }

    ctx["nclients"] = len(clients_interests_request_obj.client_ids)

    return response, OK


def method_handler(request, ctx, store):
    try:
        methods = {
            "clients_interests": clients_interests_method,
            "online_score": online_score_method,
        }

        request_body = request.get("body")
        request_obj = MethodRequest(request_body)

        if not check_auth(request_obj):
            response, code = "Forbidden", FORBIDDEN
            return response, code

        method = request_body.get("method")
        if method and method in methods.keys():
            response, code = methods.get(request_body.get("method"))(
                request_obj, ctx, store
            )
            return response, code
        else:
            response, code = "The method was not found", INVALID_REQUEST
            return response, code

    except ValueError as e:
        return str(e), INVALID_REQUEST


class MainHTTPHandler(BaseHTTPRequestHandler):
    router = {"method": method_handler}
    store = Store()

    def get_request_id(self, headers):
        return headers.get("HTTP_X_REQUEST_ID", uuid.uuid4().hex)

    def do_POST(self):
        response, code = {}, OK
        context = {"request_id": self.get_request_id(self.headers)}
        request = None
        try:
            data_string = self.rfile.read(int(self.headers["Content-Length"]))
            request = json.loads(data_string)
        except Exception:
            code = BAD_REQUEST
        if request:
            path = self.path.strip("/")
            logging.info("%s: %s %s" % (self.path, data_string, context["request_id"]))
            if path in self.router:
                try:
                    response, code = self.router[path](
                        {"body": request, "headers": self.headers}, context, self.store
                    )
                except Exception as e:
                    logging.exception("Unexpected error: %s" % e)
                    code = INTERNAL_ERROR
            else:
                code = NOT_FOUND

        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        if code not in ERRORS:
            r = {"response": response, "code": code}
        else:
            r = {"error": response or ERRORS.get(code, "Unknown Error"), "code": code}
        context.update(r)
        self.wfile.write(json.dumps(r).encode("utf-8"))
        return


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-p", "--port", action="store", type=int, default=8080)
    parser.add_argument("-l", "--log", action="store", default=None)
    args = parser.parse_args()
    logging.basicConfig(
        filename=args.log,
        level=logging.INFO,
        format="[%(asctime)s] %(levelname).1s %(message)s",
        datefmt="%Y.%m.%d %H:%M:%S",
    )
    server = HTTPServer(("0.0.0.0", args.port), MainHTTPHandler)
    logging.info("Starting server at %s" % args.port)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()
