from flask import Flask
from datetime import datetime


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/time')
def datanow():
    return datetime.now().isoformat()


@app.route('/greeting/<name>')
def show_name(name):
    with open('names.txt', 'a') as f_out:
        f_out.write(f'{name }')
    return 'Hello, {}'.format(name)


@app.route('/names')
def show_names():
    with open('names.txt', 'r') as f_out:
        return f_out.read()
