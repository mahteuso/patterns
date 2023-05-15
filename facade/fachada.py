from _insert import Inserir
from _select import Selecionar
from _delete import Deletar

class Fachada:

    def __init__(self):
        self._select = Selecionar()
        self._deleta = Deletar()
        self._insert = Inserir()


    def _select_one(self):
        return self._select.selecionar_um()

    def _select_many(self):
        return self._select.selecionar_varios()

    def _delete(self):
        return self._deleta._deletar()

    def _insert_one(self):
        return self._insert.inserir_um()