import pytest

params_get_score = [
    pytest.param(
        {"phone": "79175002040", "email": "stupnikov@otus.ru"}, 3.0, id="Phone + Email"
    ),
    pytest.param(
        {
            "phone": "79175002040",
            "email": "stupnikov@otus.ru",
            "first_name": "Станислав",
        },
        3.0,
        id="Phone + Email + FirstName",
    ),
    pytest.param(
        {
            "phone": "79175002040",
            "email": "stupnikov@otus.ru",
            "last_name": "Ступников",
        },
        3.0,
        id="Phone + Email + LastName",
    ),
    pytest.param(
        {
            "phone": "79175002040",
            "email": "stupnikov@otus.ru",
            "first_name": "Станислав",
            "last_name": "Ступников",
        },
        3.5,
        id="Phone + Email + FirstName + LastName",
    ),
    pytest.param(
        {
            "phone": "79175002040",
            "email": "stupnikov@otus.ru",
            "birthday": "01.01.2000",
        },
        3.0,
        id="Phone + Email + Birthday",
    ),
    pytest.param(
        {"phone": "79175002040", "email": "stupnikov@otus.ru", "gender": 1},
        3.0,
        id="Phone + Email + Gender",
    ),
    pytest.param(
        {
            "phone": "79175002040",
            "email": "stupnikov@otus.ru",
            "birthday": "01.01.2000",
            "gender": 1,
        },
        4.5,
        id="Phone + Email + Birthday + Gender",
    ),
    pytest.param(
        {
            "phone": "79175002040",
            "email": "stupnikov@otus.ru",
            "first_name": "Станислав",
            "birthday": "01.01.2000",
            "gender": 1,
        },
        4.5,
        id="Phone + Email + Birthday + Gender + FirstName",
    ),
    pytest.param(
        {
            "phone": "79175002040",
            "email": "stupnikov@otus.ru",
            "last_name": "Ступников",
            "birthday": "01.01.2000",
            "gender": 1,
        },
        4.5,
        id="Phone + Email + Birthday + Gender + LastName",
    ),
    pytest.param(
        {
            "phone": "79175002040",
            "email": "stupnikov@otus.ru",
            "first_name": "Станислав",
            "last_name": "Ступников",
            "birthday": "01.01.2000",
            "gender": 1,
        },
        5.0,
        id="Phone + Email + Birthday + Gender + FirstName + LastName",
    ),
]
