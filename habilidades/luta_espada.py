from interface import InterfaceGuerreiro
class Lutador(InterfaceGuerreiro):
    def __init__(self, nivel):
        self.nivel = nivel

    def comportamento(self):
        print('Usando espadas para lutar')

    def nivel_atributo(self):
        print(f'Usando espada de nível: {self.nivel}')