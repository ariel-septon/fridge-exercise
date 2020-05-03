from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .. import db
from config import Config

# from ..models import User


@main.route('/', methods=['GET', 'POST'])
def index():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html',
                           name=session.get('name'),
                           known=session.get('known', False),
                           current_time=datetime.utcnow())
