# A program to create visualizations of the data structures (linked lists, sequential lists, stacks, queues, binary search trees) 
# PROJETO DE ESTRUTURA DE DADOS
# Grupo: Guilherme Nogueira, Luciano Pereira, Pedro Lucas, Thais Melquiades, Victória Grisi

from PyQt5.QtWidgets import *
import sys

from structures.linkedlist import LinkedList
from structures.queue import Queue
from structures.stack import Stack
from structures.node import Node

from interface.main_interface import janelamain

liste = LinkedList()

textoparainput = ''
posicao = 0
fila = Queue()
application = PyQt5.QtWidgets.QApplication(sys.argv)
janela = janelamain()
sys.exit(application.exec_())