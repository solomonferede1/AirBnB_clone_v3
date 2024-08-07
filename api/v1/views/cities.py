#!/usr/bin/python3
'''Cities'''

from models.city import City
from models.state import State
from models import storage
from flask import jsonify, request, abort
from api.v1.views import app_views


@app_views.route('/states/<state_id>/cities', methods=['GET'], strict_slashes=False)
def get_cities(state_id):
    '''Retrieve cities by state'''
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    cities = state.cities
    return jsonify([city.to_dict() for city in cities])