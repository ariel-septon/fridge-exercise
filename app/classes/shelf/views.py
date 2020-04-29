from flask import flash, redirect, render_template, url_for

from . import shelf
from .form import CreateAShelfForm
from ... import db
from ...models import Shelf


@shelf.route('/create-a-shelf', methods=['GET', 'POST'])
def create():
    """
    Handle requests to the /create-an-item route
    Add an item to the database through the form

    """
    form = CreateAShelfForm()
    if form.validate_on_submit():
        new_shelf = Shelf(level_number=form.level_number.data,
                                        place_size=form.place_size.data)

        # add employee to the database
        db.session.add(new_shelf)
        db.session.commit()
        flash('success!')

        # redirect to the login page
        return redirect(url_for('auth.login'))

    # load registration template
    return render_template('auth/creation_form.html', form=form, title='Create a shelf', object='a shelf')
