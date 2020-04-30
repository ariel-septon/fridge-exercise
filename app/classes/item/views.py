from flask import flash, redirect, render_template, url_for

from . import item
from .form import CreateAnItemForm
from ... import db
from ...models import Item


@item.route('/create-an-item', methods=['GET', 'POST'])
def create_an_item():
    """
    Handle requests to the /create-an-item route
    Add an item to the database through the form
    """
    form = CreateAnItemForm()
    if form.validate_on_submit():
        new_item = Item(name=form.name.data,
                        shelf_located=form.shelf_located.data,
                        type_category=form.type_category.data,
                        kosher_category=form.kosher_category.data,
                        expiration_date=form.expiration_date.data,
                        place_taken=form.place_taken.data)

        # add item to the database
        db.session.add(new_item)
        db.session.commit()
        flash('success!')

    # load registration template
    return render_template('auth/creation_form.html', form=form, title='Create an item', object='an item')


@item.route('/items', methods=['GET', 'POST'])
def list_items():
    """
    List all items
    """

    items = Item.query.all()

    return render_template('items.html',
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
        edit_item.shelf_located = form.shelf_located.data
        edit_item.type_category = form.type_category.data
        edit_item.kosher_category = form.kosher_category.data
        edit_item.expiration_date = form.expiration_date.data
        edit_item.place_taken = form.place_taken.data
        db.session.commit()
        flash('You have successfully edited the item.')

        # redirect to the items page
        return redirect(url_for('item.list_items'))

    form.name.data = edit_item.name
    form.shelf_located.data = edit_item.shelf_located
    form.type_category.data = edit_item.type_category
    form.kosher_category.data = edit_item.kosher_category
    form.expiration_date.data = edit_item.expiration_date
    form.place_taken.data = edit_item.place_taken

    return render_template('edit/item.html', action="Edit",
                           add_item=add_item, form=form,
                           item=edit_item, title="Edit Item")


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

