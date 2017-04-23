from flask import Flask, render_template, request, redirect, url_for, session as log_in
from app.modules.decorator import *
from app.modules.moderator.moderator import Moderator
from app.modules.location.location import Location
from app.modules.question.question import Question

app = Flask(__name__)

app.config.from_object('config')


@app.route("/", methods=['GET', 'POST'])
def index():
    # if request.method == "POST":
    #     login = request.form.get('login')
    #     password = request.form.get('password')
    #     person = Moderator.findModerator(login, password)
    #     if person == None:
    #         return render_template('error_login.html')
    #     log_in['logged_in'] = True
    #     log_in['login'] = person.login
    #     locations = Location.get_all(1)
    #     print(locations[0])
    #     return render_template('layout.html', login=log_in['login'], locations=locations)
    #
    locations = Location.get_all(1)
    return render_template('layout.html', locations=locations)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        login = request.form.get('login')
        password = request.form.get('password')
        person = Moderator.findModerator(login, password)
        if person == None:
            return render_template('error_login.html')
        log_in['logged_in'] = True
        log_in['login'] = person.login
        return redirect(url_for(index))

    return render_template('index.html')



@app.route("/layout", methods=['GET', 'POST'])
def layout1():
    return redirect(url_for('index'))

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
    print("LCOATION ID")
    print(location_id)
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
