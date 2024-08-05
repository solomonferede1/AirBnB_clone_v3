#!/user/bin/python3
'''Index file'''


from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def status():
    return jsonify({'status': 'OK'})
