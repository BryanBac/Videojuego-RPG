from abc import ABCMeta, abstractmethod
import pygame
from typing import Dict


class Personaje(metaclass=ABCMeta):
    def __init__(self, hp, mp, st, pos_x, pos_y, h, ruta_imagen: str):
        self.hp: int = hp
        self.__mp: int = mp
        self.st: int = st
        self.__pos_x: int = pos_x
        self.__pos_y: int = pos_y
        self.__h: int = h
        self.colision_actual = False
        self.colision_anterior = False
        self.__items: Dict[str, int] = {('Item 1', 2), ('Item 2', 3), ('Item 3', 4)}
        self.personaje = pygame.image.load(ruta_imagen).convert_alpha()
        self.personaje = pygame.transform.scale(self.personaje, (150, h))
        self.rec_personaje = self.personaje.get_rect(topright=(self.__pos_x, self.__pos_y))

    @abstractmethod
    def izquierda(self):
        pass

    @abstractmethod
    def get_imagen(self):
        pass

    @abstractmethod
    def get_rect(self) -> float:
        pass

    @abstractmethod
    def derecha(self):
        pass

    @abstractmethod
    def saltar(self):
        pass

    @abstractmethod
    def golpear(self, rectangulo_enemigo, key_pressed: bool) -> bool:
        pass

    @abstractmethod
    def super_ataque(self) -> float:
        pass

    @abstractmethod
    def correr(self):
        pass

    @abstractmethod
    def recibir_daño(self, cantidad_recibida: int):
        pass
