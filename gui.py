import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from classes import *
import sys

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)

liste = LinkedList()
fila = Queue()
pilha = Stack()
arvore = Tree()

listadaarvore = []
tamanhomaximodapilha = 19

# LISTA LISTA LISTA LISTA
class janelalista(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #121212;")

        labellista = QLabel(self)
        labellista.setText("Lista Encadeada")
        labellista.setStyleSheet("color: white; font-size: 30px; font-weight: bold;")
        labellista.move(10, 10)

        listImage = QLabel(self)
        listImage.setPixmap(QPixmap("assets/list.png"))
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.3)
        listImage.setGraphicsEffect(self.opacity_effect)
        listImage.move(900, 550)
        listImage.show()

        labelentrada = QLabel(self)
        labelentrada.setText("Adicionar elemento")
        labelentrada.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        labelentrada.move(20, 60)

        labelremover = QLabel(self)
        labelremover.setText("Remover elemento")
        labelremover.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        labelremover.move(470, 60)

        labelconsutar = QLabel(self)
        labelconsutar.setText("Consultar elemento")
        labelconsutar.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        labelconsutar.move(20, 140)

        self.inputlista()
        self.consultarlista()
        #self.inputconsultar()   
        self.inputlistaposition()
        self.removedalistabutton()
        self.removedalista()
        self.removedalistaposicao()

        # add button
        addbutton = QPushButton('Adicionar', self)
        addbutton.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
        addbutton.move(330, 90)
        addbutton.resize(100, 30)
        addbutton.clicked.connect(self.addbutton_clicked)

        self.initUI()
        
    def initUI(self):
        self.setGeometry(10, 30, 1050, 700)
        self.setWindowTitle('DS Viewer')
        self.show()

    def consultarlista(self):
        self.consultarlista = QLineEdit(self)
        self.consultarlista.move(20, 170)
        self.consultarlista.resize(200, 30)
        self.consultarlista.setObjectName("consultarlista")
        self.consultarlista.setStyleSheet("color: white")
        self.consultarlista.setPlaceholderText("Valor do elemento")

        buttonconsultar = QPushButton('Consultar', self)
        buttonconsultar.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
        buttonconsultar.move(230, 170)
        buttonconsultar.resize(100, 30)
        buttonconsultar.clicked.connect(self.buttonconsultar_clicked)

    def buttonconsultar_clicked(self):
        print('Consultar')
        self.consultarlista = self.findChild(QLineEdit, 'consultarlista')
        print(self.consultarlista.text())
        estalanista = liste.searchandmatch(self.consultarlista.text())
        print(estalanista)

        # if the element is in the list show a message in the screen
        if estalanista >= 0:
            msg = QMessageBox()
            msg.setWindowTitle("Elemento encontrado")
            msg.setText("O elemento está na lista, na posição: "+str(liste.searchandmatch(self.consultarlista.text())))
            msg.setIcon(QMessageBox.Information)
            msg.exec_()

        # if the element is not in the list show a message in the screen
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Elemento não encontrado")
            msg.setText("O elemento não está na lista")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()

    def inputlista(self):
        entrada = QLineEdit(self)
        entrada.move(20, 90)
        entrada.resize(200, 30)
        entrada.setObjectName("entrada")
        entrada.setStyleSheet("color: white;")
        entrada.setPlaceholderText("Valor")
        entrada.textChanged.connect(self.onchanged) # Certifica que o texto foi alterado 

    def inputlistaposition(self):
        entradaposicao = QLineEdit(self)
        entradaposicao.move(230, 90)
        entradaposicao.resize(80, 30)
        entradaposicao.setObjectName("entradaposicao")
        entradaposicao.setStyleSheet("color: white;")
        entradaposicao.setPlaceholderText("Posição")
        entradaposicao.textChanged.connect(self.onchanged)

    # now create a button for remotion (red color with white text)
    def removedalistabutton(self):
        removedalistabutton = QPushButton('Remover', self)
        removedalistabutton.setStyleSheet("background-color: #FF0000; color: white; font-size: 15px; font-weight: bold;")
        removedalistabutton.move(790, 90)
        removedalistabutton.resize(100, 30)
        removedalistabutton.clicked.connect(self.removedalistabutton_clicked)

    def removedalista(self):
        entradaremove = QLineEdit(self)
        entradaremove.move(470, 90)
        entradaremove.resize(200, 30)
        entradaremove.setObjectName("entradaremove")
        entradaremove.setStyleSheet("color: white;")
        entradaremove.setPlaceholderText("Valor")
        entradaremove.textChanged.connect(self.onchanged)

    def removedalistaposicao(self):
        entradaremoveposicao = QLineEdit(self)
        entradaremoveposicao.move(680, 90)
        entradaremoveposicao.resize(95, 30)
        entradaremoveposicao.setObjectName("entradaremoveposicao")
        entradaremoveposicao.setStyleSheet("color: white;")
        entradaremoveposicao.setPlaceholderText("Posição")
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
  
    def onchanged(self, text):
        print(text)

