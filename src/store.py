import logging
from contextlib import contextmanager
from typing import Generator

import redis


class Store:
    """Redis storage"""

    def __init__(
        self,
        redis_host: str = "host.docker.internal",
        redis_port: int = 6379,
        socket_connect_timeout: float = 10.0,
        socket_timeout: float = 10.0,
        max_retries: int = 5,
    ) -> None:
        self.redis_host = redis_host
        self.redis_port = redis_port
        self.socket_connect_timeout = socket_connect_timeout
        self.socket_timeout = socket_timeout
        self.max_retries = max_retries

    @contextmanager
    def redis_connection(self) -> Generator[redis.Redis, None, None]:
        """Context manager for 'with'"""
        conn = None
        error = None
        for retire in range(self.max_retries):
            logging.info(f"Conn Attempt {retire + 1}/{self.max_retries}")
            try:
                conn = redis.Redis(
                    host=self.redis_host,
                    port=self.redis_port,
                    decode_responses=True,
                    socket_connect_timeout=self.socket_connect_timeout,
                    socket_timeout=self.socket_timeout,
                )
                conn.ping()
                break
            except redis.RedisError as e:
                logging.error(str(e))
                error = e
                continue

        if error is not None:
            raise redis.RedisError("Connection to storage failed")

        try:
            yield conn
        finally:
            conn.close()

    def healthcheck(self):
        """Service func for healthcheck redis storage"""
        with self.redis_connection() as r:
            result = r.ping()
            logging.info(f"Redis is alive: {result}")
            return result

    def set(self, i_cid: str, field: str, value: str) -> None:
        """Set to persistent redis storage"""
        with self.redis_connection() as r:
            return r.hset(i_cid, field, value)

    def get(self, i_cid: str) -> str:
        """Get from persistent redis storage"""
        with self.redis_connection() as r:
            return r.hget(i_cid, "interests")

    def cache_get(self, key: str):
        """Get cache from redis storage"""
        try:
            with self.redis_connection() as r:
                return r.hget(f"cache:{key}", "score")
        except redis.RedisError:
            logging.error("Сouldn't get cache from store")

    def cache_set(self, key: str, score: float, ttl: int | float) -> None:
        """Set cache to redis storage"""
        try:
            with self.redis_connection() as r:
                r.hset(f"cache:{key}", mapping={"score": score})
                r.expire(f"cache:{key}", ttl)
        except redis.RedisError:
            logging.info("Couldn't set cache to store")
