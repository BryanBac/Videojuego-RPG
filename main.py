import pygame
from mecanicas.mechanical import Mechanical
from Abstrac_factory.factory import Factory
from Abstrac_factory.pvp_factory import PvpFactory
from Abstrac_factory.pc_factory import PCFactory
from mecanicas.seleccion import MechanicalSeleccion

pygame.init()
ancho = 800
alto = 400
screen = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Videojuego")
clock = pygame.time.Clock()
#  texto
test_font = pygame.font.SysFont("Curier", 29)
text_surface1 = test_font.render("PvP", False, "White")
text_surface2 = test_font.render("PC", False, "White")
text_surface3 = test_font.render("Salir", False, "White")
text_surface4 = test_font.render("Sanador", False, "White")
text_surface5 = test_font.render("Guerrero", False, "White")
text_surface6 = test_font.render("Mago", False, "White")

#  imagenes -- Estas son de prueba para ver como funciddddddddddddona esto
fondo_surface = pygame.image.load("Assets/Otros/Fondo_1.png").convert()
indice_fondo: int = 0

#  Fabricas y mecanicas de pantallas
fabrica: Factory = PvpFactory()
fabrica_pc: Factory = PCFactory()
mecanica: Mechanical = Mechanical()
mecanica_seleccion: MechanicalSeleccion = MechanicalSeleccion()
mecanica_seleccion_2: MechanicalSeleccion = MechanicalSeleccion()
personaje_1: int = 0
personaje_2: int = 0
creados: bool = False


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


def imagenes_seleccion(texto: str):
    fondo = pygame.image.load("Assets/Otros/Fondo_4.png").convert()
    screen.blit(fondo, (0, 0))
    letra = pygame.font.SysFont("Curier", 30)
    texto = letra.render(texto, True, (0, 170, 228))
    rectangulo_texto = texto.get_rect()
    rectangulo_texto.centerx = 400
    rectangulo_texto.centery = 45
    screen.blit(texto, rectangulo_texto)
    imagen_1 = pygame.image.load("Assets/Sanador/Ataque.png").convert_alpha()
    imagen_1 = pygame.transform.scale(imagen_1, (100, 100))
    rec_imagen_1 = imagen_1.get_rect(topright=(ancho / 3 + 200, alto / 3 - 60))
    imagen_2 = pygame.image.load("Assets/Caballero/Ataque.png").convert_alpha()
    imagen_2 = pygame.transform.scale(imagen_2, (100, 100))
    rec_imagen_2 = imagen_2.get_rect(topright=(ancho / 3 + 200, alto / 3 + 45))
    imagen_3 = pygame.image.load("Assets/Mago/Ataque.png").convert_alpha()
    imagen_3 = pygame.transform.scale(imagen_3, (100, 100))
    rec_imagen_3 = imagen_3.get_rect(topright=(ancho / 3 + 200, alto / 3 + 160))
    screen.blit(imagen_1, rec_imagen_1)
    screen.blit(imagen_2, rec_imagen_2)
    screen.blit(imagen_3, rec_imagen_3)


def pantalla_seleccion(texto: str):
    global text_surface4, text_surface5, text_surface6
    imagenes_seleccion(texto)
    if mecanica_seleccion.eleccion == 1:
        text_surface4 = test_font.render("Sanador", False, "Cyan")
        text_surface5 = test_font.render("Guerrero", False, "White")
        text_surface6 = test_font.render("Mago", False, "White")
    elif mecanica_seleccion.eleccion == 2:
        text_surface4 = test_font.render("Sanador", False, "White")
        text_surface5 = test_font.render("Guerrero", False, "Cyan")
        text_surface6 = test_font.render("Mago", False, "White")
    elif mecanica_seleccion.eleccion == 3:
        text_surface4 = test_font.render("Sanador", False, "White")
        text_surface5 = test_font.render("Guerrero", False, "White")
        text_surface6 = test_font.render("Mago", False, "Cyan")
    screen.blit(text_surface4, (ancho / 3, alto / 3 - 40))
    screen.blit(text_surface5, (ancho / 3, alto / 3 + 50))
    screen.blit(text_surface6, (ancho / 3, alto / 3 + 150))


