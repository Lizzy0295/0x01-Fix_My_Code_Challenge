#!/usr/bin/python3
""" Views module """

from flask import Blueprint
from api.v1.views.index import status  # Import specific view functions

# Create a Blueprint for API v1 views
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

# Register the status view function under the app_views blueprint
app_views.add_url_rule('/status', 'status', status, methods=['GET'])

