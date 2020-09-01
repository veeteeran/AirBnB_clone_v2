#!/usr/bin/python3
""" Task 8 doc """
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def teardown(db):
    """ Docstring for teardown """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ display a HTML page: (inside the tag BODY) """

    return render_template('7-states_list.html', states=storage.all('State'))

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
