from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/upload/", methods=["POST"])
def upload_file():
    prediction = 0
    return str(prediction)
