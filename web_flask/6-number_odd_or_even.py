#!/usr/bin/python3
"""Task 0 Docstring"""
from flask import Flask, render_template
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


@app.route('/python', defaults={'text': None}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """Starts a Flask web application,
       display “C ” followed by the value of the text variable
    """
    if text is None:
        return 'Python is cool'

    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Starts a Flask web application,
       display “n is a number” only if n is an integer
    """
    if type(n) is int:
        return 'n is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Starts a Flask web application,
       display “n is a number” only if n is an integer
    """
    if type(n) is int:
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Starts a Flask web application,
       display “n is a number” only if n is an integer
    """
    # Checks for even numbers
    if type(n) is int:
        if n % 2 == 0:
            parity = 'even'
        else:
            parity = 'odd'
        return render_template('6-number_odd_or_even.html', n=n, parity=parity)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
