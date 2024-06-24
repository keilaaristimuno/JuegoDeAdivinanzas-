import pygame
import constantes.colores as colores
import constantes.rectangulos as rectangulos
import fuentes.fuentes as fuentes
from funciones import *
from constantes.botones import *

pygame.init()

def mostrar_inicio(ventana, pos_mouse, lista_eventos, juego):
    
    #Creo el titulo
    titulo = "Adivina el logo"
    fuente_titulo = fuentes.FUENTE_75
    titulo = fuente_titulo.render(titulo, True, colores.AMARILLO)
    ventana.blit(titulo, centrar_txt(ventana.get_rect().centerx, 75, titulo))
    #Creo el boton de ingreso de texto
    btn_ent_txt.rect = centrar_rect(ventana.get_rect().centerx, 250, btn_ent_txt.rect)
    btn_ent_txt.dibujar_btn(ventana, 0, 3, pos_txt_y = - 50)
    btn_ent_txt.validar_escritura(pos_mouse,lista_eventos)
    #Creo el contorno del ingreso de texto
    btn_contorno_ent_txt.rect = btn_ent_txt.rect
    btn_contorno_ent_txt.dibujar_btn(ventana, 3, 3)
    # #Creo el boton de escritura
    # btn_escritura = clases.Boton(rectangulos.REC_IN_ESCRITURA, colores.BLANCO)
    # btn_escritura.rect = centrar_rect(btn_ent_txt.rect.centerx, btn_ent_txt.rect.centery, btn_escritura.rect)
    # if btn_ent_txt.escribiendo == True:
    #     btn_escritura.dibujar_btn(ventana, 0, 0)
    
    #Creo el boton de jugar
    btn_empezar.rect = centrar_rect(ventana.get_rect().centerx, ventana.get_rect().centery + 100, btn_empezar.rect)
    btn_empezar.dibujar_btn(ventana, 0, 5, 0, 0, pos_mouse)
    #Boton de configuraciones con hover
    btn_config.dibujar_btn(ventana, 0,5, pos_mouse = pos_mouse)
    #Valido si hizo click en jugar
    if btn_empezar.validar_click(lista_eventos) == True:
        juego.logeado = True

def mostrar_principal(ventana, jugador: dict, pos_mouse, lista_eventos, juego) -> None:
    
    #Creo los rectangulos necesarios en la pantalla
    #Boton de dificultad
    btn_dificultad.dibujar_btn(ventana,0, 5, pos_txt_y = -15)
    #Boton categoria banderas
    btn_cat_banderas.dibujar_btn(ventana, 0, 5, pos_img_y = -5)
    #Boton categoria comidas
    btn_cat_comidas.dibujar_btn(ventana, 0, 5,pos_img_y = -5)
    #Boton categoria clubes
    btn_cat_clubes.dibujar_btn(ventana, 0, 5,pos_img_y = -5)
    #Boton categoria autos
    btn_cat_autos.dibujar_btn(ventana, 0, 5,pos_img_y = -5)
    #Boton categoria tecnologia
    btn_cat_tecno.dibujar_btn(ventana, 0, 5,pos_img_y = -5)
    #Boton categoria
    btn_categoria.dibujar_btn(ventana,0,5)
    #Boton Jugar con hover
    btn_jugar.dibujar_btn(ventana, 0, 5, 0, 0, pos_mouse)
    #Boton nivel del jugador
    btn_nvl_jugador.dibujar_btn(ventana,0,5, pos_txt_y = -15)
    txt_num = fuentes.FUENTE_35.render(f"{jugador['nivel_exp']}",True, colores.NEGRO)
    ventana.blit(txt_num, (centrar_txt(rectangulos.REC_PP_NIVEL_EXP.centerx, rectangulos.REC_PP_NIVEL_EXP.centery + 10, txt_num)))
    #Boton barra de experiencia
    btn_exp_jugador.dibujar_btn(ventana,0,5, pos_txt_y = -15)
    experiencia = lambda exp_actual, exp_necesaria: str(exp_actual) +  "/" + str(exp_necesaria)
    txt_numero_exp = fuentes.FUENTE_35.render(f"{experiencia(jugador['puntaje_exp'][0], jugador['puntaje_exp'][1])}",
                                              True, colores.NEGRO)
    ventana.blit(txt_numero_exp, (centrar_txt(rectangulos.REC_PP_BARRA_EXP.centerx, rectangulos.REC_PP_BARRA_EXP.centery + 10,
                                              txt_numero_exp)))
    #Boton barra de monedas   
    btn_monedas.dibujar_btn(ventana, 0,5, pos_txt_y = - 15)
    txt_num_monedas = fuentes.FUENTE_35.render(f"{jugador['monedas']}",True, colores.BLANCO)
    ventana.blit(txt_num_monedas, (centrar_txt(rectangulos.REC_PP_BARRA_MONEDAS.centerx, 
                                               rectangulos.REC_PP_BARRA_MONEDAS.centery + 10, txt_num_monedas)))
    #Boton barra de tienda de tienda con hover
    btn_gemas.dibujar_btn(ventana,0,5, pos_txt_y = -15,pos_mouse = pos_mouse)
    txt_num_gemas = fuentes.FUENTE_35.render(f"{jugador['gemas']}",True, colores.BLANCO)
    ventana.blit(txt_num_gemas, (centrar_txt(rectangulos.REC_PP_BARRA_GEMAS.centerx, rectangulos.REC_PP_BARRA_GEMAS.centery + 10, 
                                             txt_num_gemas)))
    #Boton de Como jugar con hover
    btn_como_jugar.dibujar_btn(ventana, 0,5, pos_mouse = pos_mouse)
    #Boton de configuraciones con hover
    btn_config.dibujar_btn(ventana, 0,5, pos_mouse = pos_mouse)
   
    #Imagen del personaje
    imagen_personaje = pygame.image.load("imagenes\P_Principal\personaje.png")
    imagen_personaje = pygame.transform.scale(imagen_personaje, (150,180))
    ventana.blit(imagen_personaje, (320,200))
   
    #Textos y botones de dificultades
    #Boton de dificultad Fácil con hover
    btn_dif_f.dibujar_btn(ventana, 0,5,pos_mouse = pos_mouse)
    #Boton de dificultad Normal con hover
    btn_dif_n.dibujar_btn(ventana, 0,5,pos_mouse = pos_mouse)
    #Boton de dificultad Difícil con hover
    btn_dif_d.dibujar_btn(ventana, 0,5,pos_mouse = pos_mouse)
    
    if btn_dif_f.validar_click(lista_eventos) == True or juego.dificultad == "f":
        juego.dificultad = "f"
    if btn_dif_n.validar_click(lista_eventos) == True:
        juego.dificultad = "n"
    if btn_dif_d.validar_click(lista_eventos) == True:
        juego.dificultad = "d" 
    match juego.dificultad:
        
        case "f":
            btn_dif_f.color = btn_dif_f.hover
            btn_dif_n.color = btn_dif_n.aux_color
            btn_dif_d.color = btn_dif_d.aux_color
        case "n":
            btn_dif_n.color = btn_dif_n.hover
            btn_dif_f.color = btn_dif_f.aux_color
            btn_dif_d.color = btn_dif_d.aux_color
        case "d":
            btn_dif_d.color = btn_dif_d.hover
            btn_dif_n.color = btn_dif_n.aux_color
            btn_dif_f.color = btn_dif_f.aux_color
        case _:
            btn_dif_f.color = btn_dif_f.hover
            btn_dif_n.color = btn_dif_n.aux_color
            btn_dif_d.color = btn_dif_d.aux_color
    
    #Valido si hizo click en jugar
    if btn_jugar.validar_click(lista_eventos) == True:
        juego.jugando = True
    
