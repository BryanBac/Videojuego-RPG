from models.personaje.personaje import Personaje
from models.personaje.animacion import Animacion
import pygame


class Sanador(Personaje):
    def __init__(self, hp, mp, st, pos_x, pos_y, h, ruta_imagen: str):
        super().__init__(hp, mp, st, pos_x, pos_y, h, ruta_imagen)
        # Siempre se utilizan listas para no tener problema con la clase animar()
        self.__base: list[str] = ["Assets/Sanador/Base.png"]
        self.__ataque: list[str] = ["Assets/Sanador/Ataque.png"]
        self.__caminar: list[str] = [
            "Assets/Sanador/Paso_derecha.png",
            "Assets/Sanador/Base.png",
            "Assets/Sanador/Paso_izquierda.png",
            "Assets/Sanador/Base.png",
        ]
        self.__saltar: list[str] = [
            "Assets/Sanador/Salto_1.png",
            "Assets/Sanador/Salto_2.png",
        ]
        self.ver_izq: bool = False  # Invierte la imagen para que vea a la izquierda
        self.saltando: bool = False  # Evita múltiples saltos
        self.golpe = pygame.mixer.Sound("Music/Curacion.mp3")
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

    # La animación depende de otras condiciones para ocurrir, por eso esta en un método diferente
    def animar_ataque(self):
        self.personaje = self.__animacion.ataque()
        self.animar()
        self.golpe.play()

    def izquierda(self):
        self.personaje = self.__animacion.caminar()
        self.ver_izq = True
        self.animar()
        self.rec_personaje.left -= 4
        if self.rec_personaje.left < 0:
            self.rec_personaje.left = 0

    def derecha(self):
        self.personaje = self.__animacion.caminar()
        self.ver_izq = False
        self.animar()
        self.rec_personaje.left += 4
        if self.rec_personaje.left > 656:
            self.rec_personaje.left = 656

    # Solo afecta la gravedad e indica que el jugador está saltando para evitar múltiples saltos
    def saltar(self):
        if not self.saltando:
            self.gravedad -= 18
            self.saltando = True

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

    def golpear(self, rectangulo_enemigo, key_pressed: bool) -> bool:
        if self.rec_personaje.colliderect(rectangulo_enemigo):
            self.colision_actual = self.rec_personaje.colliderect(rectangulo_enemigo)
            if self.colision_anterior != self.colision_actual and key_pressed:
                self.colision_anterior = self.colision_actual
                return True
        else:
            self.colision_anterior = False
            self.colision_actual = False
            return False

    def super_ataque(self) -> float:
        pass

    def correr(self):
        pass

    def get_imagen(self):
        return self.personaje

    def get_rect(self) -> float:
        return self.rec_personaje

    def revivir(self):
        pass

    def recibir_daño(self, cantidad_recibida: int):
        self.hp = self.hp - cantidad_recibida
