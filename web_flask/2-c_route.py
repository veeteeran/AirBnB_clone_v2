#!/usr/bin/python3
"""Task 0 Docstring"""
from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Starts a Flask web application, display Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """Starts a Flask web application, display HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Starts a Flask web application,
       display “C ” followed by the value of the text variable
    """
    return 'C %s' % text.replace('_', ' ')

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
