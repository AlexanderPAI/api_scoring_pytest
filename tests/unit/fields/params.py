import pytest

# fields

# params for test positive validate
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

# params for test negative validate
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
