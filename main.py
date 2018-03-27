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
    return f'Hello, {name}'
