.PHONY: build up test

build:
	docker-compose build

up:
	docker-compose up

test:
	docker-compose run --rm api_scoring pytest -v
