from models.personaje.personaje import Personaje


class Sanador(Personaje):
    def __init__(self, hp, mp, st, pos_x, pos_y, h, ruta_imagen: str):
        super().__init__(hp, mp, st, pos_x, pos_y, h, ruta_imagen)

    def izquierda(self):
        pass

    def derecha(self):
        pass

    def saltar(self):
        pass

    def golpear(self, rectangulo_enemigo, key_pressed: bool):
        if self.rec_personaje.colliderect(rectangulo_enemigo):
            self.colision_actual = self.rec_personaje.colliderect(rectangulo_enemigo)
            if self.colision_anterior != self.colision_actual and key_pressed:
                self.colision_anterior = self.colision_actual
                return self.st
        else:
            self.colision_anterior = False
            self.colision_actual = False
            return 0

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
        if cantidad_recibida != 0:
            print(f"Recibi {cantidad_recibida} de daño")
