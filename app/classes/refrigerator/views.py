from flask import flash, redirect, render_template, url_for

from . import refrigerator
from .form import CreateARefrigeratorForm
from ... import db
# from .refrigerator import Refrigerator
from ...models import Refrigerator


@refrigerator.route('/refrigerators')
def list_refrigerators():
    refrigerators = Refrigerator.query.all()
    return render_template('list_pages/refrigerators.html',
                           refrigerators=refrigerators, title='Refrigerators')


@refrigerator.route('/refrigerators/add', methods=['GET', 'POST'])
def add():
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
            flash('Error: refrigerator name already exists.')

        return redirect(url_for('refrigerator.list_refrigerators'))
    return render_template('edit/refrigerator.html', add_refrigerator=add_refrigerator,
                           form=form, title='Add Refrigerator')


@refrigerator.route('/refrigerators/edit/<int:refrigerator_id>', methods=['GET', 'POST'])
def edit(refrigerator_id):
    add_refrigerator = False

    edit_refrigerator = Refrigerator.query.get_or_404(refrigerator_id)
    form = CreateARefrigeratorForm(obj=edit_refrigerator)
    if form.validate_on_submit():
        edit_refrigerator.model = form.model.data
        edit_refrigerator.color = form.color.data
        db.session.add(edit_refrigerator)
        db.session.commit()
        flash('You have successfully edited the refrigerator.')

        return redirect(url_for('refrigerator.list_refrigerators'))

    form.model.data = edit_refrigerator.model
    form.color.data = edit_refrigerator.color
    return render_template('edit/refrigerator.html', add_refrigerator=add_refrigerator,
                           form=form, title="Edit Refrigerator")


@refrigerator.route('/refrigerators/delete/<int:refrigerator_id>', methods=['GET', 'POST'])
def delete(refrigerator_id):
    delete_refrigerator = Refrigerator.query.get_or_404(refrigerator_id)
    db.session.delete(delete_refrigerator)
    db.session.commit()
    flash('You have successfully deleted the refrigerator.')

    return redirect(url_for('refrigerator.list_refrigerators'))
