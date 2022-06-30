import pygame
from sys import exit


# maneja la mecanica de pantallas
class Mechanical:
    def __init__(self):
        self.eleccion: int = 1
        self.pantalla: int = 0
        #  0 va a ser ningua, 1 pvp, 2 pvPC
        self.tipo_lucha: int = 0

    def operar_evento(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
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
