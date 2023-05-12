from interface import InterfaceGuerreiro

class Mago(InterfaceGuerreiro):

    def __init__(self, nivel: int) -> None:
        self.nivel = nivel

    def lutar(self):
        print(f'O Mago está usando o poder de cura')

    def level(self):
        print(f'O poder de cura tem o nível {self.nivel}')