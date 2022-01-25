import os
import sys
from flask import Flask, redirect, request, jsonify, url_for
import json
from git import Repo
import requests
import datetime
import time
import logging
from config import logger

app = Flask(__name__)
app.logger = logger

@app.after_request
def after_request(response):
    # timestamp this is configured in logger
    #now = datetime.datetime.now()
    #timestamp = now.strftime('[%Y-%b-%d %H:%M]')
    logger.info('%s %s %s %s %s', request.remote_addr, request.method, request.scheme, request.full_path, response.status)
    return response


@app.route("/")
def index():
    return redirect('/helloworld')


@app.route("/helloworld")
def hello():
    args = request.args

    name = args.get("name", default="", type=str)
    greeting = "Hello Stranger"
    if name:
        greeting = "Hello" + "".join(map(lambda x: x if x.islower() else " " + x, name))

    return greeting


@app.route("/versionz")
def versionz():
    repo = Repo(search_parent_directories=True)
    repo_name = repo.remotes.origin.url.split('.git')[0].split('/')[-1]
    repo_hash = repo.head.object.hexsha
    return jsonify(project_name=repo_name, hash=repo_hash)


if __name__ == "__main__":
    app.run(port=8080)
