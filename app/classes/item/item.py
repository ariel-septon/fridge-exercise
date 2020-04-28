from app.helpers.utils import id_number_generator


class Item:
    def __init__(self, name, shelf_located, type_category, kosher_category,
                 expiration_date, place_taken):
        self.id = id_number_generator()
        self.name = name
        self.shelf_located = shelf_located
        self.type_category = type_category
        self.kosher_category = kosher_category
        self.expiration_date = expiration_date
        self.place_taken = place_taken

    def __eq__(self, other) -> bool:
        if not isinstance(other, Item):
            return False
        return other.name == self.name and \
               other.shelf_located == self.shelf_located and \
               other.type_category == self.type_category and \
               other.kosher_category == self.kosher_category and \
               other.expiration_date == self.expiration_date and \
               other.place_taken == self.place_taken
