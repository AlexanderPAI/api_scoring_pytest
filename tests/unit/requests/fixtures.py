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


online_score_request_positive_fixtures = [
    pytest.param(
        {"phone": "79175002040", "email": "stupnikov@otus.ru"},
        id="POSITIVE OnlineScoreRequest: Success - Phone + Email",
    ),
    pytest.param(
        {"first_name": "Станислав", "last_name": "Ступников"},
        id="POSITIVE OnlineScoreRequest: Success - First_name + Last_name",
    ),
    pytest.param(
        {"birthday": "01.01.2000", "gender": 1},
        id="POSITIVE OnlineScoreRequest: Success - BirthDay + Gender",
    ),
]


online_score_request_negative_fixtures = [
    pytest.param(
        {"phone": "79175002040", "first_name": "Станислав", "birthday": "01.01.2000"},
        '"online_score" request must have at least one pair with non-empty values: phone - email, '
        "first_name - last_name, birthday - gender.",
        id="NEGATIVE OnlineScoreRequest: No Email, No Last_name, No Gender Error",
    ),
    pytest.param(
        {"email": "stupnikov@otus.ru", "last_name": "Ступников", "gender": 1},
        '"online_score" request must have at least one pair with non-empty values: phone - email, '
        "first_name - last_name, birthday - gender.",
        id="NEGATIVE OnlineScoreRequest: No Phone, No First_name, No BirthDay Error",
    ),
]
