from .node import Node

class Tree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def sort (self):
        if self.root is None:
            return []
        else:
            return self.root.recursive_sort([])

    def imprimir_arvore(self):
        if self.root is not None:
            self.root.imprimir_arvore()

    def insert(self, data):
        if self.root:
            self.size = self.size + 1
            return self.root.insert(data)
        else:
            self.root = Node(data)
            self.size = self.size + 1
            return True

    def delete(self, data):
        if self.root is not None:
            return self.root.delete(data,self.root)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        if self.root is not None:
            print()
            print('Preorder: ')
            self.root.preorder()

    def inorder(self):
        print()
        if self.root is not None:
            print('Inorder: ')
            self.root.inorder()

    def postorder(self):
        print()
        if self.root is not None:
            print('Postorder: ')
            self.root.postorder()

    def size (self):
        if self.root is not None:
            return self.root.size()

    def __str__(self):
        return str(self.root)

    def __repr__(self):
        return str(self.root)