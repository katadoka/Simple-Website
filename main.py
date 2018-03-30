from flask import Flask
from datetime import datetime
from flask import render_template

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
        f_out.write(f'{name}\n')
    return 'Hello, {}'.format(name)


@app.route('/names')
def show_names():
    names = []
    with open('names.txt', 'r') as f_out:
        for line in f_out:
            names.append(line)
    return render_template('hello.html', names=names)
