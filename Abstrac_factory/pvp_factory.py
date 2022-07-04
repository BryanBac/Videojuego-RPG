from Abstrac_factory.factory import Factory
from models.personaje.personaje import Personaje
from models.personaje.sanador import Sanador
from models.personaje.guerrero import Guerrero
from models.personaje.mago import Mago
from typing import List
import pygame
from sys import exit


class PvpFactory(Factory):
    def __init__(self):
        self.jugadores: List[Personaje] = []
        self.presion_izq: bool = False
        self.presion_der: bool = False
        self.presion_A: bool = False
        self.presion_D: bool = False
        self.z_pressed: bool = False
        self.j_pressed: bool = False
        self.presion_arriba: bool = False
        self.presion_W: bool = False
        self.personajes_creados: bool = False
        self.daños: List[int] = []

    def crear_jugador(self, eleccion: int):
        jugador1: Personaje
        if eleccion == 1:
            jugador1 = Sanador(200, 10, 10, 150, 365, 180, "Assets/Sanador/Base.png")
        elif eleccion == 2:
            jugador1 = Guerrero(200, 10, 10, 150, 365, 180, "Assets/Caballero/Base.png")
        else:
            jugador1 = Mago(200, 10, 10, 150, 365, 180, "Assets/Mago/Base.png")
        self.jugadores.append(jugador1)
        self.daños.append(self.jugadores[0].hp)

    def crear_rival(self, eleccion: int):
        jugador2: Personaje
        if eleccion == 1:
            jugador2 = Sanador(200, 10, 10, 656, 365, 180, "Assets/Sanador/Base.png")
        elif eleccion == 2:
            jugador2 = Guerrero(200, 10, 10, 656, 365, 180, "Assets/Caballero/Base.png")
        else:
            jugador2 = Mago(200, 10, 10, 656, 365, 180, "Assets/Mago/Base.png")
        self.jugadores.append(jugador2)
        self.daños.append(self.jugadores[1].hp)

    def operar_evento(self, event: pygame.event):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #  teclas levantadas
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.presion_izq = False
                self.jugadores[1].detener_animacion()
            if event.key == pygame.K_RIGHT:
                self.presion_der = False
                self.jugadores[1].detener_animacion()
            if event.key == pygame.K_a:
                self.presion_A = False
                self.jugadores[0].detener_animacion()
            if event.key == pygame.K_d:
                self.presion_D = False
                self.jugadores[0].detener_animacion()
            if event.key == pygame.K_z:
                self.z_pressed = False
                self.jugadores[0].detener_animacion()
                self.jugadores[0].colision_anterior = False
            if event.key == pygame.K_j:
                self.j_pressed = False
                self.jugadores[1].detener_animacion()
                self.jugadores[1].colision_anterior = False

        #  teclas oprimidas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.presion_izq = True
            if event.key == pygame.K_RIGHT:
                self.presion_der = True
            if event.key == pygame.K_UP:
                self.presion_arriba = True
            if event.key == pygame.K_w:
                self.presion_W = True
            if event.key == pygame.K_a:
                self.presion_A = True
            if event.key == pygame.K_d:
                self.presion_D = True
            if event.key == pygame.K_z:
                self.z_pressed = True
            if event.key == pygame.K_j:
                self.j_pressed = True

    def movimiento_de_jugadores(self):
        self.jugadores[0].aplicar_gravedad()
        self.jugadores[1].aplicar_gravedad()
        if self.presion_A:
            self.jugadores[0].izquierda()
        if self.presion_D:
            self.jugadores[0].derecha()
        if self.presion_W:
            self.jugadores[0].saltar()
            self.presion_W = False
        if self.presion_izq:
            self.jugadores[1].izquierda()
        if self.presion_der:
            self.jugadores[1].derecha()
        if self.presion_arriba:
            self.jugadores[1].saltar()
            self.presion_arriba = False

    def daño(self):
        if self.jugadores[0].golpear(self.jugadores[1].get_rect(), self.z_pressed):
            self.jugadores[1].recibir_daño(self.jugadores[0].st)
            self.jugadores[0].animar_ataque()
            self.daños[0] = self.jugadores[1].hp
        if self.jugadores[1].golpear(self.jugadores[0].get_rect(), self.j_pressed):
            self.jugadores[0].recibir_daño(self.jugadores[1].st)
            self.jugadores[1].animar_ataque()
            self.daños[1] = self.jugadores[0].hp
        return self.daños
