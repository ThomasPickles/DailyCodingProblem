class FixedLengthQueue:
    """Keep last N entities"""

    def __init__(self, N):
        self._length = N
        self._items = [None] * N
        self._index = 0

    def record(self, id):
        self._items[self._index] = id
        self._index = (self._index + 1) % self._length

    def get_last(self, i):
        index = (self._index-i) % self._length
        return self._items[index]


orders = FixedLengthQueue(3)
orders.record(3)
orders.record(4)
orders.record(5)
orders.record(6)
orders.record(7)
orders.record(8)
orders.get_last(2) # should be 7