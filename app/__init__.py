from flask import Flask, render_template, request, redirect, url_for, session as log_in
from app.modules.decorator import *
from app.modules.moderator.moderator import Moderator
from app.modules.location.location import Location

app = Flask(__name__)

app.config.from_object('config')


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        login = request.form.get('login')
        password = request.form.get('password')
        person = Moderator.findModerator(login, password)
        if person == None:
            return render_template('error_login.html')
        log_in['logged_in'] = True
        log_in['login'] = person.login

        return render_template('layout.html', login=log_in['login'])

    return render_template('index.html')


@app.route("/add-moderator", methods=['GET', 'POST'])
def add():
    if request.method == "GET":
        locations = Location.get_all(1)
        return render_template('add-moderator.html', locations = locations)
    login = request.form.get('login')
    password = request.form.get('password')
    new_moderator = Moderator(login, password)
    new_moderator.save()
    return render_template('add-moderator.html', added="Moderator added.")