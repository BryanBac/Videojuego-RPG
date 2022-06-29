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
    if mecanica.pantalla == 1:
        fabrica.movimiento_de_jugadores()
    # manejo de eventos
    for event in pygame.event.get():
        mecanica.operar_evento(event)
        if mecanica.pantalla == 1:
            # una vez terminada la partida, solo debemos cambiar el valor de mecanica.pantalla
            fabrica.operar_evento(event)
            if not fabrica.personajes_creados:
                fabrica.crear_jugador(1)
                fabrica.crear_rival(2)
    # pantallas y acciones de impresion en ellas
    if mecanica.pantalla == 0:
        pantalla_inicio(text_surface1, text_surface2, text_surface3)
    elif mecanica.pantalla == 1:
        fabrica.daño()
        # impresion en pantalla
        pantalla_pvp(fondo_surface, fabrica.jugadores[0].get_imagen(), fabrica.jugadores[0].get_rect(),
                     fabrica.jugadores[1].get_imagen(), fabrica.jugadores[1].get_rect())
    pygame.display.update()
    clock.tick(60)