# JANELA FILA FILA FILA FILA FILA
class janelafila(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #121212;")
        labelfila = QLabel(self)
        labelfila.setText("Fila")
        labelfila.setStyleSheet("color: white; font-size: 30px; font-weight: bold;")
        labelfila.move(10, 10)

        queueImage = QLabel(self)
        queueImage.setPixmap(QPixmap("assets/queue.png"))
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.3)
        queueImage.setGraphicsEffect(self.opacity_effect)
        queueImage.move(900, 550)
        queueImage.show()

        labelenfileirar = QLabel(self)
        labelenfileirar.setText("Enfileirar elemento")
        labelenfileirar.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        labelenfileirar.move(20, 60)

        labelprimeirofila = QLabel(self)
        labelprimeirofila.setText("Primeiro da fila")
        labelprimeirofila.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        labelprimeirofila.move(20, 500)

        enqueuebutton = QPushButton('Enfileirar', self)
        enqueuebutton.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
        enqueuebutton.move(40, 130)
        enqueuebutton.resize(120, 30)
        enqueuebutton.clicked.connect(self.enqueuebutton_clicked)

        dequeuebutton = QPushButton('Desenfileirar', self)
        dequeuebutton.setStyleSheet("background-color: red; color: white; font-size: 15px; font-weight: bold;")
        dequeuebutton.move(180, 130)
        dequeuebutton.resize(120, 30)
        dequeuebutton.clicked.connect(self.dequeuebutton_clicked)

        self.inputfila()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(10, 30, 1050, 700)
        self.setWindowTitle('Fila')
        self.show()

    def inputfila(self):
        entradafila = QLineEdit(self)
        entradafila.move(20, 90)
        entradafila.resize(300, 30)
        entradafila.setObjectName("entradafila")
        entradafila.setStyleSheet("color: white;")
        entradafila.setPlaceholderText("Valor")
        
    def enqueuebutton_clicked(self):
        print("enqueue button clicked")
        textoparainputfila = self.findChild(QLineEdit, 'entradafila').text()
        # if there is no text in the input, do nothing
        if textoparainputfila == "":
            return

        fila.enqueue(textoparainputfila)
        lastelement = fila.get(fila.size() - 1)
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
        button = QPushButton(str(lastelement), self)
        button.setObjectName("primeirofila")
        button.setStyleSheet("background-color: orange; color: white; font-size: 15px; font-weight: bold;")
        button.move(20, 530)
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
            button.move(20 + i * 50, 400)  
            button.resize(50, 30)
            button.show()

        lastelement = fila.get(fila.size() - 1)
        print("checgou aqui")
        labelprimeirofila = QLabel(self)
        labelprimeirofila.setText("Primeiro da fila")
        labelprimeirofila.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        labelprimeirofila.move(20, 500)
        labelprimeirofila.show()

        button = QPushButton(str(lastelement), self)
        button.setObjectName("primeirofila")
        button.setStyleSheet("background-color: orange; color: white; font-size: 15px; font-weight: bold;")
        button.move(20, 530)
        button.resize(50, 30)
        button.show()

    def imageblackbmp(self):
        imageblack = QLabel(self)
        imageblack.setPixmap(QPixmap("black.bmp"))
        imageblack.move(10, 200)
        imageblack.resize(600, 600)
        imageblack.show()

