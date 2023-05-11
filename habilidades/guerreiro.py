from interface import InterfaceGuerreiro
from typing import Type

class Guerreiro:
    def __init__(self, personagem: Type[InterfaceGuerreiro]):
        self.personagem = personagem

    def lutar(self):
        self.personagem.comportamento()

    def nivel_guerreiro(self):
        self.personagem.level()