import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from classes.binary_tree import Tree
import sys

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

arvore = Tree()

lista_da_arvore = []
tamanho_maximo_da_pilha = 19

class janela_arvore(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setStyleSheet("background-color: black;")
        label_arvore = QLabel(self)
        label_arvore.setText("Árvore")
        label_arvore.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        label_arvore.move(10, 10)

        tree_image = QLabel(self)
        tree_image.setPixmap(QPixmap("assets/tree.png"))
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.3)
        tree_image.setGraphicsEffect(self.opacity_effect)
        tree_image.move(900, 550)
        tree_image.show()

        label_inserir = QLabel(self)
        label_inserir.setText("Inserir elemento")
        label_inserir.setStyleSheet("color: white; font-size: 15px; font-weight: bold;")
        label_inserir.move(10, 40)

        self.input_arvore()

        button_inserir = QPushButton('Inserir', self)
        button_inserir.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
        button_inserir.move(320, 50)
        button_inserir.resize(100, 30)
        button_inserir.clicked.connect(self.button_inserir_clicked)

        label_remover = QLabel(self)
        label_remover.setText("Remover elemento")
        label_remover.setStyleSheet("color: white; font-size: 15px; font-weight: bold;")
        label_remover.move(450, 40)

        self.remove_da_arvore()

        button_remover = QPushButton('Remover', self)
        button_remover.setStyleSheet("background-color: red; color: white; font-size: 15px; font-weight: bold;")
        button_remover.move(730, 50)
        button_remover.resize(100, 30)
        button_remover.clicked.connect(self.button_remover_clicked)

        button_inordem = QPushButton('In-ordem', self)
        button_inordem.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
        button_inordem.move(10, 90)
        button_inordem.resize(100, 30)
        button_inordem.clicked.connect(self.button_inordem_clicked)

        label_pesquisa = QLabel(self)
        label_pesquisa.setText("Pesquisar elemento")
        label_pesquisa.setStyleSheet("color: white; font-size: 15px; font-weight: bold;")
        label_pesquisa.move(10, 130)

        self.input_pesquisa()

        button_pesquisa = QPushButton('Pesquisar', self)
        button_pesquisa.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
        button_pesquisa.move(320, 140)
        button_pesquisa.resize(100, 30)
        button_pesquisa.clicked.connect(self.button_pesquisa_clicked)

        self.init_UI()
    
    def init_UI(self):
        self.setGeometry(10, 30, 1050, 700)
        self.setWindowTitle('Árvore')
        self.show()

    def input_arvore(self):
        entrada_arvore = QLineEdit(self)
        entrada_arvore.move(10, 60)
        entrada_arvore.resize(300, 20)
        entrada_arvore.setObjectName("entrada_arvore")
        entrada_arvore.setStyleSheet("color: white;")
        entrada_arvore.setPlaceholderText("Digite o valor")

    def input_pesquisa(self):
        entrada_arvore = QLineEdit(self)
        entrada_arvore.move(10, 150)
        entrada_arvore.resize(300, 20)
        entrada_arvore.setObjectName("entrada_arvore")
        entrada_arvore.setStyleSheet("color: white;")
        entrada_arvore.setPlaceholderText("Digite o valor")

    def remove_da_arvore(self):
        remove_da_arvore = QLineEdit(self)
        remove_da_arvore.move(450, 60)
        remove_da_arvore.resize(270, 20)
        remove_da_arvore.setObjectName("remove_da_arvore")
        remove_da_arvore.setStyleSheet("color: white;")
        remove_da_arvore.setPlaceholderText("Digite o valor")

    def image_black_bmp(self):
        imageblack = QLabel(self)
        imageblack.setPixmap(QPixmap("black.bmp"))
        imageblack.move(10, 180)
        imageblack.resize(600, 600)
        imageblack.show()

    def button_inserir_clicked(self):
        entrada_arvore = self.findChild(QLineEdit, "entrada_arvore")
        valor = entrada_arvore.text()
        lista_da_arvore.append(valor)
        arvore.insert(valor)
        print("\n"*10)
        arvore.imprimir_arvore()

    def button_remover_clicked(self):
        remove_da_arvore = self.findChild(QLineEdit, "remove_da_arvore")
        valor = remove_da_arvore.text()
        arvore.delete(valor)
        print("\n"*10)
        arvore.imprimir_arvore()

    def button_inordem_clicked(self):
        inor = arvore.inorder()
        print(inor)

    def button_pesquisa_clicked(self):
        entrada_arvore = self.findChild(QLineEdit, "entrada_arvore")
        valor = entrada_arvore.text()
        pesq = arvore.find(valor)
        print(pesq)
