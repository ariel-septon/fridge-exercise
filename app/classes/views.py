from flask import render_template, make_response, jsonify

from run import app
from . import methods
from flask import json
from .forms import CompareRefrigerators, CompareShelves, CompareItems, \
    ChooseRefrigerator, ChooseRefrigerator1, ChooseRefrigerator2, \
    RemoveItemFromRefrigerator, AddAnItemToRefrigerator


@methods.route('/methods', methods=['GET', 'POST'])
def list_methods():
    return render_template('list_pages/methods.html', template=True)


@methods.route('/methods/compare', methods=['GET', 'POST'])
def compare_methods():
    refrigerator_form = CompareRefrigerators()
    if refrigerator_form.validate_on_submit():
        return compare_refrigerators(refrigerator_form)
    shelf_form = CompareShelves()
    if shelf_form.validate_on_submit():
        return compare_shelves(shelf_form)
    item_form = CompareItems()
    if item_form.validate_on_submit():
        return compare_items(item_form)
    return render_template('list_pages/compare_methods.html', template=True, refrigerator_form=refrigerator_form,
                           shelf_form=shelf_form, item_form=item_form)


@methods.route('/methods/objects', methods=['GET', 'POST'])
def objects_methods():
    add_item_form = AddAnItemToRefrigerator()
    if add_item_form.validate_on_submit():
        return add_item_to_refrigerator(add_item_form.refrigerator.data, add_item_form.item.data)
    take_item_out_form = RemoveItemFromRefrigerator()
    if take_item_out_form.validate_on_submit():
        return take_item_out(take_item_out_form.refrigerator__.data, take_item_out_form.item__.data)
    return render_template('list_pages/objects_methods.html', template=True, add_item=add_item_form,
                           take_out=take_item_out_form)


@methods.route('/methods/refrigerator-methods', methods=['GET', 'POST'])
def refrigerator_methods():
    cleanup_form = ChooseRefrigerator()
    if cleanup_form.validate_on_submit():
        return cleanup_refrigerator(cleanup_form.refrigerator.data)
    whats_to_eat_form = ChooseRefrigerator1()
    if whats_to_eat_form.validate_on_submit():
        return whats_to_eat(whats_to_eat_form)
    getting_ready_form = ChooseRefrigerator2()
    if getting_ready_form.validate_on_submit():
        return shopping_ready(getting_ready_form.refrigerator2.data)
    return render_template('list_pages/refrigerator_methods.html',
                           cleanup=cleanup_form,
                           more=whats_to_eat_form,
                           last=getting_ready_form)


def take_item_out(get_refrigerator, get_item):
    get_refrigerator.take_out_an_item(get_item.id)
    return jsonify_refrigerator(get_refrigerator)


def add_item_to_refrigerator(get_refrigerator, get_item):
    if get_refrigerator.add_an_item(get_item):
        for shelf in get_refrigerator.shelves_list:
            for item in shelf.items_list:
                item.expiration_date = str(item.expiration_date)
        response = app.response_class(
            response=json.dumps(refrigerator_creator(get_refrigerator), default=lambda o: o.__dict__,
                                sort_keys=True, indent=4),
            status=200,
            mimetype='application/json'
        )

    else:
        response = make_response(jsonify('The selected refrigerator '
                                         'does not have enough space left'), 404)

    return response


def compare_shelves(form):
    response = app.response_class(
        response=json.dumps(form.shelf1.data.__eq__(form.shelf2.data), default=lambda o: o.__dict__,
                            sort_keys=True, indent=4),
        status=200,
        mimetype='application/json'
    )
    return response


def compare_refrigerators(form):
    print('in')
    response = app.response_class(
        response=json.dumps(form.refrigerator1.data.__eq__(form.refrigerator2.data), default=lambda o: o.__dict__,
                            sort_keys=True, indent=4),
        status=200,
        mimetype='application/json'
    )
    print('out')
    return response


def compare_items(form):
    response = app.response_class(
        response=json.dumps(form.item1.data.__eq__(form.item2.data), default=lambda o: o.__dict__,
                            sort_keys=True, indent=4),
        status=200,
        mimetype='application/json'
    )
    return response


def cleanup_refrigerator(get_refrigerator):
    get_refrigerator.cleanup()
    return jsonify_refrigerator(get_refrigerator)


def place_left(get_refrigerator):
    json_dict = {
        'refrigerator model': get_refrigerator.model,
        'refrigerator color': get_refrigerator.color,
        'place left in the fridge': get_refrigerator.place_left_in_the_fridge()
    }
    response = app.response_class(
        response=json.dumps(json_dict, default=lambda o: o.__dict__,
                            sort_keys=True, indent=4),
        status=200,
        mimetype='application/json'
    )
    return response


def whats_to_eat(form):
    refrigerator = form.refrigerator1.data
    list1 = refrigerator.whats_to_eat(form.kosher_category.data, form.type_category.data)
    for item in list1:
        item.expiration_date = str(item.expiration_date)
    if len(list1) != 0:
        response = app.response_class(
            response=json.dumps(list1, default=lambda o: o.__dict__,
                                sort_keys=True, indent=4),
            status=200,
            mimetype='application/json'
        )
    else:
        response = make_response(jsonify('The selected refrigerator '
                                         'does not contain an item that'
                                         ' matches the selected categories'), 404)

    return response


def shopping_ready(get_refrigerator):
    get_refrigerator.getting_shopping_ready()
    return jsonify_refrigerator(get_refrigerator)


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


def jsonify_refrigerator(get_refrigerator):
    for shelf in get_refrigerator.shelves_list:
        for item in shelf.items_list:
            item.expiration_date = str(item.expiration_date)
    response = app.response_class(
        response=json.dumps(refrigerator_creator(get_refrigerator), default=lambda o: o.__dict__,
                            sort_keys=True, indent=4),
        status=200,
        mimetype='application/json'
    )
    return response
