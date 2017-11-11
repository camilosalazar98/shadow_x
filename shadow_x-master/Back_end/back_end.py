from flask import Flask
from flask import render_template, Response, request
import json



app = Flask(__name__)

@app.route("/home_page")
def hello():
    '''
    Returns a static webpage for now.
    '''
    return render_template('home.html')
'''
The return renders page.
'''
@app.route("/home_page")
def hello():
    '''
    Returns a static webpage for now.
    '''
    return render_template('home.html')

@app.route("/aboutus")
def hello():
    '''
    Returns a static webpage for now.
    '''
    return render_template('home.html')

@app.route("/")
def hello():
    '''
    Returns a static webpage for now.
    '''
    return render_template('home.html')
