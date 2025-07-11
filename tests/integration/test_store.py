import hashlib
import json

import pytest

from src.scoring import get_interests, get_score
from src.store import Store


@pytest.mark.parametrize(
    "key_parts, score, expected",
    [
        pytest.param(
            [
                "79998887733",
                "stupnikov@otus.ru",
                "01.01.2000",
                str(2),
                "Станислав",
                "Ступников",
            ],
            5.0,
            "5.0",
            id="POSITIVE Store: cache_get and cache_set",
        )
    ],
)
def test_store_cache_set_and_get(key_parts, score, expected):
    store = Store()
    key = "uid:" + hashlib.md5("".join(key_parts).encode("utf-8")).hexdigest()
    store.cache_set(key, score, 60 * 60)
    assert store.cache_get(key) == expected


@pytest.mark.parametrize(
    "cid, interests, expected",
    [
        pytest.param(
            1,
            json.dumps(["travel", "music"]),
            '["travel", "music"]',
            id="POSITIVE Store: get and set",
        )
    ],
)
def test_store_set_and_get(cid, interests, expected):
    store = Store()
    store.set(f"i:{cid}", "interests", str(interests))
    assert store.get("i:1") == expected


@pytest.mark.parametrize(
    "attrs, expected",
    [
        pytest.param(
            {
                "phone": "79998887733",
                "email": "stupnikov@otus.ru",
                "birthday": "01.01.2000",
                "gender": 1,
                "first_name": "Станислав",
                "last_name": "Ступников",
            },
            5.0,
            id="POSITIVE Store: get_score with store",
        )
    ],
)
def test_get_score_with_store(attrs, expected):
    store = Store()
    assert get_score(store, **attrs) == expected


def test_get_interests_with_store():
    store = Store()
    store.set("i:5", "interests", json.dumps(["travel", "geek"]))
    assert get_interests(store, 5) == ["travel", "geek"]
