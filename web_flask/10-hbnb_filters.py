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


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters(id):
    """ display a HTML page: like 6-index.html """
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()

    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
