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


if __name__ == '__main__':
    app.run(host='0.0.0.0')
