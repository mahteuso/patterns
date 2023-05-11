from interface import InterfaceGuerreiro
class Curandeiro(InterfaceGuerreiro):
    def __init__(self, nivel: int) -> None:
        self.nivel = nivel

    def comportamento(self):
        print('Usando magia de cura')


    def nivel_atributo(self):
        print(f'Usando cura nível: {self.nivel}')
