from interface import InterfaceGuerreiro


class Mago(InterfaceGuerreiro):
    def __init__(self, nivel: int) -> None:
        self.nivel = nivel


    def comportamento(self):
        print('Mago usando magia!')

    def level(self):
        print(f'Mago usando cura nível: {self.nivel}')
