class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        # if the stack is not empty, remove the last element
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def top(self):
        if not self.is_empty():
            return self.items[-1]

    def get(self, index):
        if not self.is_empty():
            return self.items[index]
          

    def __str__(self):
        return str(self.items)
    
    def __repr__(self):
        return str(self.items)