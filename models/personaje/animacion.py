import pygame


class Animacion:
    def __init__(self, base, caminar_lista, saltar_lista, ataque_lista):
        self.base: list[str] = base
        self.caminar_lista: list[str] = caminar_lista
        self.saltar_lista: list[str] = saltar_lista
        self.ataque_lista: list[str] = ataque_lista
        self.movimiento_camina: float = 0  # Apuntador de imagen para animación al caminar
        self.movimiento_salta: float = 0  # Apuntador de imagen para animación al saltar
        self.movimiento_ataque: float = 0  # Apuntador de imagen para animación al atacar
        self.animacion: list[str] = base  # Selecciona la animación a reproducir
        self.contador: float = 0  # Apuntador de la animación
        self.jugador = pygame.image.load(self.base[0]).convert_alpha()

    def __animar(self, animacion, indice):
        if animacion == self.movimiento_camina:
            self.movimiento_salta = 0
            self.movimiento_ataque = 0
        elif animacion == self.movimiento_ataque:
            self.movimiento_camina = 0
            self.movimiento_salta = 0
        elif animacion == self.movimiento_salta:
            self.movimiento_camina = 0
            self.movimiento_ataque = 0

        self.jugador = pygame.image.load(
            animacion[int(indice)]
        ).convert_alpha()
        return self.jugador

    def caminar(self):
        self.movimiento_camina += 0.08
        if int(self.movimiento_camina) >= len(self.caminar_lista):
            self.movimiento_camina = 0
        return self.__animar(self.caminar_lista, self.movimiento_camina)

    def saltar(self):
        self.movimiento_salta += 0.2
        if int(self.movimiento_salta) >= len(self.saltar_lista):
            self.movimiento_salta = len(self.saltar_lista) - 1
        return self.__animar(self.saltar_lista, self.movimiento_salta)

    def detener(self):
        self.movimiento_ataque = 0
        self.movimiento_camina = 0
        self.movimiento_salta = 0
        return self.__animar(self.base, 0)

    def ataque(self):
        if int(self.movimiento_ataque) == 0:
            self.movimiento_ataque += 0.15
        else:
            self.movimiento_ataque += 0.02
        if int(self.movimiento_ataque) >= len(self.ataque_lista):
            self.movimiento_ataque = len(self.ataque_lista) - 1
        return self.__animar(self.ataque_lista, self.movimiento_ataque)
