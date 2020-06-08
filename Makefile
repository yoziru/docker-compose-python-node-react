build:
	docker-compose build

up: build
	docker-compose up

down: build
	docker-compose down

backend_bash: build
	docker-compose run --rm backend /bin/bash

frontend_bash: build
	docker-compose run --rm frontend /bin/bash

test: build
	docker-compose run backend python -m pytest ./tests
	docker-compose run frontend yarn test --watchAll=false

lint:
	docker-compose run backend isort --recursive .
	docker-compose run backend black .
	docker-compose run backend flake8 . --statistics
	docker-compose run frontend yarn format
