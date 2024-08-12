#!/usr/bin/python3
"""
Module for Flask App that integrates with AirBnB static HTML Template
"""
import uuid
from flask import Flask, render_template, url_for
from models import storage

# flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


# begin flask page rendering
@app.teardown_appcontext
def teardown_db(exception):
    """Method calls .close() after requests"""
    storage.close()


@app.route('/100-hbnb/')
def hbnb_filters(the_id=None):
    """Method handles request to custom templates"""
    states = storage.all('State').values()
    amens = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    cache_id = (str(uuid.uuid4()))

    return render_template('100-hbnb.html',states=states,amens=amens,
                           places=places,users=users,cache_id=cache_id)


if __name__ == "__main__":
    """Flask App"""
    app.run(host=host, port=port)
