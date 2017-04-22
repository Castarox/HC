from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.config.from_object('config')

@app.route("/")
def index():
    return "hello"
