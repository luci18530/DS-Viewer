# LISTA ENCADEADA | LINKED LIST (USING PYTHON BUILD-IN LIST)
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

    def searchandmatch(self, item):
        if item in self.items:
            return self.items.index(item)
        else:
            return -1
    
    
# FILAS | QUEUES
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        # if the queue is not empty, remove the first element
        if not self.isEmpty():
            return self.items.pop()

    def size(self):
        return len(self.items)

    def get(self, index):
        # if the queue is not empty, return the element at the index
        if not self.isEmpty():
            return self.items[index]

    def __str__(self):
        return str(self.items)
    
    def __repr__(self):
        return str(self.items)

# PILHAS | STACKS
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        # if the stack is not empty, remove the last element
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def top(self):
        if not self.isEmpty():
            return self.items[-1]

    def get(self, index):
        if not self.isEmpty():
            return self.items[index]
          

    def __str__(self):
        return str(self.items)
    
    def __repr__(self):
        return str(self.items)

# ARVORE BINARIA DE BUSCA | BINARY SEARCH TREE
class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        ''' For inserting the node '''
        if self.data == data:
            return False
        
        elif data < self.data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True

        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True 

    # PRINT THE TREE IN TERMINAL WITH LEVELS AND LINES
    def printTree(self, level=0):
        # no children
        if self.rightChild is None and self.leftChild is None:
            print('\t' * level, self.data)

        # only right child
        if self.rightChild is not None and self.leftChild is None:
            print('\t' * level, self.data)
            print('\t' * level, '    \\')
            self.rightChild.printTree(level+1)

        # only left child
        if self.rightChild is None and self.leftChild is not None:
            print('\t' * level, self.data)
            print('\t' * level, '    /')
            self.leftChild.printTree(level+1)

        # both children
        if self.rightChild and self.leftChild:
            self.rightChild.printTree(level+1)
            print('\t' * level, '    /')
            print('\t' * level, self.data)
            print('\t' * level, '    \\')   
            self.leftChild.printTree(level+1)

        

            

    def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current.leftChild is not None):
            current = current.leftChild

        return current

    def maxValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current.rightChild is not None):
            current = current.rightChild

        return current


    def delete(self, data,root):
        ''' For deleting the node '''
        if self is None:
            return None

        # if current node's data is less than that of root node, then only search in left subtree else right subtree
        if data < self.data:
            self.leftChild = self.leftChild.delete(data,root)
        elif data > self.data:
            self.rightChild = self.rightChild.delete(data,root)
        else:
            # deleting node with one child
            if self.leftChild is None:

                if self == root:
                    temp = self.minValueNode(self.rightChild)
                    self.data = temp.data
                    self.rightChild = self.rightChild.delete(temp.data,root) 

                temp = self.rightChild
                self = None
                return temp
            elif self.rightChild is None:

                if self == root:
                    temp = self.maxValueNode(self.leftChild)
                    self.data = temp.data
                    self.leftChild = self.leftChild.delete(temp.data,root) 

                temp = self.leftChild
                self = None
                return temp

            # deleting node with two children
            # first get the inorder successor
            temp = self.minValueNode(self.rightChild)
            self.data = temp.data
            self.rightChild = self.rightChild.delete(temp.data,root)

        return self

    def find(self, data):
        ''' This function checks whether the specified data is in tree or not '''
        if(data == self.data):
            return True
        elif(data < self.data):
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def preorder(self):
        '''For preorder traversal of the BST '''
        if self:
            print(str(self.data), end = ' ')
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def inorder(self):
        ''' For Inorder traversal of the BST '''
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.data), end = ' ')
            if self.rightChild:
                self.rightChild.inorder()


    def postorder(self):
        ''' For postorder traversal of the BST '''
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.data), end = ' ')

    def size(self):
        ''' For finding the size of the BST '''
        if self is None:
            return 0
        else:
            return self.leftChild.size() + 1 + self.rightChild.size()

    
    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return str(self.data)

    # print the tree in terminal, using levels, lines and branches
    def print_tree(self, level=0):
        if self.rightChild:
            self.rightChild.print_tree(level + 1)
        print(' ' * 4 * level + '->', self.data)
        if self.leftChild:
            self.leftChild.print_tree(level + 1)

    # PRINT THIS FUCKING TREE IN TERMINAL PLEASE 
    def imprimirarvore(self, nivel=0):
        if self.rightChild:
            self.rightChild.imprimirarvore(nivel+1)
            print('\t' * nivel, '    /')
        print('\t' * nivel, self.data)
        if self.leftChild:
            print('\t' * nivel, '    \\')
            self.leftChild.imprimirarvore(nivel+1)

        

class Tree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def sort (self):
        if self.root is None:
            return []
        else:
            return self.root.recursive_sort([])

    def imprimirarvore(self):
        if self.root is not None:
            self.root.imprimirarvore()

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

    def __str__(self):
        return str(self.root)

    def __repr__(self):
        return str(self.root)

    def size (self):
        if self.root is not None:
            return self.root.size()

    # print the tree in terminal, using levels, lines and branches
    def printtree(self):
        if self.root is not None:
            self.root.print_tree()     