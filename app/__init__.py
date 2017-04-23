from flask import Flask, render_template, request, redirect, url_for, session as log_in
from app.modules.decorator import *
from app.modules.moderator.moderator import Moderator
from app.modules.location.location import Location

app = Flask(__name__)

app.config.from_object('config')

@app.route('/locations/')
def locations():
    user = session['user']
    locations = Location.get_all(user['idx'])
    #     return render_template('layout.html', login=log_in['login'], locations = locations)
    return render_template('layout.html', locations = locations)


@app.before_request
def before_request():
    if 'user' not in session and request.endpoint != 'login':
        return redirect(url_for('login'))
# @app.route("/", methods=['GET', 'POST'])
# def index():
#     user = session['user']
#
#     return render_template('index.html', user=user)
    #
    # if request.method == "POST":
    #     login = request.form.get('login')
    #     password = request.form.get('password')
    #     person = Moderator.findModerator(login, password)
    #     if person == None:
    #         return render_template('error_login.html')
    #     log_in['logged_in'] = True
    #     log_in['login'] = person.login
    #     locations = Location.get_all(1)
    #     return render_template('layout.html', login=log_in['login'], locations = locations)

    # return render_template('index.html')

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = Moderator.findModerator(request.form['login'], request.form['password'])
        user = {'name': user.login, 'type': user.type, 'idx': user.idx}
        if user:
            session['user'] = user
            return redirect(url_for('locations'))
        return redirect(url_for('login'))
    return render_template("login.html")
    # if request.method == "POST":
    #     login = request.form.get('login')
    #     password = request.form.get('password')
    #     person = Moderator.findModerator(login, password)
    #     if person == None:
    #         return render_template('error_login.html')
    #     log_in['logged_in'] = True
    #     log_in['login'] = person.login
    #     locations = Location.get_all(1)
    #     return render_template('layout.html', login=log_in['login'], locations = locations)
    # return render_template('index.html')

@app.route("/add-moderator", methods=['GET', 'POST'])
def add():
    if request.method == "GET":
        login = request.form.get('login')
        password = request.form.get('password')
        new_moderator = Moderator(login, password)
        new_moderator.save()
        return render_template('add-moderator.html', added="Moderator added.")
    return redirect(url_for('locations'))