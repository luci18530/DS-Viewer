import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

from utils import *
import sys

class janelafila(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: black;")
        labelfila = QLabel(self)
        labelfila.setText("Fila")
        labelfila.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        labelfila.move(10, 10)

        labelenfileirar = QLabel(self)
        labelenfileirar.setText("Enfileirar elemento")
        labelenfileirar.setStyleSheet("color: white; font-size: 15px; font-weight: bold;")
        labelenfileirar.move(10, 40)

        enqueuebutton = QPushButton('Enfileirar', self)
        enqueuebutton.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
        enqueuebutton.move(320, 50)
        enqueuebutton.resize(100, 30)
        enqueuebutton.clicked.connect(self.enqueuebutton_clicked)

        dequeuebutton = QPushButton('Desenfileirar', self)
        dequeuebutton.setStyleSheet("background-color: red; color: white; font-size: 15px; font-weight: bold;")
        dequeuebutton.move(320, 90)
        dequeuebutton.resize(100, 30)
        dequeuebutton.clicked.connect(self.dequeuebutton_clicked)

        self.inputfila()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(10, 30, 1050, 700)
        self.setWindowTitle('Fila')
        self.show()

    def inputfila(self):
        entradafila = QLineEdit(self)
        entradafila.move(10, 60)
        entradafila.resize(300, 20)
        entradafila.setObjectName("entradafila")
        entradafila.setStyleSheet("color: white;")
        entradafila.setPlaceholderText("Digite o valor")
        
    def enqueuebutton_clicked(self):
        print("enqueue button clicked")
        textoparainputfila = self.findChild(QLineEdit, 'entradafila').text()
        # if there is no text in the input, do nothing
        if textoparainputfila == "":
            return

        fila.enqueue(textoparainputfila)
        print(fila)
        for i in range (fila.size()):
            button = QPushButton(str(fila.get(i)), self)
            # set id for each button
            button.setObjectName(str(i))
            button.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
            button.move(10 + i * 50, 400)  
            button.resize(50, 30)
            button.show()

    def dequeuebutton_clicked(self):
        print("dequeue button clicked")
        fila.dequeue()
        print(fila)
        self.imageblackbmp()
        for i in range (fila.size()):
            button = QPushButton(str(fila.get(i)), self)
            # set id for each button
            button.setObjectName(str(i))
            button.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
            button.move(10 + i * 50, 400)  
            button.resize(50, 30)
            button.show()

    def imageblackbmp(self):
        imageblack = QLabel(self)
        imageblack.setPixmap(QPixmap("black.bmp"))
        imageblack.move(10, 200)
        imageblack.resize(600, 600)
        imageblack.show()