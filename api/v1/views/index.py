#!/usr/bin/python3
"""Create Flask app views"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Return status"""
    res = {"status": "OK"}
    return jsonify(res)


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """Return stats"""
    stats = {}
    for k, v in storage.all().items():
        stats[k] = v.to_dict()
    return jsonify(res)