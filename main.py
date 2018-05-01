from flask import Flask
from datetime import datetime
from flask import render_template
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
    return 'Hello, {}'.format(name)


def search_name(name):
    query = (Amount
        .select(Amount.user_id, Amount.amount)
        .where(Amount.user_id == name))
    return query


@app.route('/names')
def show_names():
    query_names = (User
                .select(User.username))

    names = []
    for row in query_names:
        current_balance_name = 0
        for amount in search_name(row.username):
            current_balance_name += amount.amount
        names.append('{} - {}'.format(row.username, current_balance_name))
    return render_template('hello.html', names=names)
