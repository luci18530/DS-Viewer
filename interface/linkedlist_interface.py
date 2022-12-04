import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

from utils import *
import sys

class janelalista(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: black;")
        labellista = QLabel(self)
        labellista.setText("Lista Encadeada")
        labellista.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        labellista.move(10, 10)

        labelentrada = QLabel(self)
        labelentrada.setText("Adicionar elemento")
        labelentrada.setStyleSheet("color: white; font-size: 15px; font-weight: bold;")
        labelentrada.move(10, 40)

        labelremover = QLabel(self)
        labelremover.setText("Remover elemento")
        labelremover.setStyleSheet("color: white; font-size: 15px; font-weight: bold;")
        labelremover.move(460, 40)

        painter = QPainter(self)
        painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        painter.drawRect(0,300, 900, 400)
        painter.end()

        self.inputlista()       
        self.inputlistaposition()
        self.removedalistabutton()
        self.removedalista()
        self.removedalistaposicao()

        # add button
        addbutton = QPushButton('Adicionar', self)
        addbutton.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
        addbutton.move(320, 50)
        addbutton.resize(100, 30)
        addbutton.clicked.connect(self.addbutton_clicked)

        self.initUI()
        
    def initUI(self):
        self.setGeometry(10, 30, 1050, 700)
        self.setWindowTitle('Lista Encadeada')
        self.show()

    def inputlista(self):
        entrada = QLineEdit(self)
        entrada.move(10, 60)
        entrada.resize(200, 20)
        entrada.setObjectName("entrada")
        entrada.setStyleSheet("color: white;")
        entrada.setPlaceholderText("Digite um valor")
        entrada.textChanged.connect(self.onchanged) # Certifica que o texto foi alterado 

    def inputlistaposition(self):
        entradaposicao = QLineEdit(self)
        entradaposicao.move(220, 60)
        entradaposicao.resize(81, 20)
        entradaposicao.setObjectName("entradaposicao")
        entradaposicao.setStyleSheet("color: white;")
        entradaposicao.setPlaceholderText("Digite a posição")
        entradaposicao.textChanged.connect(self.onchanged)

    # now create a button for remotion (red color with white text)
    def removedalistabutton(self):
        removedalistabutton = QPushButton('Remover', self)
        removedalistabutton.setStyleSheet("background-color: #FF0000; color: white; font-size: 15px; font-weight: bold;")
        removedalistabutton.move(780, 50)
        removedalistabutton.resize(100, 30)
        removedalistabutton.clicked.connect(self.removedalistabutton_clicked)

    def removedalista(self):
        entradaremove = QLineEdit(self)
        entradaremove.move(460, 60)
        entradaremove.resize(200, 20)
        entradaremove.setObjectName("entradaremove")
        entradaremove.setStyleSheet("color: white;")
        entradaremove.setPlaceholderText("Digite o valor a remover")
        entradaremove.textChanged.connect(self.onchanged)

    def removedalistaposicao(self):
        entradaremoveposicao = QLineEdit(self)
        entradaremoveposicao.move(670, 60)
        entradaremoveposicao.resize(95, 20)
        entradaremoveposicao.setObjectName("entradaremoveposicao")
        entradaremoveposicao.setStyleSheet("color: white;")
        entradaremoveposicao.setPlaceholderText("Posição a remover")
        entradaremoveposicao.textChanged.connect(self.onchanged)

    def addbutton_clicked(self):
        print("add button clicked")

        textoparainput = self.findChild(QLineEdit, 'entrada').text()
        # if there is no text in the input, do nothing
        if textoparainput == "":
            return

        posicao = self.findChild(QLineEdit, 'entradaposicao').text()
        # if there is no text in the input, do nothing
        if posicao == "":
            return

        # if position is not a number, do nothing
        if not posicao.isnumeric():
            return

        liste.insert(int(posicao), textoparainput)

        button = []

        
        for i in range(liste.size()):       
            # create a list of buttons (SERVE PRA PILHA E FILA, LISTA É FEIO) SIMBORAAAAAAAA           
            button = QPushButton(str(liste.get(i)), self)
            button.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
            button.move(10 + i * 50, 400)  
            button.resize(50, 30)
            button.show()

        print(liste)
        print("posicao =", posicao)

    def imageblackbmp(self):
        imageblack = QLabel(self)
        imageblack.setPixmap(QPixmap("black.bmp"))
        imageblack.move(10, 200)
        imageblack.resize(600, 600)
        imageblack.show()

    def removedalistabutton_clicked(self):
        print("remove button clicked")
        textoparainput = self.findChild(QLineEdit, 'entradaremove').text()
        posicaoremover = self.findChild(QLineEdit, 'entradaremoveposicao').text()
        # if there is no text in the input, do nothing
        if textoparainput == "" and posicaoremover == "":
            print("nenhum valor digitado")
            return
        if textoparainput != "" and posicaoremover != "":
            print("digite apenas um valor")
            return
        if textoparainput != "" and posicaoremover == "":
            print("removendo por valor")

            liste.remove(textoparainput)
            print("tam lista ",liste.size())
            self.imageblackbmp()

            for i in range(liste.size()):       
            # create a list of buttons (SERVE PRA PILHA E FILA, LISTA É FEIO) SIMBORAAAAAAAA
                
                
                button = QPushButton(str(liste.get(i)), self)
                # set id for each button
                button.setObjectName(str(i))
                button.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
                button.move(10 + i * 50, 400)  
                button.resize(50, 30)
                button.show()

        if posicaoremover != "" and textoparainput == "":
            print("removendo por posição")
            print(liste.size())
            # if the position is not a number, do nothing
            if not posicaoremover.isnumeric():
                return
            # if the position is not in the list, do nothing
            if int(posicaoremover) >= liste.size():
                return
            print(posicaoremover)
            liste.pop(int(posicaoremover))

            self.imageblackbmp()

            for i in range(liste.size()):       
            # create a list of buttons (SERVE PRA PILHA E FILA, LISTA É FEIO) SIMBORAAAAAAAA
                # LOAD IMAGE
                print("i =", i)

                button = QPushButton(str(liste.get(i)), self)
                # set id for each button
                button.setObjectName(str(i))
                button.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
                button.move(10 + i * 50, 400)  
                button.resize(50, 30)
                button.show()

            print(liste)


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Insert:
            
            print("Insert")
            textoparainput = self.findChild(QLineEdit, "entrada").text()
            posicao = self.findChild(QLineEdit, "entradaposicao").text()
            liste.insert(int(posicao), textoparainput)
            print(liste)
            print("posicao =", posicao)

        elif e.key() == Qt.Key_Control:
            print("Delete")
            textopararemove = self.findChild(QLineEdit, "entradaremove").text()
            liste.remove(textopararemove)
            print(liste)
  
    def onchanged(self, text):
        print(text)