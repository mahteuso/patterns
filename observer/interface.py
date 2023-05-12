from abc import ABC, abstractmethod

class InterfaceObservador(ABC):

    @abstractmethod
    def atualizar(self, mensagem):
        ...
