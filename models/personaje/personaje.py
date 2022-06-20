from abc import ABCMeta, abstractmethod


class Personaje(metaclass=ABCMeta):
    @abstractmethod
    def izquierda(self):
        raise NotImplementedError

    @abstractmethod
    def derecha(self):
        raise NotImplementedError

    @abstractmethod
    def saltar(self):
        raise NotImplementedError

    @abstractmethod
    def golpear(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def super_ataque(self) -> float:
        raise NotImplementedError
