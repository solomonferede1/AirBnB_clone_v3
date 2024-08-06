#!/usr/bin/python3
'''Start flask web app for HBNB clone project'''

import os
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_session(exception=None):
    '''Ensure the session is closed

    This function is called after each request to close the current
    SQLAlchemy session.
    '''
    storage.close()


if __name__ == '__main__':
    '''Run the Flask app if this script is executed directly

    The host and port for the Flask app are set based on environment variables
    `HBNB_API_HOST` and `HBNB_API_PORT`. If these are not set, defaults are
    used: '0.0.0.0' for the host and 5000 for the port. The app is run in
    threaded mode to handle multiple requests simultaneously.
    '''
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(os.environ.get('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)

