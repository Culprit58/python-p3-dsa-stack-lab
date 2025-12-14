class Stack:

    def __init__(self, items=None, limit=100):
        self.limit = limit
        self.items = []

        if items:
            for item in items:
                if len(self.items) < self.limit:
                    self.items.append(item)

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if not self.full():
            self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        if target not in self.items:
            return -1
        # distance from top of stack
        return len(self.items) - 1 - self.items.index(target)
