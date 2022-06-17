import pygame
from sys import exit

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

#  imagenes -- Estas son de prueba para ver como funciona esto
fondo_surface = pygame.image.load("assets/fondo.jpg").convert()

piso_surface = pygame.image.load("assets/ch.png").convert()
piso_surface = pygame.transform.scale(piso_surface, (ancho, 50))

cuatro_brazos = pygame.image.load("assets/cuatrobrazos.png").convert_alpha()
cuatro_brazos = pygame.transform.scale(cuatro_brazos, (150, 100))
rec_cuatro_brazos = cuatro_brazos.get_rect(topright=(150, 250))

kevin11 = pygame.image.load("assets/kevin11.png").convert_alpha()
ancho_villano = 150
kevin11 = pygame.transform.scale(kevin11, (ancho_villano, 180))
rec_kevin11 = kevin11.get_rect(topright=(656-ancho_villano, 250))

#  variables importantes
eleccion: int = 1
pantalla: int = 0
colision_actual: bool = False
colision_anterior1: bool = False
colision_anterior2: bool = False


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
        rec_cuatro_brazos.left -= 4
        if rec_cuatro_brazos.left == -4:
            rec_cuatro_brazos.left = 0
    if presion_D:
        rec_cuatro_brazos.left += 4
        if rec_cuatro_brazos.left == 656:
            rec_cuatro_brazos.left = 652
    if presion_izq:
        rec_kevin11.left -= 4
        if rec_kevin11.left == -4:
            rec_kevin11.left = 0
    if presion_der:
        rec_kevin11.left += 4
        if rec_kevin11.left == 656:
            rec_kevin11.left = 652
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
            if event.key == pygame.K_j:
                if pantalla == 1:
                    j_pressed = False
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
    # colisiones -- me falta arreglar un error, hasta ahorita solo funciona un golpe y luego debe alejarse
    if rec_cuatro_brazos.colliderect(rec_kevin11):
        colision_actual = rec_cuatro_brazos.colliderect(rec_kevin11)
        if z_pressed:
            if colision_anterior1 != colision_actual:
                colision_anterior1 = colision_actual
                print("atacó jugador 1")
        if j_pressed:
            if colision_anterior2 != colision_actual:
                colision_anterior2 = colision_actual
                print("atacó jugador 2")
    else:
        colision_anterior = False
        colision_actual = False
    if pantalla == 0:
        pantalla_inicio(text_surface1, text_surface2, text_surface3)
    elif pantalla == 1:
        pantalla_pvp(fondo_surface, cuatro_brazos, rec_cuatro_brazos, kevin11, rec_kevin11)
    pygame.display.update()
    clock.tick(60)
