from interface import InterfaceGuerreiro


class Lutador(InterfaceGuerreiro):
    def __init__(self, nivel: int) -> None:
        self.nivel = nivel

    def comportamento(self):
        print('Lutador usando Machado!')

    def level(self):
        print(f'Lutador usando Machado de nível: {self.nivel}')