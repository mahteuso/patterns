from interface import InterfaceGuerreiro
from typing import Type
class Guerreiro:
    def __init__(self, habilidade: Type[InterfaceGuerreiro]):
        self.habilidade = habilidade

    def lutar(self):
        self.habilidade.comportamento()


    def nivel(self):
        self.habilidade.nivel_atributo()