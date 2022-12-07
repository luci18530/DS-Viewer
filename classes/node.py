class Node(object):
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert(self, data):
        ''' For inserting the node '''
        if self.data == data:
            return False
        
        elif data < self.data:
            if self.left_child:
                return self.left_child.insert(data)
            else:
                self.left_child = Node(data)
                return True

        else:
            if self.right_child:
                return self.right_child.insert(data)
            else:
                self.right_child = Node(data)
                return True 


    def delete(self, data,root):
        ''' For deleting the node '''
        if self is None:
            return None

        # if current node's data is less than that of root node, then only search in left subtree else right subtree
        if data < self.data:
            self.left_child = self.left_child.delete(data,root)
        elif data > self.data:
            self.right_child = self.right_child.delete(data,root)
        else:
            # deleting node with one child
            if self.left_child is None:

                if self == root:
                    temp = self.min_value_node(self.right_child)
                    self.data = temp.data
                    self.right_child = self.right_child.delete(temp.data,root) 

                temp = self.right_child
                self = None
                return temp
            elif self.right_child is None:

                if self == root:
                    temp = self.max_value_node(self.left_child)
                    self.data = temp.data
                    self.left_child = self.left_child.delete(temp.data,root) 

                temp = self.left_child
                self = None
                return temp

            # deleting node with two children
            # first get the inorder successor
            temp = self.min_value_node(self.right_child)
            self.data = temp.data
            self.right_child = self.right_child.delete(temp.data,root)

        return self

    def find(self, data):
        ''' This function checks whether the specified data is in tree or not '''
        if(data == self.data):
            return True
        elif(data < self.data):
            if self.left_child:
                return self.left_child.find(data)
            else:
                return False
        else:
            if self.right_child:
                return self.right_child.find(data)
            else:
                return False

    def preorder(self):
        '''For preorder traversal of the BST '''
        if self:
            print(str(self.data), end = ' ')
            if self.left_child:
                self.left_child.preorder()
            if self.right_child:
                self.right_child.preorder()

    def inorder(self):
        ''' For Inorder traversal of the BST '''
        if self:
            if self.left_child:
                self.left_child.inorder()
            print(str(self.data), end = ' ')
            if self.right_child:
                self.right_child.inorder()


    def postorder(self):
        ''' For postorder traversal of the BST '''
        if self:
            if self.left_child:
                self.left_child.postorder()
            if self.right_child:
                self.right_child.postorder()
            print(str(self.data), end = ' ')

    def size(self):
        ''' For finding the size of the BST '''
        if self is None:
            return 0
        else:
            return self.left_child.size() + 1 + self.right_child.size()

    # print the tree in terminal, using levels, lines and branches
    def imprimir_arvore(self, nivel=0):
        if self.right_child:
            self.right_child.imprimir_arvore(nivel+1)
            print('\t' * nivel, '    /')
        print('\t' * nivel, self.data)
        if self.left_child:
            print('\t' * nivel, '    \\')
            self.left_child.imprimir_arvore(nivel+1)


    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return str(self.data)