import flask
from flask import Flask, jsonify, request, render_template, redirect, url_for
import json

app = Flask(__name__)

URL_WEB = 'https://synit-web.herokuapp.com/'

@app.route('/')
def home():
    return redirect(URL_WEB)

if __name__ == '__main__':
    app.run()