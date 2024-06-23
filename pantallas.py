import pygame
import colores
import rectangulos
import clases
import fuentes.fuentes as fuentes
from funciones import *

pygame.init()

def mostrar_inicio(ventana, pos_mouse):
    
    #Creo el titulo
    titulo = "Adivina el logo"
    fuente_titulo = fuentes.FUENTE_75
    titulo = fuente_titulo.render(titulo, True, colores.AMARILLO)
    ventana.blit(titulo, centrar_txt(ventana.get_rect().centerx, 75, titulo))
    #Creo el boton de ingreso de texto
    btn_ent_txt = clases.BotonEntradaTxt(rectangulos.REC_IN_ENT_TXT, colores.GRIS,colores.BLANCO, "Ingrese su usuario",
                                         fuentes.FUENTE_40, colores.BLANCO)
    btn_ent_txt.rect = centrar_rect(ventana.get_rect().centerx, 250, btn_ent_txt.rect)
    btn_ent_txt.dibujar_btn(ventana, 0, 3, pos_txt_y = - 50)
    #Creo el contorno del ingreso de texto
    btn_contorno_ent_txt = clases.Boton(btn_ent_txt.rect, colores.NEGRO)
    btn_contorno_ent_txt.dibujar_btn(ventana, 3, 3)
    #Creo el boton de jugar
    btn_jugar = clases.BotonTxt(rectangulos.REC_IN_JUGAR, colores.OCRE, fuentes.FUENTE_55, "Jugar", colores.NEGRO,
                                colores.AMARILLO)
    btn_jugar.rect = centrar_rect(ventana.get_rect().centerx, ventana.get_rect().centery + 100, btn_jugar.rect)
    btn_jugar.dibujar_btn(ventana, 0, 5, 0, 0, pos_mouse)
    #Boton de configuraciones con hover
    btn_config = clases.BotonImg(rectangulos.REC_PP_CONFIG, colores.OCRE,"imagenes\General\configuracion.png",(40,40), 
                                 colores.AMARILLO)
    btn_config.dibujar_btn(ventana, 0,5, pos_mouse = pos_mouse)

