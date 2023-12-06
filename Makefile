SRC=$(CURDIR)/src
TESTS=$(CURDIR)/tests

requirements:
	pip install -r $(CURDIR)/requirements.txt -r $(CURDIR)/requirements-dev.txt

format:
	isort $(SRC) $(TESTS)
	black $(SRC) $(TESTS)

test:
	python -m pytest -- $(CURDIR)/

build:
	docker-compose build

run:
	docker-compose up --build

build-run: build run

all: requirements format test