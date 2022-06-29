import pygame
from mecanicas.mechanical import Mechanical
from Abstrac_factory.factory import Factory
from Abstrac_factory.pvp_factory import PvpFactory

pygame.init()
ancho = 800
alto = 400
screen = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Inmersion Quest")
clock = pygame.time.Clock()
#  texto
test_font = pygame.font.Font(None, 20)
text_surface1 = test_font.render("PvP", False, "White")
text_surface2 = test_font.render("PC", False, "White")
text_surface3 = test_font.render("Salir", False, "White")

#  imagenes -- Estas son de prueba para ver como funciddddddddddddona esto
fondo_surface = pygame.image.load("assets/fondo.jpg").convert()
piso_surface = pygame.image.load("assets/ch.png").convert()
piso_surface = pygame.transform.scale(piso_surface, (ancho, 50))

#  Fabricas y mecanicas de pantallas
fabrica: Factory = PvpFactory()
mecanica: Mechanical = Mechanical()


def pantalla_inicio(text_surface1, text_surface2, text_surface3):
    if mecanica.eleccion == 1:
        text_surface2 = test_font.render("PC", False, "White")
        text_surface1 = test_font.render("PvP", False, "Cyan")
    elif mecanica.eleccion == 2:
        text_surface1 = test_font.render("PvP", False, "White")
        text_surface3 = test_font.render("Salir", False, "White")
        text_surface2 = test_font.render("PC", False, "Cyan")
    elif mecanica.eleccion == 3:
        text_surface2 = test_font.render("PC", False, "White")
        text_surface3 = test_font.render("Salir", False, "Cyan")
    screen.blit(text_surface1, (ancho / 3, alto / 3))
    screen.blit(text_surface2, (ancho / 3, alto / 3 + 50))
    screen.blit(text_surface3, (ancho / 3, alto / 3 + 100))


def pantalla_pvp(fondo, personaje, rect_personaje, villano, rec_villano):
    screen.blit(fondo, (0, 0))
    screen.blit(piso_surface, (0, 350))
    screen.blit(personaje, rect_personaje)
    screen.blit(villano, rec_villano)


while True:
    #  Movimiento (funciona debido a que inicializada la fabrica, están en false)
    if fabrica.presion_A:
        personaje1.rec_personaje.left -= 4
        if personaje1.rec_personaje.left == -4:
            personaje1.rec_personaje.left = 0
    if fabrica.presion_D:
        personaje1.rec_personaje.left += 4
        if personaje1.rec_personaje.left == 656:
            personaje1.rec_personaje.left = 652
    if fabrica.presion_izq:
        personaje2.rec_personaje.left -= 4
        if personaje2.rec_personaje.left == -4:
            personaje2.rec_personaje.left = 0
    if fabrica.presion_der:
        personaje2.rec_personaje.left += 4
        if personaje2.rec_personaje.left == 656:
            personaje2.rec_personaje.left = 652
    # manejo de eventos
    for event in pygame.event.get():
        mecanica.operar_evento(event)
        if mecanica.pantalla == 1:
            # una vez terminada la partida, solo debemos cambiar el valor de mecanica.pantalla
            fabrica.operar_evento(event)
            if not fabrica.personajes_creados:
                fabrica.crear_jugador(1)
                fabrica.crear_rival(2)
                personaje1 = fabrica.jugadores[0]
                personaje2 = fabrica.jugadores[1]
    # pantallas y acciones de impresion en ellas
    if mecanica.pantalla == 0:
        pantalla_inicio(text_surface1, text_surface2, text_surface3)
    elif mecanica.pantalla == 1:
        # golpes
        if personaje1.golpear(personaje2.get_rect(), fabrica.z_pressed):
            personaje2.recibir_daño(personaje1.st)
            print(f"P2 HP: {personaje2.hp}")
        if personaje2.golpear(personaje1.get_rect(), fabrica.j_pressed):
            personaje1.recibir_daño(personaje2.st)
            print(f"P1 HP: {personaje1.hp}")
        # impresion en pantalla
        pantalla_pvp(fondo_surface, personaje1.get_imagen(), personaje1.get_rect(),
                     personaje2.get_imagen(), personaje2.get_rect())
    pygame.display.update()
    clock.tick(60)
