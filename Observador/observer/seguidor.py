from interface import InterfaceCanal


class Seguidor(InterfaceCanal):

    def __init__(self, nome: str) -> None:
        self.nome = nome


    def update(self, observador):
        print(f'|{self.nome} recebeu| : {observador}')