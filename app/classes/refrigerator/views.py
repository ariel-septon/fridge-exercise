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

        db.session.add(new_refrigerator)
        db.session.commit()
        flash('success!')

        # redirect to the login page
        return redirect(url_for('shelf.create'))

    # load registration template
    return render_template('auth/creation_form.html', form=form, title='Create a refrigerator', object='a refrigerator')


@refrigerator.route('/refrigerators')
def list_refrigerators():
    """
    List all refrigerators
    """
    refrigerators = Refrigerator.query.all()
    return render_template('refrigerators.html',
                           refrigerators=refrigerators, title='Refrigerators')


@refrigerator.route('/refrigerators/add', methods=['GET', 'POST'])
def add():
    """
    Add a refrigerator to the database
    """
    add_refrigerator = True

    form = CreateARefrigeratorForm()
    if form.validate_on_submit():
        new_refrigerator = Refrigerator(model=form.model.data,
                                        color=form.color.data)

        try:
            # add role to the database
            db.session.add(new_refrigerator)
            db.session.commit()
            flash('You have successfully added a new refrigerator.')
        except:
            # in case role name already exists
            flash('Error: refrigerator name already exists.')

        # redirect to the roles page
        return redirect(url_for('refrigerator.list_refrigerators'))

    # load role template
    return render_template('edit/refrigerator.html', add_refrigerator=add_refrigerator,
                           form=form, title='Add Refrigerator')


@refrigerator.route('/refrigerators/edit/<int:refrigerator_id>', methods=['GET', 'POST'])
def edit(refrigerator_id):
    """
    Edit a refrigerator
    """

    add_refrigerator = False

    edit_refrigerator = Refrigerator.query.get_or_404(refrigerator_id)
    form = CreateARefrigeratorForm(obj=edit_refrigerator)
    if form.validate_on_submit():
        edit_refrigerator.model = form.model.data
        edit_refrigerator.color = form.color.data
        db.session.add(edit_refrigerator)
        db.session.commit()
        flash('You have successfully edited the refrigerator.')

        # redirect to the roles page
        return redirect(url_for('refrigerator.list_refrigerators'))

    form.model.data = edit_refrigerator.model
    form.color.data = edit_refrigerator.color
    return render_template('edit/refrigerator.html', add_refrigerator=add_refrigerator,
                           form=form, title="Edit Refrigerator")


@refrigerator.route('/refrigerators/delete/<int:refrigerator_id>', methods=['GET', 'POST'])
def delete(refrigerator_id):
    """
    Delete a refrigerator from the database
    """

    delete_refrigerator = Refrigerator.query.get_or_404(refrigerator_id)
    db.session.delete(delete_refrigerator)
    db.session.commit()
    flash('You have successfully deleted the refrigerator.')

    # redirect to the roles page
    return redirect(url_for('refrigerator.list_refrigerators'))
