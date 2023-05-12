from interface import InterfaceObservador
class Observadores(InterfaceObservador):

    def __init__(self, nome):
        self.nome = nome


    def atualizar(self, mensagem):
        print(f'|{self.nome} recebeu| : {mensagem}')


