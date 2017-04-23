
from flask import Flask, render_template, request, redirect, url_for, jsonify
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
        if user:
            user = {'name': user.login, 'type': user.type, 'idx': user.idx}
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
    return redirect(url_for('locations'))


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
    return redirect(url_for('locations'))



@app.route("/edit/<location_id>", methods=["GET", "POST"])
def edit_location(location_id):
    location = Location.get_by_id(location_id)
    if request.method == "GET":
        return render_template('location_edit.html', location=location)
    name = request.form.get('name')
    beacon = request.form.get('beacon')
    location.name = name
    location.beacon_major = beacon
    location.save()
    return redirect(url_for('locations'))

@app.route("/add_location/", methods=["GET", "POST"])
def add_location():
    if request.method == "POST":
        name = request.form.get('name')
        beacon = request.form.get('beacon')
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')
        moderator_id = session['user']['idx']
        try:
            location = Location(name, beacon, moderator_id, latitude, longitude)
            location.save()
            return redirect(url_for('locations'))
        except:
            return redirect(url_for('add_location'))
    return render_template('add_location.html')


@app.route('/android/login', methods=['POST'])
def and_login():
    if request.method == 'POST':
        login = request.json['login']
        password = request.json['password']
        print(login)
        print(password)
        value = {'status': True,  "login": login, "level": 2, "score": 22}
        return jsonify(value)


@app.route('/android/beacon', methods=['POST'])
def checkBeacon():
    beacon_list = [36817]
    if request.method == 'POST':
        beacon_id = request.json['major']
        print(beacon_id)
        value = {'status':True}
        return jsonify(value)


@app.route('/android/quiz', methods=['POST'])
def quiz():
    print('quiz')
    print(request.json['major'])
    value = {'question1':{'question': 'Gdzie odbyl sie Hackaton', 'answer1': 'Codecool', 'answer2': 'AGH', 'answer3': 'UJ', 'answer4': 'UP', 'correct': 1},
             'question2':{'question': 'Platynowy sponsor', 'answer1': 'cos', 'answer2': 'cso', 'answer3': 'cos', 'answer4': 'cos', 'correct': 2}
             }

    return jsonify(value)

@app.route('/android/set_score', methods=['POST'])
def getScore():
    score = request.json['score']
    print(score)
    value = {'status': True}
    return jsonify(value)

@app.route('/android/leader_board')
def getLeaderBoard():
    value = {
        "p1":{"nick":"kamil", "points":174},
        "p2":{"nick":"Mateusz", "points":174},
        "p3":{"nick":"Sebastian", "points":172},
        "p4":{"nick":"Krzysztof ", "points":170},
        "p5":{"nick":"Kamil", "points":169},
        "p6":{"nick":"Mateusz", "points":165},
        "p7":{"nick":"Sebastian", "points":160},
        "p8":{"nick":"Krzysztof", "points":140},
        "p9":{"nick":"Kamil", "points":121},
        "p10":{"nick":"Mateusz", "points":69}
    }
    return jsonify(value)

@app.route('/android/map', methods=['POST'])
def getLocation():
    value = {
        "location1":{"y":50.051706, "x":19.948601, 'status': True, "name":"Synagoga Stara"},
        "location2":{"y":50.047591, "x":19.961799, 'status': False, "name":"Fabryka Emalia Oskara Schindlera"}
    }
    return jsonify(value)


@app.route('/android/register', methods=['POST'])
def register():
    login = request.json['login']
    password = request.json['password']

    value = {'status': True}
    return jsonify(value)

