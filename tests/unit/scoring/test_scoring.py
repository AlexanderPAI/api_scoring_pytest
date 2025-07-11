from unittest.mock import MagicMock

import pytest

import src.api as api
from src.store import Store
from tests.unit.scoring.fake_storage import fake_storage
from tests.unit.scoring.fixtures import params_get_interests, params_get_score

store = MagicMock(spec=Store)
store.cache_get.return_value = None
store.get = lambda cid: fake_storage.get(cid)


@pytest.mark.parametrize(
    "data, expected",
    params_get_score,
)
def test_get_score_result(data, expected):
    """Test get_score"""
    assert api.get_score(store, **data) == expected, f"Params {data} - wrong score"


@pytest.mark.parametrize("data, expected", params_get_interests)
def test_get_interests(data, expected):
    assert (
        api.get_interests(store, data) == expected
    ), f"Params client_id={data} - wrong interests"
