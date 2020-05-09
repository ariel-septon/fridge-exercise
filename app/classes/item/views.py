from flask import flash, redirect, render_template, url_for

from . import item
from .form import CreateAnItemForm
from ... import db
from ...models import Item


@item.route('/items', methods=['GET', 'POST'])
def list_items():
    """
    List all items
    """

    items = Item.query.all()

    return render_template('list_pages/items.html',
                           items=items, title="Items")


@item.route('/items/edit/<int:item_id>', methods=['GET', 'POST'])
def edit(item_id):
    """
    Edit an item
    """

    add_item = False

    edit_item = Item.query.get_or_404(item_id)
    form = CreateAnItemForm(obj=item)
    if form.validate_on_submit():
        edit_item.name = form.name.data
        edit_item.type_category = form.type_category.data
        edit_item.kosher_category = form.kosher_category.data
        edit_item.expiration_date = form.expiration_date.data
        edit_item.place_taken = form.place_taken.data
        db.session.commit()
        flash('You have successfully edited the item.')

        # redirect to the items page
        return redirect(url_for('item.list_items'))

    form.name.data = edit_item.name
    form.type_category.data = edit_item.type_category
    form.kosher_category.data = edit_item.kosher_category
    form.expiration_date.data = edit_item.expiration_date
    form.place_taken.data = edit_item.place_taken

    return render_template('edit/item.html', action="Edit",
                           add_item=add_item, form=form,
                           item=edit_item, title="Edit Item")


@item.route('/items/add', methods=['GET', 'POST'])
def add():
    """
    Add a shelf to the database
    """
    add_item = True

    form = CreateAnItemForm()
    if form.validate_on_submit():
        new_item = Item(name=form.name.data,
                        type_category=form.type_category.data,
                        kosher_category=form.kosher_category.data,
                        expiration_date=form.expiration_date.data,
                        place_taken=form.place_taken.data)

        try:
            # add role to the database
            db.session.add(new_item)
            db.session.commit()
            flash('You have successfully added a new shelf.')
        except:
            # in case role name already exists
            flash('Error: shelf name already exists.')

        # redirect to the roles page
        return redirect(url_for('item.list_items'))

    # load role template
    return render_template('edit/item.html', add_item=add_item,
                           form=form, title='Add Item')


@item.route('/departments/delete/<int:item_id>', methods=['GET', 'POST'])
def delete(item_id):
    """
    Delete a department from the database
    """

    delete_item = Item.query.get_or_404(item_id)
    db.session.delete(delete_item)
    db.session.commit()
    flash('You have successfully deleted the item.')

    # redirect to the items page
    return redirect(url_for('item.list_items'))
