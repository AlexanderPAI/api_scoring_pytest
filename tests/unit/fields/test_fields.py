import pytest

from src.api import ArgumentsField, CharField, Field
from tests.unit.fields.params import (
    arguments_field_negative_validate,
    arguments_field_positive_validate,
    char_field_negative_validate,
    char_field_positive_validate,
    field_negative_validate,
    field_positive_validate,
)


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


@pytest.mark.parametrize(
    "attrs, field_value",
    char_field_positive_validate,
)
def test_char_field_validate_positive(attrs, field_value):
    field = CharField(**attrs)
    field.validate(field_value)


@pytest.mark.parametrize("attrs, field_value, expected", char_field_negative_validate)
def test_char_field_validate_negative(attrs, field_value, expected):
    field = CharField(**attrs)
    with pytest.raises(ValueError) as e:
        field.validate(field_value)
    assert str(e.value) == expected.format(field_name=field.name)


@pytest.mark.parametrize(
    "attrs, field_value",
    arguments_field_positive_validate,
)
def test_arguments_field_validate_positive(attrs, field_value):
    field = ArgumentsField(**attrs)
    field.validate(field_value)


@pytest.mark.parametrize(
    "attrs, field_value, expected", arguments_field_negative_validate
)
def test_arguments_field_negative_validate(attrs, field_value, expected):
    field = ArgumentsField(**attrs)
    with pytest.raises(ValueError) as e:
        field.validate(field_value)
    assert str(e.value) == expected.format(field_name=field.name)
