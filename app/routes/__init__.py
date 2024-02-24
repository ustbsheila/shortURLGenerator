from flask import Blueprint

main_bp = Blueprint('main', __name__)

# Import routes from the sub-modules
from . import main_routes