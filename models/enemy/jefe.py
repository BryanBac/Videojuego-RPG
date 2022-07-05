from models.enemy.enemy import Enemy
import pygame
import random


class Jefe(Enemy):
    def __init__(self, hp, mp, st, pos_x, pos_y, h, ruta_imagen: str):
        super().__init__(hp, mp, st, pos_x, pos_y, h, ruta_imagen)
        # Comentarios de animación en la clase sanador
        self.__base: list[str] = ["Assets/Enemigo/Base.png"]
        self.__ataque: list[str] = [
            "Assets/Enemigo/Ataque_1.png",
            "Assets/Enemigo/Ataque_2.png"
        ]
        self.__caminar: list[str] = [
            "Assets/Enemigo/Paso_derecha.png",
            "Assets/Enemigo/Base.png",
            "Assets/Enemigo/Paso_izquierda.png",
            "Assets/Enemigo/Base.png",
        ]
        self.__saltar: list[str] = [
            "Assets/Enemigo/Salto_1.png",
            "Assets/Enemigo/Salto_2.png",
        ]
        self.__indice: float = 0
        self.__animacion: list[str] = self.__base
        self.ver_izq: bool = False
        self.saltando: bool = False
        self.golpe = pygame.mixer.Sound("Music/Golpe2.mp3")

    # Invierte la imagen
    def invertir(self):
        if self.ver_izq:
            self.personaje = pygame.transform.flip(self.personaje, True, False)

    # Actualiza la imagen y rectangulo
    def animar(self):
        self.personaje = pygame.image.load(
            self.__animacion[int(self.__indice)]
        ).convert_alpha()
        self.invertir()
        rectangulo = self.rec_personaje
        self.rec_personaje = self.personaje.get_rect(midbottom=rectangulo.midbottom)

    # Regresa la imagen a la base, ademas de reiniciar el índice
    def detener_animacion(self):
        self.__animacion = self.__base
        self.__indice = 0
        self.animar()

    def saltar(self):
        if not self.saltando:
            self.gravedad -= 18
            self.saltando = True

    def izquierda(self):
        self.__animacion = self.__caminar
        self.__indice += 0.08
        if int(self.__indice) >= len(self.__caminar):
            self.__indice = 0
        self.ver_izq = True
        self.animar()
        self.rec_personaje.left -= 4
        if self.rec_personaje.left == -4:
            self.rec_personaje.left = 0

    def derecha(self):
        self.__animacion = self.__caminar
        self.__indice += 0.08
        if int(self.__indice) >= len(self.__caminar):
            self.__indice = 0
        self.ver_izq = False
        self.animar()
        self.rec_personaje.left += 4
        if self.rec_personaje.left == 656:
            self.rec_personaje.left = 652

    def avanzar(self, rectangulo_enemigo: pygame.rect):
        avanza: int = random.randint(0, 2)
        if avanza == 1:
            salto: int = random.randint(0, 1)
            if rectangulo_enemigo.left < self.rec_personaje.left:
                self.izquierda()
                if salto == 1:
                    self.saltar()
                self.izquierda()
            if rectangulo_enemigo.left > self.rec_personaje.left:
                self.derecha()
                if salto == 1:
                    self.saltar()
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
        self.__animacion = self.__ataque
        self.__indice += 0.04
        if int(self.__indice) >= len(self.__ataque):
            self.__indice = len(self.__ataque) - 1
        self.animar()
        self.golpe.play()

    def get_imagen(self):
        return self.personaje

# Función responsable de la animación de salto
    def aplicar_gravedad(self):
        self.gravedad += 1
        self.rec_personaje.y += self.gravedad
        if self.saltando:
            self.__animacion = self.__saltar
            self.__indice += 0.2
            if int(self.__indice) >= len(self.__saltar):
                self.__indice = len(self.__saltar) - 1
            self.animar()
        if self.rec_personaje.bottom >= 365:
            self.rec_personaje.bottom = 365
            self.gravedad = 0
            if self.saltando:
                self.detener_animacion()
                self.saltando = False
