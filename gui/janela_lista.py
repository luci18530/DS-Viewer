import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from classes.linked_list import LinkedList
import sys

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

lista = LinkedList()

lista_da_arvore = []
tamanho_maximo_da_pilha = 19

class janela_lista(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #121212;")

        label_lista = QLabel(self)
        label_lista.setText("Lista Encadeada")
        label_lista.setStyleSheet("color: white; font-size: 30px; font-weight: bold;")
        label_lista.move(10, 10)

        list_image = QLabel(self)
        list_image.setPixmap(QPixmap("assets/list.png"))
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.3)
        list_image.setGraphicsEffect(self.opacity_effect)
        list_image.move(900, 550)
        list_image.show()

        label_entrada = QLabel(self)
        label_entrada.setText("Adicionar elemento")
        label_entrada.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        label_entrada.move(20, 60)

        label_remover = QLabel(self)
        label_remover.setText("Remover elemento")
        label_remover.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        label_remover.move(470, 60)

        label_consultar = QLabel(self)
        label_consultar.setText("Consultar elemento")
        label_consultar.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        label_consultar.move(20, 140)

        self.input_lista()
        self.consultar_lista()
        self.input_lista_position()
        self.remove_da_lista_button()
        self.remove_da_lista()
        self.remove_da_lista_posicao()

        # add button
        add_button = QPushButton('Adicionar', self)
        add_button.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
        add_button.move(330, 90)
        add_button.resize(100, 30)
        add_button.clicked.connect(self.addbutton_clicked)

        self.initUI()
        
    def initUI(self):
        self.setGeometry(10, 30, 1050, 700)
        self.setWindowTitle('DS Viewer')
        self.show()

    def consultar_lista(self):
        self.consultar_lista = QLineEdit(self)
        self.consultar_lista.move(20, 170)
        self.consultar_lista.resize(200, 30)
        self.consultar_lista.setObjectName("consultar_lista")
        self.consultar_lista.setStyleSheet("color: white")
        self.consultar_lista.setPlaceholderText("Valor do elemento")

        button_consultar = QPushButton('Consultar', self)
        button_consultar.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
        button_consultar.move(230, 170)
        button_consultar.resize(100, 30)
        button_consultar.clicked.connect(self.buttonconsultar_clicked)

    def buttonconsultar_clicked(self):
        print('Consultar')
        self.consultar_lista = self.findChild(QLineEdit, 'consultar_lista')
        print(self.consultar_lista.text())
        esta_na_lista = lista.searchandmatch(self.consultar_lista.text())
        print(esta_na_lista)

        # if the element is in the list show a message in the screen
        if esta_na_lista >= 0:
            msg = QMessageBox()
            msg.setWindowTitle("Elemento encontrado")
            msg.setText("O elemento está na lista, no índice: "+str(lista.searchandmatch(self.consultar_lista.text())))
            msg.setIcon(QMessageBox.Information)
            msg.exec_()

        # if the element is not in the list show a message in the screen
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Elemento não encontrado")
            msg.setText("O elemento não está na lista")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()

    def input_lista(self):
        entrada = QLineEdit(self)
        entrada.move(20, 90)
        entrada.resize(200, 30)
        entrada.setObjectName("entrada")
        entrada.setStyleSheet("color: white;")
        entrada.setPlaceholderText("Valor")
        entrada.textChanged.connect(self.onchanged) # Certifica que o texto foi alterado 

    def input_lista_position(self):
        entrada_posicao = QLineEdit(self)
        entrada_posicao.move(230, 90)
        entrada_posicao.resize(80, 30)
        entrada_posicao.setObjectName("entrada_posicao")
        entrada_posicao.setStyleSheet("color: white;")
        entrada_posicao.setPlaceholderText("Índice")
        entrada_posicao.textChanged.connect(self.onchanged)

    # now create a button for remotion (red color with white text)
    def remove_da_lista_button(self):
        remove_da_lista_button = QPushButton('Remover', self)
        remove_da_lista_button.setStyleSheet("background-color: #FF0000; color: white; font-size: 15px; font-weight: bold;")
        remove_da_lista_button.move(790, 90)
        remove_da_lista_button.resize(100, 30)
        remove_da_lista_button.clicked.connect(self.remove_da_lista_button_clicked)

    def remove_da_lista(self):
        entrada_remove = QLineEdit(self)
        entrada_remove.move(470, 90)
        entrada_remove.resize(200, 30)
        entrada_remove.setObjectName("entrada_remove")
        entrada_remove.setStyleSheet("color: white;")
        entrada_remove.setPlaceholderText("Valor")
        entrada_remove.textChanged.connect(self.onchanged)

    def remove_da_lista_posicao(self):
        entrada_remove_posicao = QLineEdit(self)
        entrada_remove_posicao.move(680, 90)
        entrada_remove_posicao.resize(95, 30)
        entrada_remove_posicao.setObjectName("entrada_remove_posicao")
        entrada_remove_posicao.setStyleSheet("color: white;")
        entrada_remove_posicao.setPlaceholderText("Índice")
        entrada_remove_posicao.textChanged.connect(self.onchanged)

    def addbutton_clicked(self):
        print("add button clicked")

        texto_para_input = self.findChild(QLineEdit, 'entrada').text()
        # if there is no text in the input, do nothing
        if texto_para_input == "":
            return

        indice = self.findChild(QLineEdit, 'entrada_posicao').text()
        # if there is no text in the input, do nothing
        if indice == "":
            return

        # if position is not a number, do nothing
        if not indice.isnumeric():
            return

        lista.insert(int(indice), texto_para_input)

        button = []

        
        for i in range(lista.size()):       
            # create a list of buttons (SERVE PRA PILHA E FILA, LISTA É FEIO) SIMBORAAAAAAAA           
            button = QPushButton(str(lista.get(i)), self)
            button.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
            button.move(10 + i * 50, 400)  
            button.resize(50, 30)
            button.show()

        print(lista)
        print("indice =", indice)

    def image_black_bmp(self):
        imageblack = QLabel(self)
        imageblack.setPixmap(QPixmap("black.bmp"))
        imageblack.move(10, 200)
        imageblack.resize(600, 600)
        imageblack.show()

    def remove_da_lista_button_clicked(self):
        print("remove button clicked")
        texto_para_input = self.findChild(QLineEdit, 'entrada_remove').text()
        posicao_remover = self.findChild(QLineEdit, 'entrada_remove_posicao').text()
        # if there is no text in the input, do nothing
        if texto_para_input == "" and posicao_remover == "":
            print("nenhum valor digitado")
            return
        if texto_para_input != "" and posicao_remover != "":
            print("digite apenas um valor")
            return
        if texto_para_input != "" and posicao_remover == "":
            print("removendo por valor")

            lista.remove(texto_para_input)
            print("tam lista ",lista.size())
            self.image_black_bmp()

            for i in range(lista.size()):       
            # create a list of buttons (SERVE PRA PILHA E FILA, LISTA É FEIO) SIMBORAAAAAAAA
                
                
                button = QPushButton(str(lista.get(i)), self)
                # set id for each button
                button.setObjectName(str(i))
                button.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
                button.move(10 + i * 50, 400)  
                button.resize(50, 30)
                button.show()

        if posicao_remover != "" and texto_para_input == "":
            print("removendo por indice")
            print(lista.size())
            # if the position is not a number, do nothing
            if not posicao_remover.isnumeric():
                return
            # if the position is not in the list, do nothing
            if int(posicao_remover) >= lista.size():
                return
            print(posicao_remover)
            lista.pop(int(posicao_remover))

            self.image_black_bmp()

            for i in range(lista.size()):       
            # create a list of buttons (SERVE PRA PILHA E FILA, LISTA É FEIO) SIMBORAAAAAAAA
                # LOAD IMAGE
                print("i =", i)

                button = QPushButton(str(lista.get(i)), self)
                # set id for each button
                button.setObjectName(str(i))
                button.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
                button.move(10 + i * 50, 400)  
                button.resize(50, 30)
                button.show()

            print(lista)
  
    def onchanged(self, text):
        print(text)
