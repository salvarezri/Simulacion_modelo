import pygame
from Grupos import Grupo
from Persona import Persona
from  Dia import Dia
import util
import random


pygame.init()
ANCHO = 1500
ALTO = 1000
# Set up the drawing window
screen = pygame.display.set_mode([ANCHO, ALTO])
print(screen.get_size())


# para guardar enfermos
enfermos = []
# crear los grupos
grupos = util.crearGrupos(ANCHO, ALTO, enfermos, screen)
print(grupos)
# crear personas
personas = util.crearPersonas(400)
# empezar simulación
dia = Dia(screen, grupos, personas)
# Run until the user asks to quit
running = True
screen.fill((255, 255, 255))
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # click
            # fondo
            screen.fill((255, 255, 255))
            # malla para separar grupos
            util.pintarMalla(ANCHO, ALTO, screen)
            # continuar simulación
            if dia.estado:
                dia.primerPaso()
            else:
                dia.segundoPaso()
    # flip el display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()

