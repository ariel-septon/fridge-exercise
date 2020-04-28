from flask import Blueprint

refrigerators_list = Blueprint('refrigerators_list', __name__)

from ...main import views, errors


