FROM python:3.9-slim-buster

WORKDIR /usr/src/app


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV GIT_PYTHON_REFRESH=quiet

COPY requirements.txt /usr/src/app/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app/

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app" ]