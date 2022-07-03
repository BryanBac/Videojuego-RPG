import pygame
from sys import exit


# maneja la mecanica de pantallas
class MechanicalSeleccion:
    def __init__(self):
        self.eleccion: int = 0
        self.personaje: int = 0

    def operar_evento(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #  teclas oprimidas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.eleccion -= 1
                if self.eleccion == 0:
                    self.eleccion = 1
            if event.key == pygame.K_DOWN:
                self.eleccion += 1
                if self.eleccion == 4:
                    self.eleccion = 3
            if event.key == pygame.K_RETURN:
                if self.eleccion == 1:
                    self.personaje = 1
                if self.eleccion == 2:
                    self.personaje = 2
                if self.eleccion == 3:
                    self.personaje = 3
