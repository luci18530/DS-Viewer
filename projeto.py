# A program to create visualizations of the data structures (linked lists, sequential lists, stacks, queues, binary search trees) 
import sys
import os
import time
import random
import pygame


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)

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

    def remove(self, item):
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
    
    
# FILAS | QUEUES
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

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
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)
    
    def __repr__(self):
        return str(self.items)

# ARVORE BINARIA DE BUSCA | BINARY SEARCH TREE
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

# FUNCOES AUXILIARES | AUXILIARY FUNCTIONS
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def draw_button(text, font, color, surface, x, y, width, height):
    pygame.draw.rect(surface, color, (x, y, width, height))
    draw_text(text, font, BLACK, surface, x + 10, y + 10)

# TEST BINARY SEARCH TREE
def test_binary_search_tree():
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    # insert more
    root.insert(9)
    root.insert(13)
    root.insert(15)
    root.insert(1)
    root.insert(5)
    print(root.findval(7))
    print(root.findval(14))
    root.print_tree()

test_binary_search_tree()

# BUTTON WITH IMAGE
class Button:
    def __init__(self, image, x, y, width, height):
        self.image = image
        self.rect = image.get_rect()
        self.rect.topleft = (x, y)
        self.width = width
        self.height = height

    def draw(self, surface):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True

        # draw button
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action






# Create a 1200x1200 sized screen
pygame.init()
running = True
altura = 720
largura = 1280
screen = pygame.display.set_mode((largura, altura))
# load button sair.png
button_sair = pygame.image.load('button_sair.png').convert_alpha()
button_teste = pygame.image.load('button_teste.png').convert_alpha()
pygame.display.set_caption('Projeto de Estrutura de Dados')
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #screen.fill(BLACK)
    pygame.display.flip()
    # draw button sair.png using the Button class
    if Button(button_sair, largura-200, altura-200, 100, 50).draw(screen):
        running = False
    if Button(button_teste, largura-200, altura-300, 100, 50).draw(screen):
        print('testei')

    
    pygame.display.update()
    
