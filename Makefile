build-backend:
	docker build -t backend_todo src/backend

RUN_BACKEND = docker run --rm -it backend_todo

bash-backend: build-backend
	$(RUN_BACKEND) sh

run-backend: build-backend
	$(RUN_BACKEND) python3 manage.py runserver 0.0.0.0:8000

build-frontend:
	docker build -t frontend_todo src/frontend

RUN_FRONTEND = docker run --rm -it frontend_todo

bash-frontend: build-frontend
	$(RUN_FRONTEND) sh

run-frontend: build-frontend
	$(RUN_FRONTEND) npm run dev
	
