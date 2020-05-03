import datetime

from flask import render_template, session, redirect, url_for

from run import app
from . import methods
from ..models import Refrigerator, Item
from flask import json
from .forms import CompareRefrigerators, CompareShelves, CompareItems, ChooseRefrigerator


@methods.route('/methods', methods=['GET', 'POST'])
def list_methods():
    """
    Render the homepage template on the / route
    """
    refrigerator_form = CompareRefrigerators()
    if refrigerator_form.validate_on_submit():
        return compare_refrigerators(refrigerator_form)
    shelf_form = CompareShelves()
    if shelf_form.validate_on_submit():
        return compare_shelves(shelf_form)
    item_form = CompareItems()
    if item_form.validate_on_submit():
        return compare_items(item_form)
    choose_refrigerator = ChooseRefrigerator()
    if choose_refrigerator.validate_on_submit():
        return place_left(choose_refrigerator.refrigerator.data)
    choose_refrigerator1 = ChooseRefrigerator()
    if choose_refrigerator1.validate_on_submit():
        return whats_to_eat(choose_refrigerator1.refrigerator.data)
    return render_template('list_pages/mthods.html', template=True, refrigerator_form=refrigerator_form,
                           shelf_form=shelf_form, item_form=item_form,
                           choose_refrigerator=choose_refrigerator,
                           choose_refrigerator1=choose_refrigerator1)


def compare_shelves(form):
    shelf1 = shelf_creator(form.shelf1.data)
    shelf2 = shelf_creator(form.shelf2.data)
    response = app.response_class(
        response=json.dumps(shelf1.__eq__(shelf2), default=lambda o: o.__dict__,
                            sort_keys=True, indent=4),
        status=200,
        mimetype='application/json'
    )
    return response


def compare_refrigerators(form):
    refrigerator1 = refrigerator_creator(form.refrigerator1.data)
    refrigerator2 = refrigerator_creator(form.refrigerator2.data)
    response = app.response_class(
        response=json.dumps(refrigerator1.__eq__(refrigerator2), default=lambda o: o.__dict__,
                            sort_keys=True, indent=4),
        status=200,
        mimetype='application/json'
    )
    return response


def compare_items(form):
    item1 = item_creator(form.item1.data, 0)
    item2 = item_creator(form.item2.data, 0)
    response = app.response_class(
        response=json.dumps(item1.__eq__(item2), default=lambda o: o.__dict__,
                            sort_keys=True, indent=4),
        status=200,
        mimetype='application/json'
    )
    return response


@methods.route('/methods/cleanup/<int:refrigerator_id>')
def cleanup_refrigerator(refrigerator_id):
    get_refrigerator = Refrigerator.query.get_or_404(refrigerator_id)
    refrigerator_obj = refrigerator_creator(get_refrigerator)
    refrigerator_obj.cleanup()
    for shelf in refrigerator_obj.shelves_list:
        for item in shelf.items_list:
            item.expiration_date = str(item.expiration_date)
    response = app.response_class(
        response=json.dumps(refrigerator_obj, default=lambda o: o.__dict__,
                            sort_keys=True, indent=4),
        status=200,
        mimetype='application/json'
    )
    return response


def place_left(get_refrigerator):
    refrigerator_obj = refrigerator_creator(get_refrigerator)
    json_dict = {
        'refrigerator model': refrigerator_obj.model,
        'refrigerator color': refrigerator_obj.color,
        'place left in the fridge': refrigerator_obj.place_left_in_the_fridge()
    }
    response = app.response_class(
        response=json.dumps(json_dict, default=lambda o: o.__dict__,
                            sort_keys=True, indent=4),
        status=200,
        mimetype='application/json'
    )
    return response


def whats_to_eat(get_refrigerator):
    refrigerator_obj = refrigerator_creator(get_refrigerator)
    list1 = refrigerator_obj.whats_to_eat('dairy', 'drink')
    for item in list1:
        item.expiration_date = str(item.expiration_date)
    response = app.response_class(
        response=json.dumps(list1, default=lambda o: o.__dict__,
                            sort_keys=True, indent=4),
        status=200,
        mimetype='application/json'
    )
    return response


@methods.route('/methods/shopping-ready/<int:refrigerator_id>')
def shopping_ready(refrigerator_id):
    get_refrigerator = Refrigerator.query.get_or_404(refrigerator_id)
    refrigerator_obj = refrigerator_creator(get_refrigerator)
    refrigerator_obj.getting_shopping_ready()
    for shelf in refrigerator_obj.shelves_list:
        for item in shelf.items_list:
            item.expiration_date = str(item.expiration_date)
    response = app.response_class(
        response=json.dumps(refrigerator_obj, default=lambda o: o.__dict__,
                            sort_keys=True, indent=4),
        status=200,
        mimetype='application/json'
    )
    return response


def refrigerator_creator(get_refrigerator):
    from .refrigerator.refrigerator_obj import RefrigeratorObj
    shelves_list = []
    for shelf in get_refrigerator.shelves_list:
        shelves_list.append(shelf_creator(shelf))
    return RefrigeratorObj(get_refrigerator.model, get_refrigerator.color, shelves_list)


def shelf_creator(get_shelf):
    from .shelf.shelf_obj import ShelfObj
    items = []
    for item in get_shelf.items_list:
        items.append(item_creator(item, get_shelf.level_number))
    return ShelfObj(get_shelf.level_number, get_shelf.place_size, items)


def item_creator(get_item, level_number):
    from .item.item_obj import ItemObj
    return ItemObj(get_item.name, level_number, get_item.type_category,
                             get_item.kosher_category, get_item.expiration_date, get_item.place_taken)
