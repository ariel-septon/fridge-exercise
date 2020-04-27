from app.classes.refrigerator import Refrigerator


class Refrigerators:
    def __init__(self):
        self.refrigerators_list = []

    def add_a_fridge(self, fridge: Refrigerator):
        self.refrigerators_list.append(fridge)

    def sort_refrigerators_by_space_left(self) -> list:
        self.refrigerators_list.sort(key=lambda x: x.place_left_in_the_fridge(), reverse=True)
        return self.refrigerators_list
