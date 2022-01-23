import os
from flask import Flask, redirect, request, jsonify
from git import Repo

app = Flask(__name__)


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
