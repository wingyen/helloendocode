FROM python:3.9-slim-buster

WORKDIR /usr/src/app


ENV VIRTUAL_ENV=/opt/env
RUN python -m venv $VIRTUAL_ENV
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"
ENV PYTHONUNBUFFERED = 1

COPY . .


RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "make run" ]