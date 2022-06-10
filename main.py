import pygame
from sys import exit


pygame.init()
ancho = 800
alto = 400
screen = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Inmersion Quest")
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 20)
text_surface1 = test_font.render("Nueva Partida", False, "White")
text_surface2 = test_font.render("Cargar Partida", False, "White")
text_surface3 = test_font.render("Salir", False, "White")

eleccion = 1
pantalla = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
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
    if pantalla == 0:
        if eleccion == 1:
            text_surface2 = test_font.render("Cargar Partida", False, "White")
            text_surface1 = test_font.render("Nueva Partida", False, "Cyan")
        elif eleccion == 2:
            text_surface1 = test_font.render("Nueva Partida", False, "White")
            text_surface3 = test_font.render("Salir", False, "White")
            text_surface2 = test_font.render("Cargar Partida", False, "Cyan")
        elif eleccion == 3:
            text_surface2 = test_font.render("Cargar Partida", False, "White")
            text_surface3 = test_font.render("Salir", False, "Cyan")
        screen.blit(text_surface1, (ancho/3, alto/3))
        screen.blit(text_surface2, (ancho/3, alto/3 + 50))
        screen.blit(text_surface3, (ancho/3, alto/3 + 100))
    pygame.display.update()
    clock.tick(60)
