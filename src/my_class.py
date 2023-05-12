class FalarAlgo:
    def __init__(self, falar):
        self.falar = falar

    def fale(self):
        print(self.falar)

    def mudar_fala(self, nova_fala):
        self.falar = nova_fala