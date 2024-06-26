# Compose
up: 
	docker compose up
down:
	docker compose down
	docker rmi todo-frontend
	docker rmi todo-backend
build:
	docker compose build

# Backend
build-backend:
	docker build -t backend_todo src/backend

RUN_BACKEND = docker run --rm -it backend_todo
run-backend: build-backend
	$(RUN_BACKEND)

bash-backend: build-backend
	$(RUN_BACKEND) sh 

# Frontend
build-frontend:
	docker build -t frontend_todo src/frontend

RUN_FRONTEND = docker run --rm -it frontend_todo
run-frontend: build-frontend
	$(RUN_FRONTEND)

bash-frontend: build-frontend
	$(RUN_FRONTEND) sh
