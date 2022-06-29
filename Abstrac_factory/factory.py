from abc import ABCMeta, abstractmethod


class Factory(metaclass=ABCMeta):
    @abstractmethod
    def crear_jugador(self, eleccion: int):
        raise NotImplementedError

    @abstractmethod
    def crear_rival(self, eleccion: int):
        raise NotImplementedError

