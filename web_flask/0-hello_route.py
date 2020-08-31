#!/usr/bin/python3
"""Task 0 Docstring"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Starts a Flask web application"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
