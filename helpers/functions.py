from datetime import *
from classes.item import Item


def id_number_generator(obj):
    return id(obj)


def is_expired(item: Item) -> bool:
    today = date.today()
    if item.expiration_date > today:
        return True
    return False
