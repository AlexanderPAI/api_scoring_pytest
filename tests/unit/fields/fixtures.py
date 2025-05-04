import datetime

import pytest

from src.api import (
    ArgumentsField,
    BirthDayField,
    CharField,
    ClientIDsField,
    DateField,
    EmailField,
    Field,
    GenderField,
    PhoneField,
)

fields_positive_fixtures = [
    pytest.param(
        Field,
        {"required": True, "nullable": True},
        "test_value",
        id='Field: required=True, nullable=True, value="test_value"',
    ),
    pytest.param(
        Field,
        {"required": False, "nullable": True},
        "test_value",
        id='Field: required=False, nullable=True, value="test_value"',
    ),
    pytest.param(
        Field,
        {"required": True, "nullable": False},
        "test_value",
        id='Field: required=True, nullable=False, value="test_value"',
    ),
    pytest.param(
        Field,
        {"required": False, "nullable": False},
        "test_value",
        id='Field: required=False, nullable=False, value="test_value"',
    ),
    pytest.param(
        CharField,
        {"required": True, "nullable": False},
        "char_test_value",
        id="CharField: value is str",
    ),
    pytest.param(
        ArgumentsField,
        {"required": True, "nullable": False},
        {"key1": "value1", "key2": "value2"},
        id="ArgumentsField: value is dict",
    ),
    pytest.param(
        EmailField,
        {"required": True, "nullable": False},
        "test@test.com",
        id="EmailField: value is test@test.com",
    ),
    pytest.param(
        PhoneField,
        {"required": True, "nullable": False},
        "79998887766",
        id='PhoneField: value is "79998887766"',
    ),
    pytest.param(
        PhoneField,
        {"required": True, "nullable": False},
        79998887766,
        id="PhoneField: value is 79998887766 (int)",
    ),
    pytest.param(
        DateField,
        {"required": True, "nullable": False},
        "20.01.2025",
        id="DateField: value is 20.01.2025",
    ),
    pytest.param(
        BirthDayField,
        {"required": True, "nullable": False},
        (datetime.datetime.now() - datetime.timedelta(days=365 * 69)).strftime(
            "%d.%m.%Y"
        ),
        id="BirthDayField: value is {}".format(
            (datetime.datetime.now() - datetime.timedelta(days=365 * 70)).strftime(
                "%d.%m.%Y"
            )
        ),
    ),
    pytest.param(
        GenderField,
        {"required": True, "nullable": False},
        0,
        id="GenderField: value is 0",
    ),
    pytest.param(
        GenderField,
        {"required": True, "nullable": False},
        0,
        id="GenderField: value is 1",
    ),
    pytest.param(
        GenderField,
        {"required": True, "nullable": False},
        0,
        id="GenderField: value is 2",
    ),
    pytest.param(
        ClientIDsField,
        {"required": True, "nullable": False},
        [1, 2, 3, 4],
        id="ClientIDsField: value is [1, 2, 3, 4]",
    ),
]


