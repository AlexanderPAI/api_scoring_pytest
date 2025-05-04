import pytest

from tests.unit.fields.fixtures import (
    fields_negative_fixtures,
    fields_positive_fixtures,
)


@pytest.mark.parametrize(
    "field_type, attrs, field_value",
    fields_positive_fixtures,
)
def test_field_validate_positive(field_type, attrs, field_value):
    field = field_type(**attrs)
    field.validate(field_value)


@pytest.mark.parametrize(
    "field_type, attrs, field_value, expected",
    fields_negative_fixtures,
)
def test_fields_validate_negative(field_type, attrs, field_value, expected):
    field = field_type(**attrs)
    with pytest.raises(ValueError) as e:
        field.validate(field_value)
    assert str(e.value) == expected.format(field_name=field.name)
