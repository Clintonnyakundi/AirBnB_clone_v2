#!/usr/bin/python3
"""
Starts a flask web app
Listen on 0.0.0.0 port 5000
/: display 'Hello HBNB!'
use option strict_slashes=False in route
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """
    Displays 'Hello HBNB!'
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """
    Displays 'HBNB'
    """
    return "HBNB"


@app.route("/c/<string:text>", strict_slashes=False)
def C_fun(text):
    """
    Display C followed by value of text variable
    """
    text = text.replace('_', ' ')
    return "C %s" % text


@app.route("/python", strict_slashes=False)
@app.route("/python/<string:text>", strict_slashes=False)
def pytext(text="is cool"):
    """
    Display 'Python' followed by value of text variable
    """
    text = text.replace('_', ' ')
    return "Python %s" % text


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """
    display “n is a number” only if n is an integer
    """
    return "%i is a number" % n


if __name__ == '__main__':
    app.run(host='0.0.0.0')
