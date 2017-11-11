from app import app
from flask import render_template, Response, request
import json


@app.route("/")
def hello():
    return "Hello World!"

@app.route('/index.html')
def Get_home_page():
    return render_template('index.html')