def mostrar_principal(ventana, jugador: dict, pos_mouse) -> None:
    
    #Creo los rectangulos necesarios en la pantalla
    #Boton de dificultad
    btn_dificultad = clases.BotonTxt(rectangulos.REC_PP_DIFICULTAD, colores.VERDE_O, fuentes.FUENTE_35, "Dificultad", colores.NEGRO)
    btn_dificultad.dibujar_btn(ventana,0, 5, pos_txt_y = -15)
    #Boton categoria banderas
    btn_cat_banderas = clases.BotonImg(rectangulos.REC_PP_CAT_BANDERAS, colores.VERDE,"imagenes\P_Principal\logo_bandera.png",(35,35))
    btn_cat_banderas.dibujar_btn(ventana, 0, 5, pos_img_y = -5)
    #Boton categoria comidas
    btn_cat_comidas = clases.BotonImg(rectangulos.REC_PP_CAT_COMIDAS, colores.GRIS,"imagenes\P_Principal\logo_comida.png",(35,35))
    btn_cat_comidas.dibujar_btn(ventana, 0, 5,pos_img_y = -5)
    #Boton categoria clubes
    btn_cat_clubes = clases.BotonImg(rectangulos.REC_PP_CAT_CLUBES, colores.GRIS,"imagenes\P_Principal\logo_clubes.png",(35,35))
    btn_cat_clubes.dibujar_btn(ventana, 0, 5,pos_img_y = -5)
    #Boton categoria autos
    btn_cat_autos = clases.BotonImg(rectangulos.REC_PP_CAT_AUTOS, colores.GRIS,"imagenes\P_Principal\logo_autos.png",(35,35))
    btn_cat_autos.dibujar_btn(ventana, 0, 5,pos_img_y = -5)
    #Boton categoria tecnologia
    btn_cat_tecno = clases.BotonImg(rectangulos.REC_PP_CAT_TECNO, colores.GRIS,"imagenes\P_Principal\logo_tecno.png",(35,35))
    btn_cat_tecno.dibujar_btn(ventana, 0, 5,pos_img_y = -5)
    #Boton categoria
    btn_categoria = clases.Boton(rectangulos.REC_PP_CATEGORIA, colores.VERDE)
    btn_categoria.dibujar_btn(ventana,0,5)
    #Boton Jugar con hover
    btn_jugar = clases.BotonTxt(rectangulos.REC_PP_JUGAR, colores.OCRE, fuentes.FUENTE_55, "Jugar", colores.NEGRO,
                                colores.AMARILLO)
    btn_jugar.dibujar_btn(ventana, 0, 5, 0, 0, pos_mouse)
    #Boton nivel del jugador
    btn_nvl_jugador = clases.BotonTxt(rectangulos.REC_PP_NIVEL_EXP, colores.VERDE, fuentes.FUENTE_20, "Nivel", colores.NEGRO)
    btn_nvl_jugador.dibujar_btn(ventana,0,5, pos_txt_y = -15)
    txt_num = fuentes.FUENTE_35.render(f"{jugador['nivel_exp']}",True, colores.NEGRO)
    ventana.blit(txt_num, (centrar_txt(rectangulos.REC_PP_NIVEL_EXP.centerx, rectangulos.REC_PP_NIVEL_EXP.centery + 10, txt_num)))
    #Boton barra de experiencia
    btn_exp_jugador = clases.BotonTxt(rectangulos.REC_PP_BARRA_EXP, colores.VERDE, fuentes.FUENTE_20, "Experiencia", colores.NEGRO)
    btn_exp_jugador.dibujar_btn(ventana,0,5, pos_txt_y = -15)
    experiencia = lambda exp_actual, exp_necesaria: str(exp_actual) +  "/" + str(exp_necesaria)
    txt_numero_exp = fuentes.FUENTE_35.render(f"{experiencia(jugador['puntaje_exp'][0], jugador['puntaje_exp'][1])}",
                                              True, colores.NEGRO)
    ventana.blit(txt_numero_exp, (centrar_txt(rectangulos.REC_PP_BARRA_EXP.centerx, rectangulos.REC_PP_BARRA_EXP.centery + 10,
                                              txt_numero_exp)))
    #Boton barra de monedas
    btn_monedas = clases.BotonTxt(rectangulos.REC_PP_BARRA_MONEDAS, colores.BTN_MONEDAS, fuentes.FUENTE_20, "Monedas", 
                                  colores.BLANCO)   
    btn_monedas.dibujar_btn(ventana, 0,5, pos_txt_y = - 15)
    txt_num_monedas = fuentes.FUENTE_35.render(f"{jugador['monedas']}",True, colores.BLANCO)
    ventana.blit(txt_num_monedas, (centrar_txt(rectangulos.REC_PP_BARRA_MONEDAS.centerx, 
                                               rectangulos.REC_PP_BARRA_MONEDAS.centery + 10, txt_num_monedas)))
    #Boton barra de tienda de tienda con hover
    btn_gemas = clases.BotonTxt(rectangulos.REC_PP_BARRA_GEMAS, colores.VIOLETA_O, fuentes.FUENTE_20, "Tienda", 
                                  colores.AMARILLO, colores.VIOLETA)  
    btn_gemas.dibujar_btn(ventana,0,5, pos_txt_y = -15,pos_mouse = pos_mouse)
    txt_num_gemas = fuentes.FUENTE_35.render(f"{jugador['gemas']}",True, colores.BLANCO)
    ventana.blit(txt_num_gemas, (centrar_txt(rectangulos.REC_PP_BARRA_GEMAS.centerx, rectangulos.REC_PP_BARRA_GEMAS.centery + 10, 
                                             txt_num_gemas)))
    #Boton de Como jugar con hover
    btn_como_jugar = clases.BotonTxt(rectangulos.REC_PP_COMO_JUGAR, colores.OCRE, fuentes.FUENTE_35, "Como jugar", 
                                  colores.BLANCO, colores.AMARILLO) 
    btn_como_jugar.dibujar_btn(ventana, 0,5, pos_mouse = pos_mouse)
    #Boton de configuraciones con hover
    btn_config = clases.BotonImg(rectangulos.REC_PP_CONFIG, colores.OCRE,"imagenes\General\configuracion.png",(40,40), 
                                 colores.AMARILLO)
    btn_config.dibujar_btn(ventana, 0,5, pos_mouse = pos_mouse)
   
    #Imagen del personaje
    imagen_personaje = pygame.image.load("imagenes\P_Principal\personaje.png")
    imagen_personaje = pygame.transform.scale(imagen_personaje, (150,180))
    ventana.blit(imagen_personaje, (320,200))
   
    #Textos y botones de dificultades
    #Boton de dificultad Fácil con hover
    btn_dif_f = clases.BotonTxt(rectangulos.REC_PP_DIF_F, colores.VERDE, fuentes.FUENTE_25, "Fácil", 
                                  colores.NEGRO, colores.VERDE_C)
    btn_dif_f.dibujar_btn(ventana, 0,5,pos_mouse = pos_mouse)
    #Boton de dificultad Normal con hover
    btn_dif_f = clases.BotonTxt(rectangulos.REC_PP_DIF_N, colores.NARANJA_O, fuentes.FUENTE_25, "Normal", 
                                  colores.NEGRO, colores.NARANJA_C)
    btn_dif_f.dibujar_btn(ventana, 0,5,pos_mouse = pos_mouse)
    #Boton de dificultad Difícil con hover
    btn_dif_f = clases.BotonTxt(rectangulos.REC_PP_DIF_D, colores.ROJO_O, fuentes.FUENTE_25, "Difícil", 
                                  colores.NEGRO, colores.ROJO_C)
    btn_dif_f.dibujar_btn(ventana, 0,5,pos_mouse = pos_mouse)

