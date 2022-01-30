import pygame
from Persona import Persona


class Grupo:
    def __init__(self, tipo, contagio, enfermos, columnas, filas, pInicial, ancho, alto, screen=None):
        """
        :param tipo: int
        :param contagio: float
        :param columnas: int
        :param filas: int
        :param pInicial: tuple(x,y)
        :param ancho: int
        :param alto: int
        """
        self._tipo = tipo
        self._contagio = contagio
        # lista que guarda enfermos
        self.enfermos = enfermos
        # matriz que guarda personas en el  grupo
        self.personas = []
        # marcador que indica donde se va a ubicar la próxima persona [columna,fila]
        self.posPersonas = [0, 0]
        # variables para Geometría y montaje de la simulación
        # contexto para poder pintar personas
        self.screen = screen
        # columnas del grupo
        self.columnas = columnas
        # filas del grupo
        self.filas = filas
        # punto sup izq del cuadro
        self.pInicial = pInicial
        # ancho del cuadro
        self.ancho = ancho
        # alto del cuadro
        self.alto = alto
        # desplazamientos para ubicar la malla donde se ubican las personas
        self.dx = (ancho / columnas) / 2
        self.dy = (alto / columnas) / 2
        # radio de las personas
        self.radio = self.calcRadio()
        # se rellena la matriz de personas con None según las filas y columnas
        self.iniciarPersonas()
        # overflow indica si el grupo está lleno
        self.overflow = False
        # fuente para texto
        self.fuente = pygame.font.Font(None, 20)

    def iniciarPersonas(self) -> None:
        self.personas = []
        self.posPersonas = [0, 0]
        for i in range(0, self.columnas):
            # crea las filas
            aux = []
            for j in range(0, self.filas):
                # crea las columnas
                aux.append(None)
            self.personas.append(aux)

    def agregarPersona(self, persona) -> None:
        # revisa si hay espacio para otra persona
        if not (self.personas[self.filas - 1][self.columnas - 1] is None):
            print("overflow")
            return None
        # guarda la persona según el indicador posPersona
        self.personas[self.posPersonas[1]][self.posPersonas[0]] = persona
        # Actualiza el indicador posPersona para la siguiente persona que entre al grupo
        self.posPersonas[0] += 1
        if self.posPersonas[0] > self.columnas - 1:
            self.posPersonas[0] = 0
            self.posPersonas[1] += 1

    def revisarContagios(self, dia):
        # se recorre el arreglo de izq. a der y de arriba a abajo
        for y in range(0, len(self.personas)):
            for x in range(0, len(self.personas[0])):
                # comprueba si hay persona
                if not (self.personas[y][x] is None):
                    # calcula si la persona se contagió
                    if self.personas[y][x].calcularContagio(self._contagio, dia):
                        # si la persona se contagió la agrega a la lista de contagios
                        self.enfermos.append(self.personas[y][x])

    """
    PINTAR
    """

    def calcRadio(self) -> float:
        # calcula el radio de las persona en función de la  cantidad de filas y columnas de estas que hallan
        ancho = (self.ancho / self.columnas * 0.8) / 2
        alto = (self.alto / self.filas * 0.8) / 2
        if ancho < alto:
            return ancho
        else:
            return alto

    def pintarCirculo(self, centro, col, id) -> None:
        # color = 0(default) -> verde ; color = 1 -> rojo
        color = (0, 255, 0)
        if col == 1: color = (255, 0, 0)
        pygame.draw.circle(self.screen, color, centro, self.radio)
        # escribir el Id de la persona en negro
        texto = self.fuente.render(str(id), True, (0, 0, 0))
        # calcular posición de texto
        x = centro[0] - 10
        y = centro[1] - 5
        self.screen.blit(texto,(x,y))

    def pintarPersona(self, x, y, persona):
        # verifica si hay persona
        if persona is None: return

        # calcula el color y la posición donde va a estar ubicada la persona
        # posición : puntoInicial + desface + (posición * anchoCelda)
        centroX = self.pInicial[0] + self.dx + (x * (self.ancho / self.columnas))
        centroY = self.pInicial[1] + self.dy + (y * (self.alto / self.filas))
        # color = 0 -> verde ; color = 1 -> rojo
        color = 0
        if persona.estado == 1:
            color = 1
        # pinta el circulo
        self.pintarCirculo((centroX, centroY), color, persona.idPersona)

    def pintarPersonas(self):
        # se recorre el arreglo de izq. a der y de arriba a abajo
        for y in range(0, len(self.personas)):
            for x in range(0, len(self.personas[0])):
                # verifica si hay persona
                if not (self.personas[y][x] is None):
                    # pinta la persona
                    self.pintarPersona(x, y, self.personas[y][x])

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def contagio(self):
        return self._contagio

    @contagio.setter
    def contagio(self, contagio):
        self._contagio = contagio

    def __str__(self):
        return f'Grupo Tipo: {self._tipo} \n Probabilidad de Contagio: {self._contagio}'
