class LinkedList:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def add(self, item):
        self.items.append(item)

    # def remove, if value is not in the list, do nothing
    def remove(self, item):
        if item in self.items:
            self.items.remove(item)

    def search(self, item):
        return item in self.items

    def index(self, item):
        return self.items.index(item)

    def pop(self, pos):
        return self.items.pop(pos)

    def insert(self, pos, item):
        self.items.insert(pos, item)

    def __str__(self):
        return str(self.items)
    
    def __repr__(self):
        return str(self.items)
    # get a value from the list by index
    def get(self, index):        
        return self.items[index]