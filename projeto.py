# A program to create visualizations of the data structures (linked lists, sequential lists, stacks, queues, binary search trees) 
# PROJETO DE ESTRUTURA DE DADOS
# Grupo: Guilherme Nogueira, Luciano Pereira, Pedro Lucas, Thais Melquiades, Vitoria Grisi
import pygame
import sys


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
        # resize image according to width and height and resize the area of collision
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = pygame.Rect(x, y, self.width, self.height)


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

    def checkinput(self, event):
        action = False

        # check mouseover and clicked conditions
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                action = True

        return action


def getfont(fontname, size):
    return pygame.font.SysFont(fontname, size)

# examples of fonts
# font = getfont('arial', 20)
# font = getfont('comicsansms', 20)
# font = getfont('courier', 20)


# Create a 1200x1200 sized screen
pygame.init()
running = True
altura = 720
largura = 1280
SCREEN = pygame.display.set_mode((largura, altura))
# load the buttons images 
button_sair = pygame.image.load('button_sair.png').convert_alpha()
button_teste = pygame.image.load('button_teste.png').convert_alpha()
button_lista = pygame.image.load('button_lista.png').convert_alpha()
button_fila = pygame.image.load('button_fila.png').convert_alpha()
button_pilha = pygame.image.load('button_pilha.png').convert_alpha()
button_arvore = pygame.image.load('button_arvore.png').convert_alpha()
pygame.display.set_caption('Projeto de Estrutura de Dados - MENU')

def listamenu():
    # Create a 1200x1200 sized screen
    pygame.init()
    running = True
    altura = 720
    largura = 1280
    lista = []
    texto = ''
    SCREEN = pygame.display.set_mode((largura, altura))
    # load the buttons images 
    button_sair = pygame.image.load('button_sair.png').convert_alpha()
    button_teste = pygame.image.load('button_teste.png').convert_alpha()
    pygame.display.set_caption('Projeto de Estrutura de Dados - LISTA')

    # create the buttons
    button1 = Button(button_teste, 100, 100, 200, 50)
    button2 = Button(button_sair, 1000, 600, 135, 60)

    # create the font
    font = getfont('arial', 20)
    SCREEN.fill(BLACK)

    # main loop
    while running:

        
        

        # draw the buttons
        button1.draw(SCREEN)
        button2.draw(SCREEN)
        
        draw_text('Digite o valor a ser inserido:', font, WHITE, SCREEN, 100, 300)
        # set a rectangle of lines to write the text
        inseridor = pygame.draw.rect(SCREEN, WHITE, (100, 350, 100, 30), 2)
        
        # type in the box
        



        


        # check events
        for event in pygame.event.get():
            # check if the event is the X button
            if event.type == pygame.QUIT:
                # if it is quit the game
                pygame.quit()
                sys.exit()
            # check if the event is a mouse button down
            if event.type == pygame.MOUSEBUTTONDOWN:
                # check if the mouse is over the button
                if button1.checkinput(event):
                    print('Button 1 was pressed')
                if button2.checkinput(event):
                    print('Button 2 was pressed')
                    running = False
                if inseridor.collidepoint(event.pos):
                    texto = ''
                    active = True

            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_RETURN:
                        texto = ''
                    elif event.key == pygame.K_BACKSPACE:
                        texto = texto[:-1]
                        clear_rect = pygame.draw.rect(SCREEN, BLACK, (100, 350, 100, 30))
                    #delete key
                    elif event.key == pygame.K_DELETE:
                        texto = ''
                        clear_rect = pygame.draw.rect(SCREEN, BLACK, (100, 350, 100, 30))                        
                    else:
                        texto += event.unicode
            # Render the current text
            txt_surface = font.render(texto, True, WHITE)
            # Resize the box if the text is too long
            width = max(200, txt_surface.get_width()+10)
            inseridor.w = width
            # Blit the text.
            SCREEN.blit(txt_surface, (inseridor.x+5, inseridor.y+5))
            pygame.display.flip()
            clock.tick(60)

            
            
                        

        # update the screen
        pygame.display.update()

def mainmenu():
    while running:
        
        SCREEN.fill((0, 0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = getfont('comicsansms', 50)
        draw_text('MENU', MENU_TEXT, WHITE, SCREEN, 550, 50)

        LISTA_BUTTON = Button(button_lista, 100, 100, 200, 70)
        FILA_BUTTON = Button(button_fila, 400, 100, 200, 70)
        PILHA_BUTTON = Button(button_pilha, 700, 100, 200, 70)
        ARVORE_BUTTON = Button(button_arvore, 1000, 100, 200, 70)
        SAIR_BUTTON = Button(button_sair, 1000, 500, 135, 60)

        SCREEN.blit(button_lista, (100, 100))
        SCREEN.blit(button_fila, (400, 100))
        SCREEN.blit(button_pilha, (700, 100))
        SCREEN.blit(button_arvore, (1000, 100))
        SCREEN.blit(button_sair, (1000, 500))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SAIR_BUTTON.checkinput(event):
                    pygame.quit()
                    sys.exit()
                if LISTA_BUTTON.checkinput(event):
                    listamenu()
                if PILHA_BUTTON.checkinput(event):
                    pilhamenu()
                if FILA_BUTTON.checkinput(event):
                    filamenu()
                if ARVORE_BUTTON.checkinput(event):
                    arvoremenu()

        pygame.display.update()
        
clock = pygame.time.Clock()
mainmenu()