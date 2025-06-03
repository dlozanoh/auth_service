# Makefile for the auth_service project

.PHONY: build run clean

build:
	docker build -t auth_service .

run:
	docker run -p 8000:8000 auth_service

clean:
	docker rmi auth_service || true