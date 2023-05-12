from interface import InterfaceGuerreiro

class Cavaleiro(InterfaceGuerreiro):

    def __init__(self, nivel: int) -> None:
        self.nivel = nivel

    def lutar(self):
        print(f'O Cavaleiro está lutando com espadas')

    def level(self):
        print(f'A espada usada tem o nível {self.nivel}')

