from interface import InterfaceGuerreiro
from typing import Type

class Guerreiro:

    def __init__(self, guerreiro: Type[InterfaceGuerreiro]) -> None:
        self.guerreiro = guerreiro

    def lutar(self):
        self.guerreiro.lutar()

    def nivel(self):
        self.guerreiro.level()
