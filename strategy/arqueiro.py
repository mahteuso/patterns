from interface import InterfaceGuerreiro

class Arqueiro(InterfaceGuerreiro):

    def __init__(self, nivel: int) -> None:
        self.nivel = nivel

    def lutar(self):
        print(f'O Arqueiro está lançando flechas.')

    def level(self):
        print(f'O arco usado tem o nível {self.nivel}')
