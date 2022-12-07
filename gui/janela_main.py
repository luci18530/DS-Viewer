import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import sys

from classes.linked_list import LinkedList
from classes.queue import Queue
from classes.stack import Stack
from classes.binary_tree import Tree

from .janela_lista import janela_lista
from .janela_fila import janela_fila
from .janela_pilha import janela_pilha
from .janela_arvore import janela_arvore

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

lista = LinkedList()
fila = Queue()
pilha = Stack()
arvore = Tree()

lista_da_arvore = []
tamanho_maximo_da_pilha = 19

class janela_main(QMainWindow):
    def __init__(self):
        super().__init__()
        # set background color to black
        self.setStyleSheet("background-color: #121212;")
        self.left = 10
        self.top = 30
        self.width = 1050
        self.height = 700
        self.title = 'Estrutura de Dados'
        exit_button = QPushButton('SAIR', self)
        exit_button.move(450, 380)
        exit_button.resize(150, 50)
        exit_button.setStyleSheet("background-color: red; color: white; font-weight: bold; font-size: 15px; font-family: Lucida Sans Unicode")
        exit_button.clicked.connect(self.close)

        self.computer_img()
        self.label_one()
        self.lista()
        self.pilha()
        self.fila()
        self.arvore()      
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def label_one(self):
        label_one = QLabel('Data Structure Viewer', self)
        # move to the center top of the window
        label_one.setAlignment(Qt.AlignCenter)
        #label_one.move(100, 10)
        label_one.resize(1050, 50)
        label_one.setStyleSheet("background-color: #121212; color: white; font-weight: bold; font-size: 32px; font-family: Lucida Sans Unicode; font-style: italic")
        label_one.show()

    def computer_img(self):
        img_comp = QPixmap('./assets/computer.png')
        computer_image = QLabel(self)
        computer_image.setPixmap(img_comp)
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.3)
        computer_image.setGraphicsEffect(self.opacity_effect)
        computer_image.resize(128,128)
        computer_image.move(900,550)
        computer_image.show()

    def lista(self):
        lista_button = QPushButton('Lista Encadeada', self)
        
        lista_button.move(375, 140)
        lista_button.resize(300, 50)
        lista_button.setStyleSheet("background-color: blue; color: white; font-weight: bold; font-size: 15px; font-family: Lucida Sans Unicode")
        lista_button.clicked.connect(self.listaclick)

    def listaclick(self):
        print('Lista Encadeada')
        self.lista = janela_lista()

    def pilha(self):
        pilha_button = QPushButton('Pilha', self)
        pilha_button.move(375, 200)
        pilha_button.resize(300, 50)
        pilha_button.setStyleSheet("background-color: blue; color: white; font-weight: bold; font-size: 15px; font-family: Lucida Sans Unicode")
        pilha_button.clicked.connect(self.pilhaclick)
    
    def pilhaclick(self):
        print('Pilha')
        self.pilha = janela_pilha()

    def fila(self):
        fila_button = QPushButton('Fila', self)
        fila_button.move(375, 260)
        fila_button.resize(300, 50)
        fila_button.setStyleSheet("background-color: blue; color: white; font-weight: bold; font-size: 15px; font-family: Lucida Sans Unicode")
        fila_button.clicked.connect(self.filaclick)

    def filaclick(self):
        print('Fila')
        print(self.objectName())
        self.fila = janela_fila()

    def arvore(self):
        arvore_button = QPushButton('Arvore', self)
        arvore_button.move(375, 320)
        arvore_button.resize(300, 50)
        arvore_button.setStyleSheet("background-color: blue; color: white; font-weight: bold; font-size: 15px; font-family: Lucida Sans Unicode")
        arvore_button.clicked.connect(self.arvoreclick)
    
    def arvoreclick(self):
        self.arvore = janela_arvore()
        print('Arvore')