# ARVORE ARVORE ARVORE ARVORE ARVORE
class janelaarvore(QWidget):
    def __init__(self):
        super().__init__()
        arvore = Tree()
        
        self.setStyleSheet("background-color: black;")
        labelarvore = QLabel(self)
        labelarvore.setText("Árvore")
        labelarvore.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        labelarvore.move(10, 10)

        treeImage = QLabel(self)
        treeImage.setPixmap(QPixmap("assets/tree.png"))
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.3)
        treeImage.setGraphicsEffect(self.opacity_effect)
        treeImage.move(900, 550)
        treeImage.show()

        labelinserir = QLabel(self)
        labelinserir.setText("Inserir elemento")
        labelinserir.setStyleSheet("color: white; font-size: 15px; font-weight: bold;")
        labelinserir.move(10, 40)

        self.inputarvore()

        buttoninserir = QPushButton('Inserir', self)
        buttoninserir.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
        buttoninserir.move(320, 50)
        buttoninserir.resize(100, 30)
        buttoninserir.clicked.connect(self.buttoninserir_clicked)

        labelremover = QLabel(self)
        labelremover.setText("Remover elemento")
        labelremover.setStyleSheet("color: white; font-size: 15px; font-weight: bold;")
        labelremover.move(450, 40)

        self.removedaarvore()

        buttonremover = QPushButton('Remover', self)
        buttonremover.setStyleSheet("background-color: red; color: white; font-size: 15px; font-weight: bold;")
        buttonremover.move(730, 50)
        buttonremover.resize(100, 30)
        buttonremover.clicked.connect(self.buttonremover_clicked)

        buttoninordem = QPushButton('In-ordem', self)
        buttoninordem.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
        buttoninordem.move(10, 90)
        buttoninordem.resize(100, 30)
        buttoninordem.clicked.connect(self.buttoninordem_clicked)

        labelpesquisa = QLabel(self)
        labelpesquisa.setText("Pesquisar elemento")
        labelpesquisa.setStyleSheet("color: white; font-size: 15px; font-weight: bold;")
        labelpesquisa.move(10, 130)

        self.inputpesquisa()

        buttonpesquisa = QPushButton('Pesquisar', self)
        buttonpesquisa.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
        buttonpesquisa.move(320, 140)
        buttonpesquisa.resize(100, 30)
        buttonpesquisa.clicked.connect(self.buttonpesquisa_clicked)

        self.initUI()
    
    def initUI(self):
        self.setGeometry(10, 30, 1050, 700)
        self.setWindowTitle('Árvore')
        self.show()

    def inputarvore(self):
        entradaarvore = QLineEdit(self)
        entradaarvore.move(10, 60)
        entradaarvore.resize(300, 20)
        entradaarvore.setObjectName("entradaarvore")
        entradaarvore.setStyleSheet("color: white;")
        entradaarvore.setPlaceholderText("Digite o valor")

    def inputpesquisa(self):
        entradaarvore = QLineEdit(self)
        entradaarvore.move(10, 150)
        entradaarvore.resize(300, 20)
        entradaarvore.setObjectName("entradaarvore")
        entradaarvore.setStyleSheet("color: white;")
        entradaarvore.setPlaceholderText("Digite o valor")

    def removedaarvore(self):
        removedaarvore = QLineEdit(self)
        removedaarvore.move(450, 60)
        removedaarvore.resize(270, 20)
        removedaarvore.setObjectName("removedaarvore")
        removedaarvore.setStyleSheet("color: white;")
        removedaarvore.setPlaceholderText("Digite o valor")

    def imageblackbmp(self):
        imageblack = QLabel(self)
        imageblack.setPixmap(QPixmap("black.bmp"))
        imageblack.move(10, 180)
        imageblack.resize(600, 600)
        imageblack.show()

    def buttoninserir_clicked(self):
        entradaarvore = self.findChild(QLineEdit, "entradaarvore")
        valor = entradaarvore.text()
        listadaarvore.append(valor)
        arvore.insert(valor)
        print("\n"*10)
        arvore.imprimirarvore()

        #self.imageblackbmp()

    def buttonremover_clicked(self):
        removedaarvore = self.findChild(QLineEdit, "removedaarvore")
        valor = removedaarvore.text()
        arvore.delete(valor)
        print("\n"*10)
        arvore.imprimirarvore()

        #self.imageblackbmp()

    def buttoninordem_clicked(self):
        inor = arvore.inorder()
        print(inor)

    def buttonpesquisa_clicked(self):
        entradaarvore = self.findChild(QLineEdit, "entradaarvore")
        valor = entradaarvore.text()
        pesq = arvore.find(valor)
        print(pesq)

