import datetime
from classes.shelf import Shelf
from classes.item import Item
from classes.refrigerator import Refrigerator


item1 = Item('cheese', 0, 'food', 'milk', datetime.datetime(2018, 5, 3), 5)
item2 = Item('steak', 0, 'food', 'meat', datetime.datetime(2018, 6, 3), 5)
itemsShelf0 = [item1, item2]
item3 = Item('steak', 1, 'food', 'meat', datetime.datetime(2055, 6, 3), 5)
itemsShelf1 = [item3]
shelf0 = Shelf(0, 20, 10, itemsShelf0)
shelf1 = Shelf(0, 20, 15, itemsShelf1)
shelves = [shelf0, shelf1]
fridge = Refrigerator('tt', 'tt', shelves)


class Obj:
    def __init__(self, number):
        self.num = number

    def append_(self) -> int:
        return self.num


obj1 = Obj(0)
obj2 = Obj(1)
obj3 = Obj(2)
obj4 = Obj(3)

objects = [obj1, obj2, obj3, obj4]
for y in range(len(objects)):
    print(objects[y].num)

objects.sort(key=lambda x: x.append_(), reverse=True)
for c in range(len(objects)):
    print(objects[c].num)
