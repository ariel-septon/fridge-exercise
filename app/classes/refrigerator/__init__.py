from flask import Blueprint

refrigerator = Blueprint('refrigerator', __name__)

from . import views

