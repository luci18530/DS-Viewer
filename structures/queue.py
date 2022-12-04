class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        # if the queue is not empty, remove the first element
        if not self.isEmpty():
            return self.items.pop()

    def size(self):
        return len(self.items)

    def get(self, index):
        return self.items[index]

    def __str__(self):
        return str(self.items)
    
    def __repr__(self):
        return str(self.items)