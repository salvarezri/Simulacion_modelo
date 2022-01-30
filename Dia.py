import random
class Dia:
    def __init__(self, screen, grupos, personas):
        self.dia = 0
        self.screen = screen
        self.grupos = grupos
        self.personas = personas
        # estado = True ->  primerPaso
        # estado = False -> segundoPaso
        self.estado = 0

    def primerPaso(self):
        self.dia += 1
        self.reiniciarGrupos()
        # pinta la nueva disposición de los grupos
        for grupo in self.grupos:
            # revisa el estado del grupo
            grupo.verificarProp()
            grupo.pintarGrupo()
            # pinta las personas
            grupo.pintarPersonas()
        self.estado = False

    def segundoPaso(self):
        # simular contagios
        for grupo in self.grupos:
            grupo.revisarContagios(self.dia)
        # pinta las nuevas personas contagiadas
        for grupo in self.grupos:
            # revisa el estado del grupo
            grupo.verificarProp()
            grupo.pintarGrupo()
            # pinta las personas
            grupo.pintarPersonas()
        self.estado = True
        print(self.dia)

    def reiniciarGrupos(self):
        # pone en 0 todos los grupos
        for grupo in self.grupos:
            grupo.iniciarPersonas()
        # selecciona un grupo aleatorio para cada persona y la añade a este
        for persona in self.personas:
            self.grupos[random.randrange(0, 6)].agregarPersona(persona)
