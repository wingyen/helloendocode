venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt


run:
	gunicorn -b 0.0.0.0:8080 app:app
