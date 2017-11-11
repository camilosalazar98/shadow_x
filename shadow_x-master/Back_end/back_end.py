from flask import Flask
from flask import render_template, Response, request

app = Flask(__name__)

@app.route("/home")
def hello():
    return "Hello World!"
