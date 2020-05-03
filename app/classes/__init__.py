from flask import Blueprint

methods = Blueprint('methods', __name__)

from . import views
