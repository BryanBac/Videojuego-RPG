from models.personaje.personaje import Personaje


class Guerrero(Personaje):
    def __init__(self, hp, mp, st, pos_x, pos_y):
        self.__hp: int = hp
        self.__mp: int = mp
        self.__st: int = st
        self.__pos_x: int = pos_x
        self.__pos_y: int = pos_y

    def izquierda(self):
        pass

    def derecha(self):
        pass

    def saltar(self):
        pass

    def golpear(self) -> float:
        pass

    def super_ataque(self) -> float:
        pass

    def correr(self):
        pass
