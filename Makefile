DC=docker compose
API_CONTAINER=hd-api
MANAGE=python manage.py
LOGS=docker logs


.PHONY: up down makemigrations migrate app-logs

up:
	${DC} up --build

app-logs:
	${LOGS} -f ${API_CONTAINER}

down:
	${DC} down -v


makemigrations:
	${DC} exec ${API_CONTAINER} ${MANAGE} makemigrations


migrate:
	${DC} exec ${API_CONTAINER} ${MANAGE} migrate --noinput