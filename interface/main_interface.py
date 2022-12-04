import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

from utils import *
from linkedlist_interface import janelalista
from queue_interface import janelafila
import sys

class janelamain(QMainWindow):
    def __init__(self):
        super().__init__()
        # set background color to black
        self.setStyleSheet("background-color: black;")
        self.left = 10
        self.top = 30
        self.width = 1050
        self.height = 700
        self.title = 'Estrutura de Dados'
        exit_button = QPushButton('SAIR', self)
        exit_button.move(1000, 660)
        exit_button.resize(50, 40)
        exit_button.setStyleSheet("background-color: red; color: white; font-weight: bold; font-size: 15px; font-family: Lucida Sans Unicode")
        exit_button.clicked.connect(self.close)

        self.label1()
        self.lista()
        self.pilha()
        self.fila()
        self.arvore()      
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def label1(self):
        label1 = QLabel('Visualizador de Estrutura de Dados', self)
        # move to the center top of the window
        label1.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        label1.resize(600, 40)
        label1.setStyleSheet("background-color: black; color: white; font-weight: bold; font-size: 32px; font-family: Lucida Sans Unicode; font-style: italic")
        label1.show()

    def lista(self):
        lista_button = QPushButton('Lista Encadeada', self)
        lista_button.move(10, 60)
        lista_button.resize(200, 40)
        lista_button.setStyleSheet("background-color: blue; color: white; font-weight: bold; font-size: 15px; font-family: Lucida Sans Unicode")
        lista_button.clicked.connect(self.listaclick)

    def listaclick(self):
        print('Lista Encadeada')
        self.lista = janelalista()

    def pilha(self):
        pilha_button = QPushButton('Pilha', self)
        pilha_button.move(10, 110)
        pilha_button.resize(200, 40)
        pilha_button.setStyleSheet("background-color: blue; color: white; font-weight: bold; font-size: 15px; font-family: Lucida Sans Unicode")
        pilha_button.clicked.connect(self.pilhaclick)
    
    def pilhaclick(self):
        print('Pilha')

    def fila(self):
        fila_button = QPushButton('Fila', self)
        fila_button.move(10, 160)
        fila_button.resize(200, 40)
        fila_button.setStyleSheet("background-color: blue; color: white; font-weight: bold; font-size: 15px; font-family: Lucida Sans Unicode")
        fila_button.clicked.connect(self.filaclick)

    def filaclick(self):
        print('Fila')
        print(self.objectName())
        self.fila = janelafila()

    def arvore(self):
        arvore_button = QPushButton('Arvore', self)
        arvore_button.move(10, 210)
        arvore_button.resize(200, 40)
        arvore_button.setStyleSheet("background-color: blue; color: white; font-weight: bold; font-size: 15px; font-family: Lucida Sans Unicode")
        arvore_button.clicked.connect(self.arvoreclick)
    
    def arvoreclick(self):
        print('Arvore')