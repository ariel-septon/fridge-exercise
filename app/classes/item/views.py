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

        # redirect to the login page
        return redirect(url_for('auth.login'))

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
