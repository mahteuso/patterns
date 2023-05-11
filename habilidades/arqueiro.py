from interface import InterfaceGuerreiro


class Arqueiro(InterfaceGuerreiro):
    def __init__(self, nivel: int) -> None:
        self.nivel = nivel

    def comportamento(self):
        print('Arqueiro lançando flechas!')

    def level(self):
        print(f'Arqueiro usando Arco de nível: {self.nivel}')