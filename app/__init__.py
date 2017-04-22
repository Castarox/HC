from flask import Flask, render_template, request, redirect, url_for
from app.modules.decorator import *

app = Flask(__name__)

app.config.from_object('config')


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        print('dupa')
        print(request.form.get('login'))
        print(request.form.get('password'))
    return render_template('index.html')
