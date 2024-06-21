import pygame
import colores
from funciones import *

pygame.init()

def mostrar_principal(ventana, nivel, experiencia, monedas, gemas) -> None:
    
    personaje = pygame.draw.rect(ventana, (0,0,0), (300,180,150,200))
    btn_jugar = pygame.draw.rect(ventana, (0,0,0), (500,300,300,80))
    nivel_exp = pygame.draw.rect(ventana, (0,0,0), (10,15,50,50))
    barra_exp = pygame.draw.rect(ventana, (0,0,0), (70,15,150,50))
    barra_monedas = pygame.draw.rect(ventana, (0,0,0), (230,15,150,50))
    barra_gemas = pygame.draw.rect(ventana, (0,0,0), (390,15,150,50))
    
    fuente_jugar = pygame.font.SysFont("Serif", 45, True)
    txt_jugar = fuente_jugar.render("Jugar", False, colores.BLANCO)
    ventana.blit(txt_jugar, (centrar_txt(btn_jugar.centerx,btn_jugar.centery, txt_jugar)))


#nivel
    fuente_barras = pygame.font.SysFont("Serif", 15, True)
    fuente_num_nvl_exp = pygame.font.SysFont("Serif", 25, True)
    txt_nvl_exp = fuente_barras.render("Nivel", False, colores.BLANCO)
    txt_num = fuente_num_nvl_exp.render(f"{nivel}",False, colores.BLANCO)
    ventana.blit(txt_nvl_exp, (centrar_txt(nivel_exp.centerx, nivel_exp.centery - 15, txt_nvl_exp)))
    ventana.blit(txt_num, (centrar_txt(nivel_exp.centerx, nivel_exp.centery + 10, txt_num)))

#experiencia
    txt_barra_exp = fuente_barras.render("Experiencia", False, colores.BLANCO)
    ventana.blit(txt_barra_exp, (centrar_txt(barra_exp.centerx, barra_exp.centery - 15, txt_barra_exp)))
    txt_numero_exp = fuente_num_nvl_exp.render(f"{experiencia}",False, colores.BLANCO)
    ventana.blit(txt_numero_exp, (centrar_txt(barra_exp.centerx - 25, barra_exp.centery + 10, txt_num)))
#Monedas
    txt_barra_monedas = fuente_barras.render("Monedas", False, colores.BLANCO)
    ventana.blit(txt_barra_monedas, (centrar_txt(barra_monedas.centerx, barra_monedas.centery - 15, txt_barra_monedas)))
    txt_num_monedas = fuente_num_nvl_exp.render(f"{monedas}",False, colores.BLANCO)
    ventana.blit(txt_num_monedas, (centrar_txt(barra_monedas.centerx - 15, barra_monedas.centery + 10, txt_num)))

# Gemas
    txt_barra_gemas = fuente_barras.render("Gemas", False, colores.BLANCO)
    ventana.blit(txt_barra_gemas, (centrar_txt(barra_gemas.centerx, barra_gemas.centery - 15, txt_barra_gemas)))
    txt_num_gemas = fuente_num_nvl_exp.render(f"{gemas}",False, colores.BLANCO)
    ventana.blit(txt_num_gemas, (centrar_txt(barra_gemas.centerx, barra_gemas.centery + 10, txt_num)))