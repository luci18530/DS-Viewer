class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        # if the queue is not empty, remove the first element
        if not self.is_empty():
            return self.items.pop()

    def size(self):
        return len(self.items)

    def get(self, index):
        # if the queue is not empty, return the element at the index
        if not self.is_empty():
            return self.items[index]

    def __str__(self):
        return str(self.items)
    
    def __repr__(self):
        return str(self.items)