fields_negative_fixtures = [
    pytest.param(
        Field,
        {"required": True, "nullable": False},
        None,
        "{field_name} is required",
        id="Field: required=True, nullable=False, value=None",
    ),
    pytest.param(
        Field,
        {"required": True, "nullable": False},
        "",
        "{field_name} isn't nullable",
        id='Field: required=True, nullable=False, value=""',
    ),
    pytest.param(
        Field,
        {"required": True, "nullable": False},
        (),
        "{field_name} isn't nullable",
        id="Field: required=True, nullable=False, value=()",
    ),
    pytest.param(
        Field,
        {"required": True, "nullable": False},
        {},
        "{field_name} isn't nullable",
        id="Field: required=True, nullable=False, value={}",
    ),
    pytest.param(
        Field,
        {"required": True, "nullable": False},
        [],
        "{field_name} isn't nullable",
        id="Field: required=True, nullable=False, value=[]",
    ),
    pytest.param(
        CharField,
        {"required": True, "nullable": False},
        1,
        "{field_name} must be a string",
        id="CharField: value is int",
    ),
    pytest.param(
        CharField,
        {"required": True, "nullable": False},
        1.0,
        "{field_name} must be a string",
        id="CharField: value is float",
    ),
    pytest.param(
        CharField,
        {"required": True, "nullable": False},
        True,
        "{field_name} must be a string",
        id="CharField: value is bool",
    ),
    pytest.param(
        CharField,
        {"required": True, "nullable": False},
        ["one", "two"],
        "{field_name} must be a string",
        id="CharField: value is list",
    ),
    pytest.param(
        CharField,
        {"required": True, "nullable": False},
        {"key1": "value1", "key2": "value2"},
        "{field_name} must be a string",
        id="CharField: value is dict",
    ),
    pytest.param(
        ArgumentsField,
        {"required": True, "nullable": False},
        "test_value",
        "{field_name} must be a dictionary",
        id="ArgumentsField: value is str",
    ),
    pytest.param(
        ArgumentsField,
        {"required": True, "nullable": False},
        1,
        "{field_name} must be a dictionary",
        id="ArgumentsField: value is int",
    ),
    pytest.param(
        ArgumentsField,
        {"required": True, "nullable": False},
        1.0,
        "{field_name} must be a dictionary",
        id="ArgumentsField: value is float",
    ),
    pytest.param(
        ArgumentsField,
        {"required": True, "nullable": False},
        True,
        "{field_name} must be a dictionary",
        id="ArgumentsField: value is bool",
    ),
    pytest.param(
        ArgumentsField,
        {"required": True, "nullable": False},
        ["one", "two"],
        "{field_name} must be a dictionary",
        id="ArgumentsField: value is list",
    ),
    pytest.param(
        EmailField,
        {"required": True, "nullable": False},
        "test@test",
        "{field_name} must be email",
        id="EmailField: value is test@test",
    ),
    pytest.param(
        EmailField,
        {"required": True, "nullable": False},
        "test.com",
        "{field_name} must be email",
        id="EmailField: value is test.com",
    ),
    pytest.param(
        EmailField,
        {"required": True, "nullable": False},
        "test",
        "{field_name} must be email",
        id="EmailField: value is test",
    ),
    pytest.param(
        PhoneField,
        {"required": True, "nullable": False},
        "89998887766",
        '{field_name} must starts with "7" and be no longer than 11 characters',
        id='PhoneField: value is "89998887766"',
    ),
    pytest.param(
        PhoneField,
        {"required": True, "nullable": False},
        "+7-999-888-77-66",
        '{field_name} must starts with "7" and be no longer than 11 characters',
        id='PhoneField: value is "+7-999-888-77-66"',
    ),
    pytest.param(
        PhoneField,
        {"required": True, "nullable": False},
        "8999888",
        '{field_name} must starts with "7" and be no longer than 11 characters',
        id='PhoneField: value is "8999888"',
    ),
    pytest.param(
        PhoneField,
        {"required": True, "nullable": False},
        89998887766,
        '{field_name} must starts with "7" and be no longer than 11 characters',
        id="PhoneField: value is 89998887766 (int)",
    ),
    pytest.param(
        PhoneField,
        {"required": True, "nullable": False},
        8999888.0000,
        "{field_name} must be number or string",
        id="PhoneField: value is 8999888.0000 (float)",
    ),
    pytest.param(
        DateField,
        {"required": True, "nullable": False},
        "2025.01.20",
        "{field_name} must be in the DD.MM.YYYY format",
        id="DateField: value is 2025.01.20",
    ),
    pytest.param(
        DateField,
        {"required": True, "nullable": False},
        "20-01-2025",
        "{field_name} must be in the DD.MM.YYYY format",
        id="DateField: value is 20-01-2025",
    ),
    pytest.param(
        DateField,
        {"required": True, "nullable": False},
        "20012025",
        "{field_name} must be in the DD.MM.YYYY format",
        id="DateField: value is 20012025",
    ),
    pytest.param(
        DateField,
        {"required": True, "nullable": False},
        "20/01/2025",
        "{field_name} must be in the DD.MM.YYYY format",
        id="DateField: value is 20/01/2025",
    ),
    pytest.param(
        BirthDayField,
        {"required": True, "nullable": False},
        (datetime.datetime.now() + datetime.timedelta(days=365)).strftime("%d.%m.%Y"),
        "{field_name} must be positive amount years",
        id="BirthDayField: value is {}".format(
            (datetime.datetime.now() + datetime.timedelta(days=365)).strftime(
                "%d.%m.%Y"
            )
        ),
    ),
    pytest.param(
        BirthDayField,
        {"required": True, "nullable": False},
        (datetime.datetime.now() - datetime.timedelta(days=365 * 71)).strftime(
            "%d.%m.%Y"
        ),
        "{field_name} too many years old, must be <= 70",
        id="BirthDayField: value is {}".format(
            (datetime.datetime.now() - datetime.timedelta(days=365 * 70)).strftime(
                "%d.%m.%Y"
            )
        ),
    ),
    pytest.param(
        GenderField,
        {"required": True, "nullable": False},
        -1,
        "{field_name} must be 0 - UNKNOWN, 1 - MALE, 2 - FEMALE",
        id="GenderField: value is -1",
    ),
    pytest.param(
        GenderField,
        {"required": True, "nullable": False},
        3,
        "{field_name} must be 0 - UNKNOWN, 1 - MALE, 2 - FEMALE",
        id="GenderField: value is 3",
    ),
    pytest.param(
        GenderField,
        {"required": True, "nullable": False},
        "Three",
        "{field_name} must be 0 - UNKNOWN, 1 - MALE, 2 - FEMALE",
        id="GenderField: value is Three",
    ),
    pytest.param(
        ClientIDsField,
        {"required": True, "nullable": False},
        "1, 2, 3, 4",
        "{field_name} must be list of integers",
        id='ClientIDsField: value is "1, 2, 3, 4"',
    ),
    pytest.param(
        ClientIDsField,
        {"required": True, "nullable": False},
        {"clients_ids": [1, 2, 3, 4]},
        "{field_name} must be list of integers",
        id='ClientIDsField: value is {"clients_ids": [1, 2, 3, 4]}',
    ),
    pytest.param(
        ClientIDsField,
        {"required": True, "nullable": False},
        ["1", "2", "3", "4"],
        "{field_name} must be list of integers",
        id='ClientIDsField: value is ["1", "2", "3", "4"]',
    ),
]
