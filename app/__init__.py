from flask import Flask, render_template, request, redirect, url_for, jsonify
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


@app.route('/android/login', methods=['POST'])
def and_login():
    if request.method == 'POST':
        login = request.json['login']
        password = request.json['password']
        print(login)
        print(password)
        value = {'status': False, "login": login, "level": 2}
        return jsonify(value)
