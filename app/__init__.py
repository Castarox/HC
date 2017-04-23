from flask import Flask, render_template, request, redirect, url_for, session as log_in
from app.modules.decorator import *
from app.modules.moderator.moderator import Moderator
from app.modules.location.location import Location
from app.modules.question.question import Question

app = Flask(__name__)

app.config.from_object('config')

@app.route('/locations/')
def locations():
    user = session['user']
    locations = Location.get_all(user['idx'])
    return render_template('layout.html', locations = locations)


@app.before_request
def before_request():
    if 'user' not in session and request.endpoint != 'login':
        return redirect(url_for('login'))


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


@app.route("/add-moderator", methods=['GET', 'POST'])
def add():
    if request.method == "GET":
        login = request.form.get('login')
        password = request.form.get('password')
        new_moderator = Moderator(login, password)
        new_moderator.save()
        return render_template('add-moderator.html', added="Moderator added.")

@app.route("/add_question/<location_id>", methods=['GET', 'POST'])
def add_question(location_id):
    if request.method == "GET":
        return render_template('add_question.html', location_id=location_id)
    question = request.form.get('question')
    answer1 = request.form.get('answer1')
    answer2 = request.form.get('answer2')
    answer3 = request.form.get('answer3')
    correct = request.form.get('answer4')
    new_question = Question(location_id, question, answer1, answer2, answer3, correct)
    new_question.save()
    return redirect(url_for('layout1'))


@app.route("/questions/<location_id>", methods=['GET', 'POST'])
def view_questions(location_id):
    if request.method == "GET":
        location = Location.get_by_id(location_id)
        questions = Question.get_all(location_id)
        return render_template('questions.html', location=location, questions=questions)


@app.route("/remove/<location_id>/<question_id>")
def remove_question(location_id, question_id):
    question = Question.get_by_id(question_id)
    question.delete()
    questions = Question.get_all(location_id)
    location = Location.get_by_id(location_id)
    # return render_template('questions.html', location=location, questions=questions)
    return render_template('questions.html', location=location, questions=questions)


@app.route("/remove/<location_id>")
def remove_location(location_id):
    location = Location.get_by_id(location_id)
    location.delete()
    return redirect(url_for('layout1'))

