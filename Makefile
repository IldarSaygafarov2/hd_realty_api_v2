DC = docker compose
API_CONTAINER = hd-api
MANAGE = python manage.py


.PHONY: up down makemigrations migrate

up:
	${DC} up --build


down:
	${DC} down -v


makemigrations:
	${DC} exec ${API_CONTAINER} ${MANAGE} makemigrations


migrate:
	${DC} exec ${API_CONTAINER} ${MANAGE} migrate --noinput