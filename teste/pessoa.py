class pessoa():

    def __init__(self, nome: str) -> None:
        self.nome = nome

    def __repr__(self):
        return f'Meu nome é {self.nome}'