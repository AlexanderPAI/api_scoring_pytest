import pytest

from src.api import Field
from tests.unit.fields.params import field_negative_validate, field_positive_validate


@pytest.mark.parametrize(
    "attrs, field_value",
    field_positive_validate,
)
def test_field_validate_positive(attrs, field_value):
    field = Field(**attrs)
    field.validate(field_value)


@pytest.mark.parametrize("attrs, field_value, expected", field_negative_validate)
def test_field_validate_negative(attrs, field_value, expected):
    field = Field(**attrs)
    with pytest.raises(ValueError) as e:
        field.validate(field_value)
    assert str(e.value) == expected.format(field_name=field.name)
