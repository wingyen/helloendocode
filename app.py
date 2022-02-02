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
import signal
from multiprocessing import Process


app = Flask(__name__)
app.logger = logger

os.environ["GIT_PYTHON_REFRESH"] = "quiet"

STOP_TIMEOUT = int(os.environ.get('STOP_TIMEOUT', '5'))
PORT = int(os.environ.get('PORT', '8080'))

@app.after_request
def after_request(response):
    # timestamp this is configured in logger
    #now = datetime.datetime.now()
    #timestamp = now.strftime('[%Y-%b-%d %H:%M]')
    logger.info('%s %s %s %s %s', request.remote_addr, request.method, request.scheme, request.full_path, response.status)
    return response


@app.route("/")
def index():
    return redirect('/helloworld'), 302


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

def signal_handler(sig, _frame):
    """Handling the SIGTERM event"""
    print(f'Received signal {sig} - stopping gracefully')
    count = STOP_TIMEOUT
    while count > 0:
        print(f'cleaning up: {count}')
        time.sleep(1)
        count -= 1
    print('Finished cleanup...')

def exit_handler(signum, frame):
    print("PID:", os.getpid())
    print('Exiting....')
    exit(0)


signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGTERM, exit_handler)



if __name__ == "__main__":
    app.run(port=8080)
