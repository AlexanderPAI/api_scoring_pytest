import json
import random
from typing import List

from src.store import Store

store = Store()

CLIENTS_IDS = [0, 1, 2, 3, 4]
INTERESTS = [
    "cars",
    "pets",
    "travel",
    "hi-tech",
    "sport",
    "music",
    "books",
    "tv",
    "cinema",
    "geek",
    "otus",
]


def fill_redis_for_test(clients_ids: List[int], interests: List[str]) -> None:
    for client_id in clients_ids:
        selected_interests = random.sample(interests, 2)
        store.set(f"i:{client_id}", "interests", json.dumps(selected_interests))


fill_redis_for_test(CLIENTS_IDS, INTERESTS)
