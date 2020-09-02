#!/usr/bin/python3
""" Task 8 doc """
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """ Docstring for teardown """
    storage.close()


@app.route('/states', defaults={'id': None}, strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ display a HTML page: (inside the tag BODY) """
    states = storage.all('State')
    print(states)
    if id is not None:
        id = 'State.' + id
    return render_template('9-states.html', states=states, id=id)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
