DC = docker compose


.PHONY: up down

up:
	${DC} up --build


down:
	${DC} down -v