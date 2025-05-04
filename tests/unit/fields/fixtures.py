import pytest

from src.api import ArgumentsField, CharField, Field

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
]
