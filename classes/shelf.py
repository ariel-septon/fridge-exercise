from helpers import functions


class Shelf:
    def __init__(self, level_number, place_size, place_left, items_list):
        self.id = functions.id_number_generator(self)
        self.level_number = level_number
        self.place_size = place_size
        self.place_left = place_left
        self.items_list = items_list

    def __eq__(self, other):
        if not isinstance(other, Shelf):
            return False

        return other.level_number == self.level_number and other.place_size == self.place_size and \
               other.place_left == self.place_left and other.items_list == self.items_list
