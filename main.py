from flask import Flask, render_template
from datetime import datetime
from peewee import fn
from modelsorm import User, Amount

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/time')
def datanow():
    return datetime.now().isoformat()


@app.route('/greeting/<name>')
def show_name(name):
    User.get_or_create(username=name)
    Amount.get_or_create(user=name, amount=0, date_time=datetime.now().isoformat())
    return 'Hello, {}'.format(name)


@app.route('/names')
def show_names():
    rows = list(Amount
        .select(Amount.user, fn.SUM(Amount.amount).alias('balance'))
        .group_by(Amount.user))
    return render_template('hello.html', rows=rows)