def mostrar_jugando(ventana, jugador: dict, pos_mouse) -> None:
    # Boton de pausa con hover
    btn_pausa.dibujar_btn(ventana, 0, 5, pos_mouse = pos_mouse)

    #Imagen vidas
    imagen_vidas = pygame.image.load("imagenes\P_Jugando\Vida.png")
    imagen_vidas = pygame.transform.scale(imagen_vidas, (30,30))

    # Número de vidas
    num_vidas = 5

    # Posición inicial y separación entre vidas
    posicion_inicial = (50, 5)
    separacion = 20

    # Dibujar las vidas
    for i in range(num_vidas):
        ventana.blit(imagen_vidas, (posicion_inicial[0] + i * separacion, posicion_inicial[1]))

#Imagen del personaje
    imagen_personaje = pygame.image.load("imagenes\P_Principal\personaje.png")
    imagen_personaje = pygame.transform.scale(imagen_personaje, (100,180))
    ventana.blit(imagen_personaje, (100, 85))

#Fonde de pantalla para las respuestas
    imagen_fondo = pygame.image.load("imagenes\P_Jugando\Fondo_respuestas.jpg")
    imagen_fondo = pygame.transform.scale(imagen_fondo, (1000,320))
    ventana.blit(imagen_fondo, (0, 265))

#Rectangulo de respuestas:
    btn_respuesta_1.dibujar_btn(ventana, 0, 5, pos_mouse= pos_mouse )
    btn_respuesta_2.dibujar_btn(ventana, 0, 5, pos_mouse= pos_mouse)
    btn_respuesta_3.dibujar_btn(ventana, 0, 5, pos_mouse= pos_mouse)
    btn_respuesta_4.dibujar_btn(ventana, 0, 5, pos_mouse= pos_mouse )

# Fondo de la imagen que debe contestar
    pygame.draw.rect(ventana, colores.BLANCO, (rectangulos.REC_BANDERAS),0,5)
    # btn_bandera.dibujar_btn(ventana, 0, 5) Cuando tengamos el json

# Cantidad de monedas y tiempo:

    btn_cant_monedas.dibujar_btn(ventana, 0, 0, -30, 0)
    txt_cant_monedas = fuentes.FUENTE_25.render(f"{jugador['monedas']}", True, colores.BLANCO)
    ventana.blit(txt_cant_monedas, (centrar_txt(rectangulos.REC_PJ_MONEDAS.centerx + 23, rectangulos.REC_PJ_MONEDAS.centery, txt_cant_monedas )))
    
    btn_cant_tiempo.dibujar_btn(ventana, 0, 0, -30, -2)
    txt_cant_tiempo = fuentes.FUENTE_25.render(f"{jugador['tiempo']}", True, colores.BLANCO)
    ventana.blit(txt_cant_tiempo, (centrar_txt(rectangulos.REC_PJ_TIEMPO.centerx +23 , rectangulos.REC_PJ_TIEMPO.centery, txt_cant_tiempo )))


# Nivel que se encuentra
    txt_nivel_banderas = fuentes.FUENTE_25.render(f"Banderas: Nivel {jugador['nivel_exp']}",True, colores.BLANCO)
    ventana.blit(txt_nivel_banderas, (centrar_txt(rectangulos.REC_NIVEL_BANDERAS.centerx, rectangulos.REC_NIVEL_BANDERAS.centery + 10, 
                                             txt_nivel_banderas)))


