#!/usr/bin/python3
"""
Index views
"""

from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'])
def get_status():
    """
    Get and return status of a request
    """
    return jsonify({"status": "OK"})
