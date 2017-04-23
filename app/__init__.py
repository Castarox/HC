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