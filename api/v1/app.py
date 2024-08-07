#!/usr/bin/python3
'''This module Starts a flask web app for HBNB clone project'''
import os
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_session(exception=None):
    '''Ensure the session is closed'''
    storage.close()


@app.errorhandler(404)
def error_404(error):
    '''Handle 404 error'''
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    '''Run the Flask app if this script is executed directly'''

    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(os.environ.get('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
