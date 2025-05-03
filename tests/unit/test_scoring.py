from unittest.mock import MagicMock

import pytest

import src.api as api
from src.store import Store
from tests.unit.params import params_get_score

store = MagicMock(spec=Store)
store.cache_get.return_value = None


@pytest.mark.parametrize(
    "data, expected",
    params_get_score,
)
def test_get_score(data, expected):
    """Test get_score"""
    assert api.get_score(store, **data) == expected, f"Params {data} - wrong score"
