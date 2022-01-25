venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt


gunicorn:
	gunicorn -b 0.0.0.0:8080 app:app


build:
	docker build -t helloflask .

run:
	docker run -it -p 8080:8080 --rm --name helloflask helloflask
