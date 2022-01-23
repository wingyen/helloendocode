from flask import Flask, redirect, request

app = Flask(__name__)


@app.route("/")
def index():
    return redirect('/helloworld')


@app.route("/helloworld", )
def hello():
    args = request.args

    name = args.get("name", default="", type=str)
    name = "".join(map(lambda x: x if x.islower() else " " + x, name))
    return name




if __name__ == "__main__":
    app.run(port=8080)
