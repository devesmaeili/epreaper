DOCKER_COMPOSE_PATH = compose.yaml

init:
	docker compose -f $(DOCKER_COMPOSE_PATH) build --no-cache
build:
	docker compose -f $(DOCKER_COMPOSE_PATH) build
start:
	docker compose -f $(DOCKER_COMPOSE_PATH) up
stop:
	docker compose -f $(DOCKER_COMPOSE_PATH) down
run:
	stop build start