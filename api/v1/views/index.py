#!/usr/bin/python3
'''Index file'''


from models import storage
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def status():
    return jsonify({'status': 'OK'})


@app_views.route('/stats')
def get_stats():
    '''The number of objects in each class'''
    counts = {}
    classes = {
        "Amenity": "amenities",
        "City": "cities",
        "Place": "places",
        "Review": "reviews",
        "State": "states",
        "User": "users"
    }
    for cls in classes:
        count = storage.count(cls)
        counts[classes.get(cls)] = count
    return jsonify(counts)
