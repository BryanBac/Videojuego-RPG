from models.enemy.enemy import Enemy
from models.personaje.animacion import Animacion
import pygame
import random


class Mob1(Enemy):
    def __init__(self, hp, mp, st, pos_x, pos_y, h, ruta_imagen: str):
        super().__init__(hp, mp, st, pos_x, pos_y, h, ruta_imagen)
        # Comentarios de animación en la clase sanador
        self.__base: list[str] = ["Assets/Mago/Base.png"]
        self.__ataque: list[str] = ["Assets/Mago/Ataque.png"]
        self.__caminar: list[str] = [
            "Assets/Mago/Paso_derecha_1.png",
            "Assets/Mago/Paso_derecha_2.png",
            "Assets/Mago/Base.png",
            "Assets/Mago/Paso_izquierda_1.png",
            "Assets/Mago/Paso_izquierda_2.png",
            "Assets/Mago/Base.png",
        ]
        self.__saltar: list[str] = [
            "Assets/Mago/Salto_1.png",
            "Assets/Mago/Salto_2.png",
        ]
        self.ver_izq: bool = False
        self.saltando: bool = False
        self.golpe = pygame.mixer.Sound("Music/Hechizo2.mp3")
        self.__animacion = Animacion(self.__base, self.__caminar, self.__saltar, self.__ataque)

    # Invierte la imagen
    def invertir(self):
        if self.ver_izq:
            self.personaje = pygame.transform.flip(self.personaje, True, False)

    # Actualiza la imagen y rectangulo
    def animar(self):
        self.invertir()
        rectangulo = self.rec_personaje
        self.rec_personaje = self.personaje.get_rect(midbottom=rectangulo.midbottom)

    # Regresa la imagen a la base, ademas de reiniciar el índice
    def detener_animacion(self):
        self.personaje = self.__animacion.detener()
        self.animar()

    def saltar(self, txt: str):
        pass

    def izquierda(self):
        self.personaje = self.__animacion.caminar()
        self.ver_izq = True
        self.animar()
        self.rec_personaje.left -= 4
        if self.rec_personaje.left == -4:
            self.rec_personaje.left = 0

    def derecha(self):
        self.personaje = self.__animacion.caminar()
        self.ver_izq = False
        self.animar()
        self.rec_personaje.left += 4
        if self.rec_personaje.left == 656:
            self.rec_personaje.left = 652

    def avanzar(self, rectangulo_enemigo: pygame.rect):
        avanza: int = random.randint(0, 3)
        if avanza == 1:
            if rectangulo_enemigo.left < self.rec_personaje.left:
                self.izquierda()
                self.izquierda()
            if rectangulo_enemigo.left > self.rec_personaje.left:
                self.derecha()
                self.derecha()
            if self.rec_personaje.colliderect(rectangulo_enemigo):
                return True
            else:
                return False

    def atacar(self, rectangulo_enemigo: pygame.rect):
        self.colision_actual = self.rec_personaje.colliderect(rectangulo_enemigo)
        if self.colision_anterior != self.colision_actual:
            self.colision_anterior = self.colision_actual
            return True
        else:
            return False

    def recibir_daño(self, cantidad_recibida: int):
        self.hp = self.hp - cantidad_recibida

    def get_rect(self) -> float:
        return self.rec_personaje

    # La animación depende de otras condiciones para ocurrir, por eso esta en un método diferente
    def animar_ataque(self):
        self.personaje = self.__animacion.ataque()
        self.animar()
        self.golpe.play()

    def get_imagen(self):
        return self.personaje

# Función responsable de la animación de salto
    def aplicar_gravedad(self):
        self.gravedad += 1
        self.rec_personaje.y += self.gravedad
        if self.saltando:
            self.personaje = self.__animacion.saltar()
            self.animar()
        if self.rec_personaje.bottom >= 365:
            self.rec_personaje.bottom = 365
            self.gravedad = 0
            if self.saltando:
                self.detener_animacion()
                self.saltando = False
