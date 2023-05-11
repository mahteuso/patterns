from abc import ABC, abstractmethod

class InterfaceGuerreiro(ABC):
    @abstractmethod
    def comportamento(self):
        ...
    @abstractmethod
    def level(self):
        ...