from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
# from .forms import NameForm
from .. import db


# from ..models import User


@main.route('/', methods=['GET', 'POST'])
def index():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")


@main.route('/ret', methods=['GET', 'POST'])
def index_more():
    return 'ret'
