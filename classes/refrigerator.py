from helpers import functions
from classes.shelf import Shelf
from classes.item import Item


class Refrigerator:
    def __init__(self, model, color, shelves_list: [Shelf]):
        self.id = functions.id_number_generator(self)
        self.model = model
        self.color = color
        self.shelves_list = shelves_list
        self.shelf_amount = len(self.shelves_list)

    def __eq__(self, other):
        if not isinstance(other, Refrigerator):
            return False

        return other.model == self.model and other.color == self.color and \
               other.shelf_amount == self.shelf_amount and other.shelves_list == self.shelves_list

    def place_left_in_the_fridge(self) -> int:
        place_left = 0
        for i in range(self.shelf_amount):
            if isinstance(self.shelves_list[i], Shelf):
                place_left += self.shelves_list[i].place_left

        return place_left

    def add_a_shelf(self, shelf: Shelf):
        self.shelves_list.append(shelf)

    def add_an_item(self, shelf: Shelf, item: Item) -> bool:
        for i in enumerate(self.shelves_list):
            if shelf.__eq__(self.shelves_list[i]):
                if self.shelves_list[i].place_left >= item.place_taken:
                    self.shelves_list[i].items_list.append(item)
                    item.shelf_located = self.shelves_list[i]
                    return True

        return False