class janelapilha(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setStyleSheet("background-color: #121212;")
        labelpilha = QLabel(self)
        labelpilha.setText("Pilha")
        labelpilha.setStyleSheet("color: white; font-size: 30px; font-weight: bold;")
        labelpilha.move(10, 10)

        stackImage = QLabel(self)
        stackImage.setPixmap(QPixmap("assets/stack.png"))
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.3)
        stackImage.setGraphicsEffect(self.opacity_effect)
        stackImage.move(900, 550)
        stackImage.show()

        labeltopopilha = QLabel(self)
        labeltopopilha.setText("Topo da pilha")
        labeltopopilha.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        labeltopopilha.move(200, 130)

        labelempilhar = QLabel(self)
        labelempilhar.setText("Empilhar elemento")
        labelempilhar.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        labelempilhar.move(20, 60)

        self.inputpilha()

        buttonempilhar = QPushButton('Empilhar', self)
        buttonempilhar.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
        buttonempilhar.move(330, 90)
        buttonempilhar.resize(100, 30)
        buttonempilhar.clicked.connect(self.buttonempilhar_clicked)

        buttondesempilhar = QPushButton('Desempilhar', self)
        buttondesempilhar.setStyleSheet("background-color: red; color: white; font-size: 15px; font-weight: bold;")
        buttondesempilhar.move(440, 90)
        buttondesempilhar.resize(100, 30)
        buttondesempilhar.clicked.connect(self.buttondesempilhar_clicked)

        self.initUI()

    def initUI(self):
        self.setGeometry(10, 30, 1050, 700)
        self.setWindowTitle('Pilha')
        self.show() 

    def inputpilha(self):
        entradaarvore = QLineEdit(self)
        entradaarvore.move(20, 90)
        entradaarvore.resize(300, 30)
        entradaarvore.setObjectName("entradapilha")
        entradaarvore.setStyleSheet("color: white;")
        entradaarvore.setPlaceholderText("Digite o valor")

    def buttonempilhar_clicked(self):
        
        entradapilha = self.findChild(QLineEdit, "entradapilha")
        valor = entradapilha.text()

        if valor == "":
            return

        # if the stack is full (size == tamanhomaximodapilha) return
        if pilha.size() == tamanhomaximodapilha:
            return

        pilha.push(valor)
        topofpilha = pilha.top()
        print(pilha)

        for i in range(pilha.size()):
            buttonpilha = QPushButton(str(pilha.get(i)), self)
            buttonpilha.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
            buttonpilha.move(20, 650 - (i * 30))
            buttonpilha.resize(60, 30)
            buttonpilha.show()

        buttontopo = QPushButton(str(topofpilha), self)
        buttontopo.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
        buttontopo.move(235, 180)
        buttontopo.resize(60, 30)
        buttontopo.show()

    def imageblackbmp(self):
        imageblack = QLabel(self)
        imageblack.setPixmap(QPixmap("black.png"))
        imageblack.move(10, 200)
        imageblack.resize(600, 600)
        imageblack.show()

    def buttondesempilhar_clicked(self):
        pilha.pop()
        print(pilha)
        topofpilha = pilha.top()
        self.imageblackbmp()
        for i in range(pilha.size()):
            buttonpilha = QPushButton(str(pilha.get(i)), self)
            buttonpilha.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
            buttonpilha.move(20, 650 - (i * 30))
            buttonpilha.resize(60, 30)
            buttonpilha.show()

        buttontopo = QPushButton(str(topofpilha), self)
        buttontopo.setStyleSheet("background-color: #008A00; color: white; font-size: 15px; font-weight: bold;")
        buttontopo.move(235, 180)
        buttontopo.resize(60, 30)
        buttontopo.show()
        
class janelamain(QMainWindow):
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

        self.computerImg()
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
        label1 = QLabel('Data Structure Viewer', self)
        # move to the center top of the window
        label1.setAlignment(Qt.AlignCenter)
        #label1.move(100, 10)
        label1.resize(1050, 50)
        label1.setStyleSheet("background-color: #121212; color: white; font-weight: bold; font-size: 32px; font-family: Lucida Sans Unicode; font-style: italic")
        label1.show()

    def computerImg(self):
        imgComp = QPixmap('./assets/computer.png')
        computerImage = QLabel(self)
        computerImage.setPixmap(imgComp)
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.3)
        computerImage.setGraphicsEffect(self.opacity_effect)
        computerImage.resize(128,128)
        computerImage.move(900,550)
        computerImage.show()

    def lista(self):
        lista_button = QPushButton('Lista Encadeada', self)
        
        lista_button.move(375, 140)
        lista_button.resize(300, 50)
        lista_button.setStyleSheet("background-color: blue; color: white; font-weight: bold; font-size: 15px; font-family: Lucida Sans Unicode")
        lista_button.clicked.connect(self.listaclick)

    def listaclick(self):
        print('Lista Encadeada')
        self.lista = janelalista()

    def pilha(self):
        pilha_button = QPushButton('Pilha', self)
        pilha_button.move(375, 200)
        pilha_button.resize(300, 50)
        pilha_button.setStyleSheet("background-color: blue; color: white; font-weight: bold; font-size: 15px; font-family: Lucida Sans Unicode")
        pilha_button.clicked.connect(self.pilhaclick)
    
    def pilhaclick(self):
        print('Pilha')
        self.pilha = janelapilha()

    def fila(self):
        fila_button = QPushButton('Fila', self)
        fila_button.move(375, 260)
        fila_button.resize(300, 50)
        fila_button.setStyleSheet("background-color: blue; color: white; font-weight: bold; font-size: 15px; font-family: Lucida Sans Unicode")
        fila_button.clicked.connect(self.filaclick)

    def filaclick(self):
        print('Fila')
        print(self.objectName())
        self.fila = janelafila()

    def arvore(self):
        arvore_button = QPushButton('Arvore', self)
        arvore_button.move(375, 320)
        arvore_button.resize(300, 50)
        arvore_button.setStyleSheet("background-color: blue; color: white; font-weight: bold; font-size: 15px; font-family: Lucida Sans Unicode")
        arvore_button.clicked.connect(self.arvoreclick)
    
    def arvoreclick(self):
        self.arvore = janelaarvore()
        print('Arvore')