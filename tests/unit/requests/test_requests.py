import pytest

from src.api import MethodRequest
from tests.unit.requests.fixtures import (
    method_request_negative_fixtures,
    method_request_positive_fixtures,
)


@pytest.mark.parametrize("request_body", method_request_positive_fixtures)
def test_method_request_positive(request_body):
    MethodRequest(request_body)


@pytest.mark.parametrize("request_body, expected", method_request_negative_fixtures)
def test_method_request_negative(request_body, expected):
    with pytest.raises(ValueError) as e:
        MethodRequest(request_body)
    assert str(e.value) == expected
