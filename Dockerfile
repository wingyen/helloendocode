FROM python:3.9-slim-buster

WORKDIR /usr/src/app


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV GIT_PYTHON_REFRESH=quiet

#COPY requirements.txt /usr/src/app/requirements.txt

RUN apt-get update && apt-get install -y git


RUN git init && git remote add origin https://github.com/wingyen/helloendocode.git
RUN git config pull.rebase true 
RUN git fetch && git pull origin main


COPY . /usr/src/app/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["gunicorn", "--log-level", "debug", "--keep-alive", "2", "-b", "0.0.0.0:8080", "app:app", "--timeout", "25"]