class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            return str(self.data) + ' is found'

    

    # PRINT TREE WITH LINES
    def print_tree(self, level=0):
        if self.right:
            self.right.print_tree(level+1)
            print('\t' * level,'/', sep='')
        print('\t' * level, self.data)
        if self.left:
            print('\t' * level,'\\', sep='')
            self.left.print_tree(level+1)

    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return str(self.data)