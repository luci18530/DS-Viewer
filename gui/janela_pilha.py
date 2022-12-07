import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from classes.stack import Stack
import sys

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

pilha = Stack()

lista_da_arvore = []
tamanho_maximo_da_pilha = 19

class janela_pilha(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setStyleSheet("background-color: #121212;")
        label_pilha = QLabel(self)
        label_pilha.setText("Pilha")
        label_pilha.setStyleSheet("color: white; font-size: 30px; font-weight: bold;")
        label_pilha.move(10, 10)

        stack_image = QLabel(self)
        stack_image.setPixmap(QPixmap("assets/stack.png"))
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.3)
        stack_image.setGraphicsEffect(self.opacity_effect)
        stack_image.move(900, 550)
        stack_image.show()

        label_topo_pilha = QLabel(self)
        label_topo_pilha.setText("Topo da pilha")
        label_topo_pilha.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        label_topo_pilha.move(200, 130)

        label_empilhar = QLabel(self)
        label_empilhar.setText("Empilhar elemento")
        label_empilhar.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        label_empilhar.move(20, 60)

        self.input_pilha()

        button_empilhar = QPushButton('Empilhar', self)
        button_empilhar.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
        button_empilhar.move(330, 90)
        button_empilhar.resize(100, 30)
        button_empilhar.clicked.connect(self.button_empilhar_clicked)

        button_desempilhar = QPushButton('Desempilhar', self)
        button_desempilhar.setStyleSheet("background-color: red; color: white; font-size: 15px; font-weight: bold;")
        button_desempilhar.move(440, 90)
        button_desempilhar.resize(100, 30)
        button_desempilhar.clicked.connect(self.button_desempilhar_clicked)

        self.init_UI()

    def init_UI(self):
        self.setGeometry(10, 30, 1050, 700)
        self.setWindowTitle('Pilha')
        self.show() 

    def input_pilha(self):
        entrada_pilha = QLineEdit(self)
        entrada_pilha.move(20, 90)
        entrada_pilha.resize(300, 30)
        entrada_pilha.setObjectName("entrada_pilha")
        entrada_pilha.setStyleSheet("color: white;")
        entrada_pilha.setPlaceholderText("Digite o valor")

    def button_empilhar_clicked(self):
        entrada_pilha = self.findChild(QLineEdit, "entrada_pilha")
        valor = entrada_pilha.text()

        if valor == "":
            return

        # if the stack is full (size == tamanho_maximo_da_pilha) return
        if pilha.size() == tamanho_maximo_da_pilha:
            return

        pilha.push(valor)
        top_of_pilha = pilha.top()
        print(pilha)

        for i in range(pilha.size()):
            button_pilha = QPushButton(str(pilha.get(i)), self)
            button_pilha.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
            button_pilha.move(20, 650 - (i * 30))
            button_pilha.resize(60, 30)
            button_pilha.show()

        button_topo = QPushButton(str(top_of_pilha), self)
        button_topo.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
        button_topo.move(235, 180)
        button_topo.resize(60, 30)
        button_topo.show()

    def image_black_bmp(self):
        imageblack = QLabel(self)
        imageblack.setPixmap(QPixmap("black.png"))
        imageblack.move(10, 200)
        imageblack.resize(600, 600)
        imageblack.show()

    def button_desempilhar_clicked(self):
        pilha.pop()
        print(pilha)
        top_of_pilha = pilha.top()
        self.image_black_bmp()
        for i in range(pilha.size()):
            button_pilha = QPushButton(str(pilha.get(i)), self)
            button_pilha.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
            button_pilha.move(20, 650 - (i * 30))
            button_pilha.resize(60, 30)
            button_pilha.show()

        button_topo = QPushButton(str(top_of_pilha), self)
        button_topo.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
        button_topo.move(235, 180)
        button_topo.resize(60, 30)
        button_topo.show()