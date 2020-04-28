from flask import Blueprint

shelf = Blueprint('shelf', __name__)

from ...main import views, errors


