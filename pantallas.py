import pygame
import colores
from funciones import *

pygame.init()

def mostrar_principal(ventana, nivel) -> None:
    
    personaje = pygame.draw.rect(ventana, (0,0,0), (300,180,150,200))
    btn_jugar = pygame.draw.rect(ventana, (0,0,0), (500,300,300,80))
    nivel_exp = pygame.draw.rect(ventana, (0,0,0), (10,15,50,50))
    barra_exp = pygame.draw.rect(ventana, (0,0,0), (70,15,150,50))
    barra_monedas = pygame.draw.rect(ventana, (0,0,0), (230,15,150,50))
    barra_gemas = pygame.draw.rect(ventana, (0,0,0), (390,15,150,50))
    
    fuente_jugar = pygame.font.SysFont("Serif", 45, True)
    txt_jugar = fuente_jugar.render("Jugar", False, colores.BLANCO)
    ventana.blit(txt_jugar, (centrar_txt(btn_jugar.centerx,btn_jugar.centery, txt_jugar)))
    #txt_nvl_exp = 
    fuente_barras = pygame.font.SysFont("Serif", 15, True)
    fuente_num_nvl_exp = pygame.font.SysFont("Serif", 25, True)
    txt_nvl_exp = fuente_barras.render("Nivel", False, colores.BLANCO)
    txt_num_nvl_exp = fuente_num_nvl_exp.render(f"{nivel}",False, colores.BLANCO)
    ventana.blit(txt_nvl_exp, (centrar_txt(nivel_exp.centerx, nivel_exp.centery - 15, txt_nvl_exp)))
    ventana.blit(txt_num_nvl_exp, (centrar_txt(nivel_exp.centerx, nivel_exp.centery + 10, txt_num_nvl_exp)))

    

