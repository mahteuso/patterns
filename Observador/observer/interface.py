from abc import ABC, abstractmethod


class InterfaceCanal(ABC):

    @abstractmethod
    def update(self, observador):
        ...
