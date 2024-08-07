#!/usr/bin/python3
'''Index file'''


from models import storage
from flask import jsonify
from api.v1.views import app_views
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": "User"}


@app_views.route('/status')
def status():
    return jsonify({'status': 'OK'})


@app_views.route('/stats')
def get_stats():
    """Counts the number of objects in each class and returns a JSON."""
    counts = {}
    for class_name, model in classes.items():
        try:
            count = storage.count(model)
            counts[class_name] = count
        except Exception as e:
            pass

    return jsonify(counts)
