.PHONY: build up test

build:
	docker-compose build

up:
	docker-compose up

test:
	docker-compose up --build -d
	docker-compose exec api_scoring python3 -m scripts.fill_redis_for_test
	docker-compose exec api_scoring pytest -v tests/
