from Abstrac_factory.factory import Factory
from models.personaje.personaje import Personaje
from models.personaje.sanador import Sanador
from models.personaje.guerrero import Guerrero
from models.personaje.mago import Mago
from models.enemy.enemy import Enemy
from models.enemy.jefe import Jefe
from models.enemy.mob1 import Mob1
from typing import List
import pygame
import random
from sys import exit


class PCFactory(Factory):
    def __init__(self):
        self.jugadores: List[Personaje] = []
        self.presion_izq: bool = False
        self.presion_der: bool = False
        self.j_pressed: bool = False
        self.presion_arriba: bool = False
        self.personajes_creados: bool = False
        self.dañaron_jugador: bool = False
        self.personajes_creados: bool = False

    def crear_jugador(self, eleccion: int):
        jugador1: Personaje
        if eleccion == 1:
            jugador1 = Sanador(10, 10, 10, 150, 365, 180, "Assets/Sanador/Base.png")
        elif eleccion == 2:
            jugador1 = Guerrero(10, 10, 10, 150, 365, 180, "Assets/Caballero/Base.png")
        else:
            jugador1 = Mago(10, 10, 10, 150, 365, 180, "Assets/Mago/Base.png")
        self.jugadores.append(jugador1)

    def crear_rival(self):
        eleccion: int = random.randint(0, 1)
        jugador2: Enemy
        if eleccion == 1:
            jugador2 = Jefe(10, 10, 10, 656, 365, 180, "Assets/Enemigo/Base.png")
        else:
            jugador2 = Mob1(10, 10, 5, 656, 365, 180, "Assets/Mago/Base.png")
        self.jugadores.append(jugador2)

    def operar_evento(self, event: pygame.event):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #  teclas levantadas
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.presion_izq = False
                self.jugadores[0].detener_animacion()
            if event.key == pygame.K_RIGHT:
                self.presion_der = False
                self.jugadores[0].detener_animacion()
            if event.key == pygame.K_j:
                self.j_pressed = False
                self.jugadores[0].detener_animacion()
                self.jugadores[0].colision_anterior = False
        #  teclas oprimidas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.presion_izq = True
            if event.key == pygame.K_RIGHT:
                self.presion_der = True
            if event.key == pygame.K_UP:
                self.presion_arriba = True
            if event.key == pygame.K_j:
                self.j_pressed = True

    def movimiento_de_jugadores(self):
        self.jugadores[0].aplicar_gravedad()
        self.jugadores[1].aplicar_gravedad()
        if self.presion_izq:
            self.jugadores[0].izquierda()
        if self.presion_der:
            self.jugadores[0].derecha()
        if self.presion_arriba:
            self.jugadores[0].saltar()
            self.presion_arriba = False

    def ataque_enemigo(self):
        self.dañaron_jugador = self.jugadores[1].avanzar(self.jugadores[0].get_rect())

    def daño(self):
        if self.jugadores[0].golpear(self.jugadores[1].get_rect(), self.j_pressed):
            self.jugadores[1].recibir_daño(self.jugadores[0].st)
            self.jugadores[0].animar_ataque()
            print(f"P2 HP: {self.jugadores[1].hp}")
        if self.dañaron_jugador:
            self.dañaron_jugador = False
            daño: int = random.randint(0, 5)
            if daño == 0:
                self.jugadores[0].recibir_daño(self.jugadores[1].st)
                self.jugadores[1].animar_ataque()
                print(f"P1 HP: {self.jugadores[0].hp}")
