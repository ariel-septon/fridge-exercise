from flask import render_template, flash, redirect, url_for

from .forms import InsertAnItemToShelf, InsertAShelfToRefrigerator
from ... import db
from ...models import Item, Shelf, Refrigerator
from . import insert_actions


@insert_actions.route('/insert-actions')
def choose_action():
    refrigerators = Refrigerator.query.all()
    shelves = Shelf.query.all()
    items = Item.query.all()

    return render_template('insert_actions.html',
                           refrigerators=refrigerators,
                           shelves=shelves,
                           items=items,
                           title='Refrigerators')


@insert_actions.route('/insert-actions/new-shelf/<int:refrigerator_id>', methods=['GET', 'POST'])
def shelf(refrigerator_id):
    """
    Assign a department and a role to an employee
    """
    refrigerator = Refrigerator.query.get_or_404(refrigerator_id)
    form = InsertAShelfToRefrigerator(obj=refrigerator)
    if form.validate_on_submit():
        refrigerator.shelves_list.append(form.shelf.data)
        db.session.add(refrigerator)
        db.session.commit()
        flash('You have successfully assigned a department and role.')
        return redirect(url_for('insert_actions.choose_action'))

    return render_template('insert_shelf.html',
                           refrigerator=refrigerator, form=form,
                           title='Assign Shelf')


@insert_actions.route('/insert-actions/new-item/<int:shelf_id>', methods=['GET', 'POST'])
def item(shelf_id):
    """
    Assign a department and a role to an employee
    """
    current_shelf = Shelf.query.get_or_404(shelf_id)
    form = InsertAnItemToShelf(obj=current_shelf)
    if form.validate_on_submit():
        current_shelf.items_list.append(form.item.data)
        db.session.add(current_shelf)
        db.session.commit()
        flash('You have successfully assigned a department and role.')
        return redirect(url_for('insert_actions.choose_action'))

    return render_template('insert_shelf.html',
                           shelf=current_shelf, form=form,
                           title='Assign Item')
