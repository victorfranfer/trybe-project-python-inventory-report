from typing import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.current_page = 0

    def __next__(self):
        try:
            list = self.data[self.current_page]
        except IndexError:
            raise StopIteration()
        else:
            self.current_page += 1
            return list
