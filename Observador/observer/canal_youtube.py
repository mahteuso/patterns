from interface import InterfaceCanal
from typing import Type


class CanalYoutube:

    def __init__(self):
        self.users = []

    def inscrever(self, user: Type[InterfaceCanal]):
        self.users.append(user)

    def desinscrever(self, user: Type[InterfaceCanal]):
        self.users.remove(user)

    def update(self, mensagem):
        for inscrito in self.users:
            inscrito.update(mensagem)

