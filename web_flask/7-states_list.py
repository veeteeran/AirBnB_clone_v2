#!/usr/bin/python3
'''
    Task 8
'''
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)
sto = storage.all('State').values()


@app.route('/states_list', strict_slashes=False)
def states_list():
    ''' Hello HBNB! '''
    return render_template("7-states_list.html", states=sto)


@app.teardown_appcontext
def close_db(self):
    """ Closes the connection at the end of the request."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
