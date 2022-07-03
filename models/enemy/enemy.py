from abc import ABCMeta, abstractmethod
import pygame
from typing import Dict


class Enemy(metaclass=ABCMeta):
    def __init__(self, hp, mp, st, pos_x, pos_y, h, ruta_imagen: str):
        self.hp: int = hp
        self.__mp: int = mp
        self.st: int = st
        self.__pos_x: int = pos_x
        self.__pos_y: int = pos_y
        self.__h: int = h
        self.colision_actual = False
        self.colision_anterior = False
        self.__items: Dict[str, int] = {("Item 1", 2), ("Item 2", 3), ("Item 3", 4)}
        self.personaje = pygame.image.load(ruta_imagen).convert_alpha()
        self.rec_personaje = self.personaje.get_rect(
            midbottom=(self.__pos_x, self.__pos_y)
        )
        self.gravedad: int = 0
        self.saltando: bool = False

    @abstractmethod
    def avanzar(self, rectangulo_enemigo: pygame.rect):
        raise NotImplementedError

    @abstractmethod
    def atacar(self):
        raise NotImplementedError
