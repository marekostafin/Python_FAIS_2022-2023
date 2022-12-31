import random

class RandomQueue:
    """Implementacja kolejki, z której elementy pobierane są w losowej kolejności"""
    def __init__(self, size=16):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.head = 0           # pierwszy do pobrania
        self.tail = 0           # pierwsze wolne

    def insert(self, item):    # wstawia element w czasie O(1)
        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self.n

    def remove(self):    # zwraca losowy element w czasie O(1)
        index = random.randint(self.head, self.tail-1)
        item = self.items[index]
        self.items[index] = self.items[self.head]
        self.head = (self.head + 1) % self.n
        return item

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.tail + 1) % self.n == self.head

    def clear(self):    # czyszczenie listy
        self.head = 0
        self.tail = 0