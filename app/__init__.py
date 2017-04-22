from flask import Flask, render_template, request, redirect, url_for, session as log_in
from app.modules.decorator import *
from app.modules.user.user import *
app = Flask(__name__)

app.config.from_object('config')


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        login = request.form.get('login')
        password = request.form.get('password')
        # person = User.find_user(login, password)
        person = None
        # if person == None:
        #     return render_template('error_login.html')
        log_in['logged_in'] = True
        log_in['login'] = "Durax"  #person.login
        log_in['level'] = "15"  #person.level
        log_in['status'] = "user"  #person.status
        dupa = "dupaaa"
        return render_template('layout.html', user=log_in['login'])

    return render_template('index.html')


@app.route('/main', methods=['GET'])
def main():
    render_template()