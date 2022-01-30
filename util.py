from Grupos import Grupo
from Dia import Dia
from Persona import Persona
import pygame
import random


def pintarMalla(ancho, alto, screen) -> None:
    # 2 verticales
    pygame.draw.line(screen, (0, 0, 0), (ancho / 3, 0), (ancho / 3, alto))
    pygame.draw.line(screen, (0, 0, 0), (2 * (ancho / 3), 0), (2 * (ancho / 3), alto))
    # 1 horizontal
    pygame.draw.line(screen, (0, 0, 0), (0, alto / 2), (ancho, alto / 2))


def crearGrupos(ancho, alto, enfermos, screen) -> list[Grupo]:
    grupos = []
    anchoG = 500
    altoG = 500
    columnas = 15
    filas = 15
    # grupo 1 0.33
    grupos.append(Grupo(1, 0.33*0.016, enfermos, columnas, filas, (0, 0), anchoG, altoG, screen))
    # grupo 2 0.58
    grupos.append(Grupo(2, 0.58*0.016, enfermos, columnas, filas, (ancho / 3, 0), anchoG, altoG, screen))
    # grupo 3 0.78
    grupos.append(Grupo(3, 0.78*0.016, enfermos, columnas, filas, (2 * (ancho / 3), 0), anchoG, altoG, screen))
    # grupo 4 0.89
    grupos.append(Grupo(4, 0.89*0.016, enfermos, columnas, filas, (0, alto / 2), anchoG, altoG, screen))
    # grupo 5 0.95
    grupos.append(Grupo(5, 0.95*0.016, enfermos, columnas, filas, (ancho / 3, alto / 2), anchoG, altoG, screen))
    # grupo 6 1
    grupos.append(Grupo(6, 1.00*0.016, enfermos, columnas, filas, (2 * (ancho / 3), alto / 2), anchoG, altoG, screen))
    return grupos


def crearPersonas(n) -> list[Persona]:
    personas = []
    for i in range(0, n):
        # cada persona se le asigana un número aleatorio de dosis
        personas.append(Persona(random.randrange(1, 4), i))
    return personas

