from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def plotas(self):
        pass

    @abstractmethod
    def perimetras(self):
        pass
