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


if __name__ == '__main__':
    app.run(host='0.0.0.0')
