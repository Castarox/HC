from flask import Flask, render_template, request, redirect, url_for
from app.modules.decorator import *

from app.modules.user.user import User

app = Flask(__name__)

app.config.from_object('config')


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        user = User.isUser('Marcin', "xxx")
        print(user.login)
    return render_template('index.html')
