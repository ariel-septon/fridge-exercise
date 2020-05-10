from app.helpers.utils import id_number_generator


class ShelfObj:
    def __init__(self, level_number, place_size, items_list):
        self.id = id_number_generator()
        self.level_number = level_number
        self.place_size = place_size
        self.items_list = items_list
        self.place_left = place_size - sum(item.place_taken for item in self.items_list)
