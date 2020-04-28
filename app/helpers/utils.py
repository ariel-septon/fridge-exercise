from datetime import *
from app.classes.item.item import Item
from app.classes.shelf.shelf import Shelf

global_id = 0


def id_number_generator() -> int:
    global global_id
    global_id += 1
    return global_id


def is_expired(item: Item) -> bool:
    return is_expired_in_less_than_x_days(item, 0)


def is_expired_in_less_than_x_days(item: Item, number_of_days) -> bool:
    today = date.today()
    delta = item.expiration_date - today
    if delta.days < number_of_days:
        return True
    return False


def item_by_id(shelves_list, id_number) -> Item:
    for shelf in shelves_list:
        for item in shelf.items_list:
            if item.id == id_number:
                return item
    raise ValueError('The item is not currently in the refrigerator')


def is_item_fits_categories(item: Item, kosher_category, type_category) -> bool:
    return item.kosher_category == kosher_category and \
           item.type_category == type_category and \
           not is_expired(item)


def get_shelf_by_id(self, id_number) -> Shelf:
    shelf = next((shelf for shelf in self.shelves_list if shelf.id == id_number), None)
    if shelf is not None:
        return shelf
    raise ValueError('The shelf is not currently in the refrigerator')


def remove_items_due_specific_expiration_date_and_kosher_category(self, number_of_days: int,
                                                                  kosher_category: str, save_items: {}) -> None:
    for shelf in self.shelves_list:
        for item in shelf.items_list:
            if is_expired_in_less_than_x_days(item, number_of_days) \
                    and item.kosher_category == kosher_category:
                print('removing the', item.name, 'that expires in', item.expiration_date)
                save_items.setdefault(shelf.id, [])
                save_items[shelf.id].append(item)
                self.take_out_an_item(item.id)


def insert_the_fresh_items_back_to_fridge(self, save_items: dict) -> None:
    for shelf_id, items in save_items.items():
        shelf = get_shelf_by_id(self, shelf_id)
        for item in items:
            self.add_an_item(shelf, item)
    print('This is not the time to do shopping')
    print('all the items who have not expired are back to the fridge')
