#!/usr/bin/python3
""" Task 9 doc """
from models import storage
from models.state import State
from os import getenv
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """ Docstring for teardown """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_list():
    """ display a HTML page: (inside the tag BODY) """
    states = storage.all('State').values()
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = storage.all('City').values()
    else:
        cities = State.cities()
    
    return render_template('8-cities_by_states.html', states=states, cities=cities)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
