class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update

class MappingSubclass(Mapping):

    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)

    def print_something(self):
        print("Print something")

    __update = print_something

# python3 -i mapping.py
# Mapping.__update -fails
# dir(Mapping)
# dir(MappingSubclass)
