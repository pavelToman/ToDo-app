build-backend:
	docker build -t backend_todo src/backend

RUN = docker run --rm -it backend_todo

bash-backend: build-backend
	$(RUN) sh

run-backend:
	$(RUN) python3 manage.py runserver 0.0.0.0:8000
