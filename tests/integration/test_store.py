import hashlib

import pytest

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
            ["travel", "music"],
            "['travel', 'music']",
            id="POSITIVE Store: get and set",
        )
    ],
)
def test_store_set_and_get(cid, interests, expected):
    store = Store()
    store.set(f"i:{cid}", "interests", str(interests))
    assert store.get("i:1") == expected
