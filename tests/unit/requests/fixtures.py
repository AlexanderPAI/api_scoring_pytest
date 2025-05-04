import pytest

method_request_positive_fixtures = [
    pytest.param(
        {
            "account": "test_account",
            "login": "test_login",
            "method": "clients_interests",
            "token": "xxx",
            "arguments": {},
        },
        id="POSITIVE MethodRequest: Valid Data Success",
    ),
]


method_request_negative_fixtures = [
    pytest.param(
        {
            "login": "test_login",
            "method": "clients_interests",
            "token": "xxx",
            "arguments": {},
        },
        "account is required",
        id="NEGATIVE MethodRequest: No Account Error",
    ),
    pytest.param(
        {
            "account": "test_account",
            "method": "clients_interests",
            "token": "xxx",
            "arguments": {},
        },
        "login is required",
        id="NEGATIVE MethodRequest: No Login Error",
    ),
    pytest.param(
        {
            "account": "test_account",
            "login": "test_login",
            "token": "xxx",
            "arguments": {},
        },
        "method is required",
        id="NEGATIVE MethodRequest: No Method Error",
    ),
    pytest.param(
        {
            "account": "test_account",
            "login": "test_login",
            "method": "clients_interests",
            "arguments": {},
        },
        "token is required",
        id="NEGATIVE MethodRequest: No Token Error",
    ),
]


clients_interests_request_positive_fixtures = [
    pytest.param(
        {"client_ids": [1, 2, 3, 4], "date": "20.07.2017"},
        id="POSITIVE ClientsInterestsRequest: Valid Data Success",
    ),
]

clients_interests_request_negative_fixtures = [
    pytest.param(
        {"date": "20.07.2017"},
        "client_ids is required",
        id="NEGATIVE MethodRequest: No ClientIDs Error",
    ),
]
