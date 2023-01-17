import random

class RandomQueue:

    def __init__(self):
        self.items = []

    def insert(self, item):    # wstawia element w czasie O(1)
        self.items.append(item)

    def remove(self):    # zwraca losowy element w czasie O(1)
        if len(self.items) == 0:
            raise("The queue is empty")
        else:
            to_remove_index = random.randint(0, len(self.items) - 1)
            self.items[to_remove_index], self.items[len(self.items) - 1] = \
                self.items[len(self.items) - 1], self.items[to_remove_index]
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return False

    def clear(self):   # czyszczenie listy
        self.items.clear()