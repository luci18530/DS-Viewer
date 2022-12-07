import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from classes.queue import Queue
import sys

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

fila = Queue()

lista_da_arvore = []
tamanho_maximo_da_pilha = 19

class janela_fila(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #121212;")
        label_fila = QLabel(self)
        label_fila.setText("Fila")
        label_fila.setStyleSheet("color: white; font-size: 30px; font-weight: bold;")
        label_fila.move(10, 10)

        queue_image = QLabel(self)
        queue_image.setPixmap(QPixmap("assets/queue.png"))
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.3)
        queue_image.setGraphicsEffect(self.opacity_effect)
        queue_image.move(900, 550)
        queue_image.show()

        label_enfileirar = QLabel(self)
        label_enfileirar.setText("Enfileirar elemento")
        label_enfileirar.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        label_enfileirar.move(20, 60)

        label_primeiro_fila = QLabel(self)
        label_primeiro_fila.setText("Primeiro da fila")
        label_primeiro_fila.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        label_primeiro_fila.move(20, 500)

        enqueue_button = QPushButton('Enfileirar', self)
        enqueue_button.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
        enqueue_button.move(40, 130)
        enqueue_button.resize(120, 30)
        enqueue_button.clicked.connect(self.enqueue_button_clicked)

        dequeue_button = QPushButton('Desenfileirar', self)
        dequeue_button.setStyleSheet("background-color: red; color: white; font-size: 15px; font-weight: bold;")
        dequeue_button.move(180, 130)
        dequeue_button.resize(120, 30)
        dequeue_button.clicked.connect(self.dequeue_button_clicked)

        self.inputfila()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(10, 30, 1050, 700)
        self.setWindowTitle('Fila')
        self.show()

    def inputfila(self):
        entrada_fila = QLineEdit(self)
        entrada_fila.move(20, 90)
        entrada_fila.resize(300, 30)
        entrada_fila.setObjectName("entrada_fila")
        entrada_fila.setStyleSheet("color: white;")
        entrada_fila.setPlaceholderText("Valor")
        
    def enqueue_button_clicked(self):
        print("enqueue button clicked")
        texto_para_input_fila = self.findChild(QLineEdit, 'entrada_fila').text()
        # if there is no text in the input, do nothing
        if texto_para_input_fila == "":
            return

        fila.enqueue(texto_para_input_fila)
        last_element = fila.get(fila.size() - 1)
        print(fila)
        for i in range (fila.size()):
            button = QPushButton(str(fila.get(i)), self)
            # set id for each button
            button.setObjectName(str(i))
            button.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
            button.move(20 + i * 50, 400)  
            button.resize(50, 30)
            button.show()

        # show a button that shows the first element of the queue 
        button = QPushButton(str(last_element), self)
        button.setObjectName("primeirofila")
        button.setStyleSheet("background-color: orange; color: white; font-size: 15px; font-weight: bold;")
        button.move(20, 530)
        button.resize(50, 30)
        button.show()


    def dequeue_button_clicked(self):
        print("dequeue button clicked")
        fila.dequeue()
        print(fila)
        self.image_black_bmp()
        for i in range (fila.size()):
            button = QPushButton(str(fila.get(i)), self)
            # set id for each button
            button.setObjectName(str(i))
            button.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
            button.move(20 + i * 50, 400)  
            button.resize(50, 30)
            button.show()

        last_element = fila.get(fila.size() - 1)
        print("checgou aqui")
        label_primeiro_fila = QLabel(self)
        label_primeiro_fila.setText("Primeiro da fila")
        label_primeiro_fila.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        label_primeiro_fila.move(20, 500)
        label_primeiro_fila.show()

        button = QPushButton(str(last_element), self)
        button.setObjectName("primeirofila")
        button.setStyleSheet("background-color: orange; color: white; font-size: 15px; font-weight: bold;")
        button.move(20, 530)
        button.resize(50, 30)
        button.show()

    def image_black_bmp(self):
        imageblack = QLabel(self)
        imageblack.setPixmap(QPixmap("black.bmp"))
        imageblack.move(10, 200)
        imageblack.resize(600, 600)
        imageblack.show()
