from flask import flash, redirect, render_template, url_for

from . import refrigerator
from .form import CreateARefrigeratorForm
from ... import db
from ...models import Refrigerator


@refrigerator.route('/create-a-refrigerator', methods=['GET', 'POST'])
def create():
    """
    Handle requests to the /create-an-item route
    Add an item to the database through the form
    """
    form = CreateARefrigeratorForm()
    if form.validate_on_submit():
        new_refrigerator = Refrigerator(model=form.model.data,
                                        color=form.color.data)

        # add employee to the database
        # db.session.add(new_refrigerator)
        # db.session.commit()
        flash('success!')

        # redirect to the login page
        return redirect(url_for('shelf.create'))

    # load registration template
    return render_template('auth/creation_form.html', form=form, title='Create a refrigerator', object='a refrigerator')
