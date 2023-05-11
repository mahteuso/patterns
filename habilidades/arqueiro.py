from interface import InterfaceGuerreiro
class Arqueiro(InterfaceGuerreiro):

    def __int__(self, nivel: int) -> None:
        self.nivel = nivel

    def comportamento(self):
        print('Usando Arco e flechas para lutar')

    def nivel_atributo(self):
        print(f'Usando Arco de nível: {self.nivel}')