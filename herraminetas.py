import pygame

pygame.init()

def obtener_pos_click_izq_mouse(evento):
    if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            pos_mouse = pygame.mouse.get_pos()
            return pos_mouse
        
