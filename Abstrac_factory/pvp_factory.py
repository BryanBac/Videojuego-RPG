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
        self.eleccion: int = 1
        self.pantalla: int = 0
        self.presion_izq: bool = False
        self.presion_der: bool = False
        self.presion_A: bool = False
        self.presion_D: bool = False
        self.z_pressed: bool = False
        self.j_pressed: bool = False

    def crear_jugador(self, eleccion: int):
        jugador1: Personaje
        if eleccion == 1:
            jugador1 = Sanador(10, 10, 10, 656-150, 250, 180, "assets/sanador.png")
        elif eleccion == 2:
            jugador1 = Guerrero(10, 10, 10, 150, 180, 180, "assets/guerrero.png")
        else:
            jugador1 = Mago(10, 10, 10, 656-150, 250, 180, "assets/sanador.png")  # imagen provisional
        self.jugadores.append(jugador1)

    def crear_rival(self, eleccion: int):
        jugador2: Personaje
        if eleccion == 1:
            jugador2 = Sanador(10, 10, 10, 656 - 150, 250, 180, "assets/sanador.png")
        elif eleccion == 2:
            jugador2 = Guerrero(10, 10, 10, 150, 180, 180, "assets/guerrero.png")
        else:
            jugador2 = Mago(10, 10, 10, 656 - 150, 250, 180, "assets/sanador.png")  # imagen provisional
        self.jugadores.append(jugador2)

    def operar_evento(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #  teclas levantadas
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                if self.pantalla == 1:
                    self.presion_izq = False
            if event.key == pygame.K_RIGHT:
                if self.pantalla == 1:
                    self.presion_der = False
            if event.key == pygame.K_a:
                if self.pantalla == 1:
                    self.presion_A = False
            if event.key == pygame.K_d:
                if self.pantalla == 1:
                    self.presion_D = False
            if event.key == pygame.K_z:
                if self.pantalla == 1:
                    self.z_pressed = False
                    self.jugadores[0].colision_anterior = False
            if event.key == pygame.K_j:
                if self.pantalla == 1:
                    self.j_pressed = False
                    self.jugadores[1].colision_anterior = False
        #  teclas oprimidas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if self.pantalla == 0:
                    self.eleccion -= 1
                    if self.eleccion == 0:
                        self.eleccion = 1
            if event.key == pygame.K_DOWN:
                if self.pantalla == 0:
                    self.eleccion += 1
                    if self.eleccion == 4:
                        self.eleccion = 3
            if event.key == pygame.K_LEFT:
                if self.pantalla == 1:
                    self.presion_izq = True
            if event.key == pygame.K_RIGHT:
                if self.pantalla == 1:
                    self.presion_der = True
            if event.key == pygame.K_a:
                if self.pantalla == 1:
                    self.presion_A = True
            if event.key == pygame.K_d:
                if self.pantalla == 1:
                    self.presion_D = True
            if event.key == pygame.K_z:
                if self.pantalla == 1:
                    self.z_pressed = True
            if event.key == pygame.K_j:
                if self.pantalla == 1:
                    self.j_pressed = True
            if event.key == pygame.K_RETURN:
                if self.pantalla == 0:
                    if self.eleccion == 1:
                        print("Iniciando partida...")
                        self.pantalla = 1
                    if self.eleccion == 2:
                        print("Cargando partida...")
                        self.pantalla = 2
                    if self.eleccion == 3:
                        print("Saliendo...")
                        exit()
