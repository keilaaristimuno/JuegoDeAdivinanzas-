import pygame

pygame.init()

def obtener_pos_mouse(evento):
    if evento.type == pygame.MOUSEBUTTONDOWN:
            pos_mouse = pygame.mouse.get_pos()
            print(pos_mouse)