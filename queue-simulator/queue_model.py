class Queue:
    def __init__(self, items=None):
        self._items = list(items) if items else []

    def enqueue(self, value):
        self._items.append(value)          # rear = dulo ng list

    def dequeue(self):
        return self._items.pop(0) if self._items else None   # front = index 0

    def peek(self):
        return self._items[0] if self._items else None

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def clear(self):
        self._items.clear()

    def to_list(self):
        return list(self._items)