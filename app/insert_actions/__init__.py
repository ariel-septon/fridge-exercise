from flask import Blueprint

insert_actions = Blueprint('insert_actions', __name__)

from .import views
