#!/usr/bin/python3

"""Script that starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """app displaying Hello"""

    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_route_v1():
    """App displaying 2 cmd"""

    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hello_route_v2(text):
    """App displaying 3 cmd"""

    return 'C ' + text.replace('_',' ')


@app.route("/python", strick_slashes=False)
@app.route("/python/<text>", strick_slashes=False)
def hello_route_v3(text='is cool'):
    """App displaying 4 cmd"""

    return 'python' + text.replace('_', ' ')


@app.route("/number/<int:n>", strick_slashes=False)
def hello_route_v4(n):
    """App displaying 4 cmd"""

    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
