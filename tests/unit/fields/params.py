import pytest

# fields

# params for field positive validate
field_positive_validate = [
    pytest.param(
        {"required": True, "nullable": True},
        "test_value",
        id='Field: required=True, nullable=True, value="test_value"',
    ),
    pytest.param(
        {"required": False, "nullable": True},
        "test_value",
        id='Field: required=False, nullable=True, value="test_value"',
    ),
    pytest.param(
        {"required": True, "nullable": False},
        "test_value",
        id='Field: required=True, nullable=False, value="test_value"',
    ),
    pytest.param(
        {"required": False, "nullable": False},
        "test_value",
        id='Field: required=False, nullable=False, value="test_value"',
    ),
]

# params for field negative validate
field_negative_validate = [
    pytest.param(
        {"required": True, "nullable": False},
        None,
        "{field_name} is required",
        id="Field: required=True, nullable=False, value=None",
    ),
    pytest.param(
        {"required": True, "nullable": False},
        "",
        "{field_name} isn't nullable",
        id='Field: required=True, nullable=False, value=""',
    ),
    pytest.param(
        {"required": True, "nullable": False},
        (),
        "{field_name} isn't nullable",
        id="Field: required=True, nullable=False, value=()",
    ),
    pytest.param(
        {"required": True, "nullable": False},
        {},
        "{field_name} isn't nullable",
        id="Field: required=True, nullable=False, value={}",
    ),
    pytest.param(
        {"required": True, "nullable": False},
        [],
        "{field_name} isn't nullable",
        id="Field: required=True, nullable=False, value=[]",
    ),
]


# params for char_field positive validate
char_field_positive_validate = [
    pytest.param(
        {"required": True, "nullable": False},
        "char_test_value",
        id="CharField: value is str",
    ),
]


# params for char_field negative validate
char_field_negative_validate = [
    pytest.param(
        {"required": True, "nullable": False},
        1,
        "{field_name} must be a string",
        id="CharField: value is int",
    ),
    pytest.param(
        {"required": True, "nullable": False},
        1.0,
        "{field_name} must be a string",
        id="CharField: value is float",
    ),
    pytest.param(
        {"required": True, "nullable": False},
        True,
        "{field_name} must be a string",
        id="CharField: value is bool",
    ),
    pytest.param(
        {"required": True, "nullable": False},
        ["one", "two"],
        "{field_name} must be a string",
        id="CharField: value is list",
    ),
]
