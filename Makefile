up:
	docker-compose up

down:
	docker-compose down

build:
	docker-compose build

backend_bash:
	docker-compose run --rm backend /bin/bash

frontend_bash:
	docker-compose run --rm frontend /bin/bash
