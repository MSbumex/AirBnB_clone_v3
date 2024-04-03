#!/usr/bin/python3
"""Create Flask app views"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Return status"""
    res = {"status": "OK"}
    return jsonify(res)