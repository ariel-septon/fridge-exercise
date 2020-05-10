from app.helpers.utils import id_number_generator
from app.classes.shelf.shelf_obj import ShelfObj


class RefrigeratorObj:
    def __init__(self, model, color, shelves_list: [ShelfObj]):
        self.id = id_number_generator()
        self.model = model
        self.color = color
        self.shelves_list = shelves_list
        self.shelf_amount = len(self.shelves_list)
