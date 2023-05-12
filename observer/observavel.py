from interface import InterfaceObservador
from typing import Type


class Observavel:
    def __init__(self):
        self.observadores = []

    def adicionar_obs(self, observador: Type[InterfaceObservador]):
        self.observadores.append(observador)

    def notificar_obs(self, mensagem):
        for observador in self.observadores:
            observador.atualizar(mensagem)
