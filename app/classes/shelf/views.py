from flask import flash, redirect, render_template, url_for

from . import shelf
from .form import CreateAShelfForm
from ... import db
#from .shelf import Shelf
from ...models import Shelf


@shelf.route('/shelves', methods=['GET', 'POST'])
def list_shelves():
    """
    List all shelves
    """
    shelves = Shelf.query.all()
    return render_template('list_pages/shelves.html',
                           shelves=shelves, title='Shelves')


@shelf.route('/shelves/add', methods=['GET', 'POST'])
def add():
    """
    Add a shelf to the database
    """
    add_shelf = True

    form = CreateAShelfForm()
    if form.validate_on_submit():
        new_shelf = Shelf(level_number=form.level_number.data,
                          place_size=form.place_size.data)

        try:
            # add role to the database
            db.session.add(new_shelf)
            db.session.commit()
            flash('You have successfully added a new shelf.')
        except:
            # in case role name already exists
            flash('Error: shelf name already exists.')

        # redirect to the roles page
        return redirect(url_for('shelf.list_shelves'))

    # load role template
    return render_template('edit/shelf.html', add_shelf=add_shelf,
                           form=form, title='Add Shelf')


@shelf.route('/shelves/edit/<int:shelf_id>', methods=['GET', 'POST'])
def edit(shelf_id):
    """
    Edit a shelf
    """

    add_shelf = False

    edit_shelf = Shelf.query.get_or_404(shelf_id)
    form = CreateAShelfForm(obj=edit_shelf)
    if form.validate_on_submit():
        edit_shelf.level_number = form.level_number.data
        edit_shelf.place_size = form.place_size.data
        db.session.add(edit_shelf)
        db.session.commit()
        flash('You have successfully edited the shelf.')

        # redirect to the roles page
        return redirect(url_for('shelf.list_shelves'))

    form.level_number.data = edit_shelf.level_number
    form.place_size.data = edit_shelf.place_size
    return render_template('edit/shelf.html', add_shelf=add_shelf,
                           form=form, title="Edit Shelf")


@shelf.route('/shelves/delete/<int:shelf_id>', methods=['GET', 'POST'])
def delete(shelf_id):
    """
    Delete a refrigerator from the database
    """

    delete_shelf = Shelf.query.get_or_404(shelf_id)
    db.session.delete(delete_shelf)
    db.session.commit()
    flash('You have successfully deleted the shelf.')

    # redirect to the roles page
    return redirect(url_for('shelf.list_shelves'))
