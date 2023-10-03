from flask import Blueprint

# Create a Blueprint instance for your main routes
main_bp = Blueprint('main', __name__)

# Import your main routes from main_routes.py
from . import main_routes
