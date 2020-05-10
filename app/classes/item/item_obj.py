from app.helpers.utils import id_number_generator


class ItemObj:
    def __init__(self, name, shelf_located, type_category, kosher_category,
                 expiration_date, place_taken):
        self.id = id_number_generator()
        self.name = name
        self.shelf_located = shelf_located
        self.type_category = type_category
        self.kosher_category = kosher_category
        self.expiration_date = expiration_date
        self.place_taken = place_taken
