from abc import ABC, abstractmethod


class InterfaceGuerreiro(ABC):

    @abstractmethod
    def lutar(self):
        ...

    def level(self):
        ...
