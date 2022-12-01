import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import sys

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
    # get a value from the list by index
    def get(self, index):
        return self.items[index]
    
    
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

liste = LinkedList()

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

    def labelseta(self,x,y): # UNICODE U+2794
        labelseta = QLabel(self)
        labelseta.setText("➔")
        labelseta.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        labelseta.move(x, y)
    
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

        # delete the list of buttons (refresh)
        #button.deleteLater()
        button = []
        #button[i].deleteLater()
        
        for i in range(liste.size()):
            
            # create a list of buttons (SERVE PRA PILHA E FILA, LISTA É FEIO) SIMBORAAAAAAAA
            
            button = QPushButton(str(liste.get(i)), self)
            button.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
            button.move(10 + i * 50, 400)  
            button.resize(50, 30)
            button.show()
        

        


        print(liste)
        print("posicao =", posicao)

    def removedalistabutton_clicked(self):
        print("remove button clicked")
        textoparainput = self.findChild(QLineEdit, 'entradaremove').text()
        posicaoremover = self.findChild(QLineEdit, 'entradaremoveposicao').text()
        # if there is no text in the input, do nothing
        if textoparainput == "" and posicaoremover == "":
            return
        elif textoparainput != "" and posicaoremover != "":
            return
        elif textoparainput != "":
            liste.remove(textoparainput)
        elif posicaoremover != "":
            print(liste.size())
            # if the position is not a number, do nothing
            if not posicaoremover.isnumeric():
                return
            # if the position is not in the list, do nothing
            if int(posicaoremover) >= liste.size():
                return
            print(posicaoremover)
            liste.pop(int(posicaoremover))
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

        labeldesenfileirar = QLabel(self)
        labeldesenfileirar.setText("Desenfileirar elemento")
        labeldesenfileirar.setStyleSheet("color: white; font-size: 15px; font-weight: bold;")
        labeldesenfileirar.move(460, 40)

        enqueuebutton = QPushButton('Enfileirar', self)
        enqueuebutton.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
        enqueuebutton.move(320, 50)
        enqueuebutton.resize(100, 30)
        enqueuebutton.clicked.connect(self.enqueuebutton_clicked)
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
        # remove exit button from the window
        

        

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
        #fila_button.deleteLater()

    def filaclick(self):
        print('Fila')
        self.fila = janelafila()

    def arvore(self):
        arvore_button = QPushButton('Arvore', self)
        arvore_button.move(10, 210)
        arvore_button.resize(200, 40)
        arvore_button.setStyleSheet("background-color: blue; color: white; font-weight: bold; font-size: 15px; font-family: Lucida Sans Unicode")
        arvore_button.clicked.connect(self.arvoreclick)
    
    def arvoreclick(self):
        print('Arvore')
