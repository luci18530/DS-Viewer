# A program to create visualizations of the data structures (linked lists, sequential lists, stacks, queues, binary search trees) 
# PROJETO DE ESTRUTURA DE DADOS
# Grupo: Guilherme Nogueira, Luciano Pereira, Pedro Lucas, Thais Melquiades, Victória Grisi
import PyQt5
import sys
from gui.janela_main import janela_main

textoparainput = ''
application = PyQt5.QtWidgets.QApplication(sys.argv)
janela = janela_main()
sys.exit(application.exec_())