# A program to create visualizations of the data structures (linked lists, sequential lists, stacks, queues, binary search trees) 
# PROJETO DE ESTRUTURA DE DADOS
# Grupo: Guilherme Nogueira, Luciano Pereira, Pedro Lucas, Thais Melquiades, Vitoria Grisi
from utils import *

# Create a 1200x1200 sized screen
pygame.init()
running = True
altura = 720
largura = 1280
SCREEN = pygame.display.set_mode((largura, altura))
# load the buttons images 
button_sair = pygame.image.load('button_sair.png').convert_alpha()
button_teste = pygame.image.load('button_teste.png').convert_alpha()
button_lista = pygame.image.load('button_lista.png').convert_alpha()
button_fila = pygame.image.load('button_fila.png').convert_alpha()
button_pilha = pygame.image.load('button_pilha.png').convert_alpha()
button_arvore = pygame.image.load('button_arvore.png').convert_alpha()
pygame.display.set_caption('Projeto de Estrutura de Dados - MENU')

def listamenu():
    # Create a 1200x1200 sized screen
    pygame.init()
    running = True
    altura = 720
    largura = 1280
    lista = []
    texto = ''
    SCREEN = pygame.display.set_mode((largura, altura))
    # load the buttons images 
    button_sair = pygame.image.load('button_sair.png').convert_alpha()
    button_teste = pygame.image.load('button_teste.png').convert_alpha()
    pygame.display.set_caption('Projeto de Estrutura de Dados - LISTA')

    # create the buttons
    button1 = Button(button_teste, 100, 100, 200, 50)
    button2 = Button(button_sair, 1000, 600, 135, 60)

    # create the font
    font = getfont('arial', 20)
    SCREEN.fill(BLACK)

    # main loop
    while running:
        
        # draw the buttons
        button1.draw(SCREEN)
        button2.draw(SCREEN)
        
        draw_text('Digite o valor a ser inserido:', font, WHITE, SCREEN, 100, 300)
        # set a rectangle of lines to write the text
        inseridor = pygame.draw.rect(SCREEN, WHITE, (100, 350, 100, 30), 2)
        
        # type in the box
        



        


        # check events
        for event in pygame.event.get():
            # check if the event is the X button
            if event.type == pygame.QUIT:
                # if it is quit the game
                pygame.quit()
                sys.exit()
            # check if the event is a mouse button down
            if event.type == pygame.MOUSEBUTTONDOWN:
                # check if the mouse is over the button
                if button1.checkinput(event):
                    print('Button 1 was pressed')
                if button2.checkinput(event):
                    print('Button 2 was pressed')
                    running = False
                if inseridor.collidepoint(event.pos):
                    texto = ''
                    active = True

            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_RETURN:
                        texto = ''
                    elif event.key == pygame.K_BACKSPACE:
                        texto = texto[:-1]
                        clear_rect = pygame.draw.rect(SCREEN, BLACK, (100, 350, 100, 30))
                    #delete key
                    elif event.key == pygame.K_DELETE:
                        texto = ''
                        clear_rect = pygame.draw.rect(SCREEN, BLACK, (100, 350, 100, 30))                        
                    else:
                        texto += event.unicode
            # Render the current text
            txt_surface = font.render(texto, True, WHITE)
            # Resize the box if the text is too long
            width = max(200, txt_surface.get_width()+10)
            inseridor.w = width
            # Blit the text.
            SCREEN.blit(txt_surface, (inseridor.x+5, inseridor.y+5))
            pygame.display.flip()
            clock.tick(60)

            
            
                        

        # update the screen
        pygame.display.update()

def mainmenu():
    while running:
        
        SCREEN.fill((0, 0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = getfont('comicsansms', 50)
        draw_text('MENU', MENU_TEXT, WHITE, SCREEN, 550, 50)

        LISTA_BUTTON = Button(button_lista, 100, 100, 200, 70)
        FILA_BUTTON = Button(button_fila, 400, 100, 200, 70)
        PILHA_BUTTON = Button(button_pilha, 700, 100, 200, 70)
        ARVORE_BUTTON = Button(button_arvore, 1000, 100, 200, 70)
        SAIR_BUTTON = Button(button_sair, 1000, 500, 135, 60)

        SCREEN.blit(button_lista, (100, 100))
        SCREEN.blit(button_fila, (400, 100))
        SCREEN.blit(button_pilha, (700, 100))
        SCREEN.blit(button_arvore, (1000, 100))
        SCREEN.blit(button_sair, (1000, 500))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SAIR_BUTTON.checkinput(event):
                    pygame.quit()
                    sys.exit()
                if LISTA_BUTTON.checkinput(event):
                    listamenu()
                if PILHA_BUTTON.checkinput(event):
                    pilhamenu()
                if FILA_BUTTON.checkinput(event):
                    filamenu()
                if ARVORE_BUTTON.checkinput(event):
                    arvoremenu()

        pygame.display.update()
        
clock = pygame.time.Clock()
mainmenu()