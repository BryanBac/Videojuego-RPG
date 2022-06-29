import pygame
from sys import exit
from models.personaje.guerrero import Guerrero
from models.personaje.sanador import Sanador
from models.personaje.personaje import Personaje

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

#  Personajes
personaje1: Personaje = Guerrero(10, 10, 10, 150, 180, 180, "assets/guerrero.png")
personaje2: Personaje = Sanador(10, 10, 10, 656-150, 250, 180, "assets/sanador.png")

#  variables importantes
eleccion: int = 1
pantalla: int = 0


def pantalla_inicio(text_surface1, text_surface2, text_surface3):
    if eleccion == 1:
        text_surface2 = test_font.render("PC", False, "White")
        text_surface1 = test_font.render("PvP", False, "Cyan")
    elif eleccion == 2:
        text_surface1 = test_font.render("PvP", False, "White")
        text_surface3 = test_font.render("Salir", False, "White")
        text_surface2 = test_font.render("PC", False, "Cyan")
    elif eleccion == 3:
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


#  variables importantes para movimientos y colisiones
presion_izq: bool = False
presion_der: bool = False

presion_A: bool = False
presion_D: bool = False

z_pressed: bool = False
j_pressed: bool = False


while True:
    #  Movimiento
    if presion_A:
        personaje1.rec_personaje.left -= 4
        if personaje1.rec_personaje.left == -4:
            personaje1.rec_personaje.left = 0
    if presion_D:
        personaje1.rec_personaje.left += 4
        if personaje1.rec_personaje.left == 656:
            personaje1.rec_personaje.left = 652
    if presion_izq:
        personaje2.rec_personaje.left -= 4
        if personaje2.rec_personaje.left == -4:
            personaje2.rec_personaje.left = 0
    if presion_der:
        personaje2.rec_personaje.left += 4
        if personaje2.rec_personaje.left == 656:
            personaje2.rec_personaje.left = 652
    #  presión de teclas
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #  teclas levantadas
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                if pantalla == 1:
                    presion_izq = False
            if event.key == pygame.K_RIGHT:
                if pantalla == 1:
                    presion_der = False
            if event.key == pygame.K_a:
                if pantalla == 1:
                    presion_A = False
            if event.key == pygame.K_d:
                if pantalla == 1:
                    presion_D = False
            if event.key == pygame.K_z:
                if pantalla == 1:
                    z_pressed = False
                    personaje1.colision_anterior = False
            if event.key == pygame.K_j:
                if pantalla == 1:
                    j_pressed = False
                    personaje2.colision_anterior = False
        #  teclas oprimidas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if pantalla == 0:
                    eleccion -= 1
                    if eleccion == 0:
                        eleccion = 1
            if event.key == pygame.K_DOWN:
                if pantalla == 0:
                    eleccion += 1
                    if eleccion == 4:
                        eleccion = 3
            if event.key == pygame.K_LEFT:
                if pantalla == 1:
                    presion_izq = True
            if event.key == pygame.K_RIGHT:
                if pantalla == 1:
                    presion_der = True
            if event.key == pygame.K_a:
                if pantalla == 1:
                    presion_A = True
            if event.key == pygame.K_d:
                if pantalla == 1:
                    presion_D = True
            if event.key == pygame.K_z:
                if pantalla == 1:
                    z_pressed = True
            if event.key == pygame.K_j:
                if pantalla == 1:
                    j_pressed = True
            if event.key == pygame.K_RETURN:
                if pantalla == 0:
                    if eleccion == 1:
                        print("Iniciando partida...")
                        pantalla = 1
                        screen.fill("Black")
                    if eleccion == 2:
                        print("Cargando partida...")
                        pantalla = 2
                        screen.fill("Black")
                    if eleccion == 3:
                        print("Saliendo...")
                        exit()

    # golpes
    if personaje1.golpear(personaje2.get_rect(), z_pressed):
        personaje2.recibir_daño(personaje1.st)
        # si se quiere comprobar, den un print del hp
    if personaje2.golpear(personaje1.get_rect(), j_pressed):
        personaje1.recibir_daño(personaje2.st)

    # pantallas
    if pantalla == 0:
        pantalla_inicio(text_surface1, text_surface2, text_surface3)
    elif pantalla == 1:
        pantalla_pvp(fondo_surface, personaje1.get_imagen(), personaje1.get_rect(),
                     personaje2.get_imagen(), personaje2.get_rect())
    pygame.display.update()
    clock.tick(60)