def pantalla_seleccion_2(texto: str):
    global text_surface4, text_surface5, text_surface6
    imagenes_seleccion(texto)
    text_surface4 = test_font.render("Sanador", False, "Cyan")
    text_surface5 = test_font.render("Guerrero", False, "White")
    text_surface6 = test_font.render("Mago", False, "White")
    if mecanica_seleccion_2.eleccion == 1:
        text_surface4 = test_font.render("Sanador", False, "Cyan")
        text_surface5 = test_font.render("Guerrero", False, "White")
        text_surface6 = test_font.render("Mago", False, "White")
    elif mecanica_seleccion_2.eleccion == 2:
        text_surface4 = test_font.render("Sanador", False, "White")
        text_surface5 = test_font.render("Guerrero", False, "Cyan")
        text_surface6 = test_font.render("Mago", False, "White")
    elif mecanica_seleccion_2.eleccion == 3:
        text_surface4 = test_font.render("Sanador", False, "White")
        text_surface5 = test_font.render("Guerrero", False, "White")
        text_surface6 = test_font.render("Mago", False, "Cyan")
    screen.blit(text_surface4, (ancho / 3, alto / 3 - 40))
    screen.blit(text_surface5, (ancho / 3, alto / 3 + 50))
    screen.blit(text_surface6, (ancho / 3, alto / 3 + 150))


def pantalla_pvp(personaje, rect_personaje, villano, rec_villano):
    fondos = [
        "Assets/Otros/Fondo_1.png",
        "Assets/Otros/Fondo_2.png",
        "Assets/Otros/Fondo_3.png",
        "Assets/Otros/Fondo_2.png",
    ]
    fondo = pygame.image.load(fondos[int(indice_fondo)]).convert()
    screen.blit(fondo, (0, 0))
    screen.blit(personaje, rect_personaje)
    screen.blit(villano, rec_villano)


def modo1():
    global creados, indice_fondo
    # una vez terminada la partida, solo debemos cambiar el valor de mecanica.pantalla
    if creados:
        fabrica.daño()
        # impresion en pantalla
        indice_fondo += 0.02
        if int(indice_fondo) == 3:
            indice_fondo = 0
        pantalla_pvp(fabrica.jugadores[0].get_imagen(), fabrica.jugadores[0].get_rect(),
                     fabrica.jugadores[1].get_imagen(), fabrica.jugadores[1].get_rect())


def seleccionar_segundo():
    global personaje_2
    pantalla_seleccion_2('Selección personaje - Jugador 2')
    if mecanica_seleccion_2.personaje == 1:
        personaje_2 = 1
        modo1()
    elif mecanica_seleccion_2.personaje == 2:
        personaje_2 = 2
        modo1()
    elif mecanica_seleccion_2.personaje == 3:
        personaje_2 = 3
        modo1()


while True:
    #  Movimiento (funciona debido a que inicializada la fabrica, están en false)
    if mecanica.pantalla == 1:
        if creados:
            fabrica.movimiento_de_jugadores()
    if mecanica.pantalla == 2:
        if creados:
            fabrica_pc.movimiento_de_jugadores()
            fabrica_pc.ataque_enemigo()
    # manejo de eventos
    for event in pygame.event.get():
        mecanica.operar_evento(event)
        if mecanica.pantalla == 1:
            if personaje_1 == 0:
                mecanica_seleccion.operar_evento(event)
            elif personaje_1 != 0 and personaje_2 == 0:
                mecanica_seleccion_2.operar_evento(event)
            else:
                fabrica.operar_evento(event)
                if not fabrica.personajes_creados:
                    fabrica.crear_jugador(personaje_1)
                    fabrica.crear_rival(personaje_2)
                    creados = True
        if mecanica.pantalla == 2:
            if personaje_1 == 0:
                mecanica_seleccion.operar_evento(event)
            else:
                if not fabrica_pc.personajes_creados:
                    fabrica_pc.crear_jugador(personaje_1)
                    fabrica_pc.crear_rival()
                    creados = True
                fabrica_pc.operar_evento(event)
    # pantallas y acciones de impresion en ellas
    if mecanica.pantalla == 0:
        pantalla_inicio(text_surface1, text_surface2, text_surface3)
    elif mecanica.pantalla == 1:
        if not creados:
            pantalla_seleccion('Selección personaje - Jugador 1')
            if mecanica_seleccion.personaje == 1:
                personaje_1 = 1
                seleccionar_segundo()
            elif mecanica_seleccion.personaje == 2:
                personaje_1 = 2
                seleccionar_segundo()
            elif mecanica_seleccion.personaje == 3:
                personaje_1 = 3
                seleccionar_segundo()
        else:
            modo1()
    elif mecanica.pantalla == 2:
        if not creados:
            pantalla_seleccion('Selección personaje - Jugador 1')
            if mecanica_seleccion.personaje == 1:
                personaje_1 = 1
            elif mecanica_seleccion.personaje == 2:
                personaje_1 = 2
            elif mecanica_seleccion.personaje == 3:
                personaje_1 = 3
        else:
            fabrica_pc.daño()
            indice_fondo += 0.02
            if int(indice_fondo) == 3:
                indice_fondo = 0
            pantalla_pvp(fabrica_pc.jugadores[0].get_imagen(), fabrica_pc.jugadores[0].get_rect(),
                         fabrica_pc.jugadores[1].get_imagen(), fabrica_pc.jugadores[1].get_rect())
    pygame.display.update()
    clock.tick(60)
