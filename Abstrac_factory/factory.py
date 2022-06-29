from abc import ABCMeta, abstractmethod
import pygame


class Factory(metaclass=ABCMeta):
    @abstractmethod
    def crear_jugador(self, eleccion: int):
        raise NotImplementedError

    @abstractmethod
    def crear_rival(self, eleccion: int):
        raise NotImplementedError

    @abstractmethod
    def operar_evento(self, event: pygame.event):
        raise NotImplementedError

    @abstractmethod
    def movimiento_de_jugadores(self):
        raise NotImplementedError

    @abstractmethod
    def daño(self):
        raise NotImplementedError
