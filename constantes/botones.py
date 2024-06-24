import pygame
import clases
import fuentes.fuentes
import constantes.rectangulos as rectangulos
import fuentes.fuentes as fuentes
import constantes.colores as colores
from funciones import *


pygame.init()

#Botones de la pantalla de inicio
btn_ent_txt = clases.BotonEntradaTxt(rectangulos.REC_IN_ENT_TXT, colores.GRIS,colores.BLANCO, "Ingrese su usuario", 
                                    fuentes.FUENTE_40, colores.BLANCO)
btn_contorno_ent_txt = clases.Boton(btn_ent_txt.rect, colores.NEGRO)
btn_empezar = clases.BotonTxt(rectangulos.REC_IN_JUGAR, colores.OCRE, fuentes.FUENTE_55, "Empezar", colores.NEGRO,
                                colores.AMARILLO)
btn_config = clases.BotonImg(rectangulos.REC_PP_CONFIG, colores.OCRE,"imagenes\General\configuracion.png",(40,40), 
                                 colores.AMARILLO)

#Botones de la pantalla principal
btn_dificultad = clases.BotonTxt(rectangulos.REC_PP_DIFICULTAD, colores.VERDE_O, fuentes.FUENTE_30, "Dificultad", colores.NEGRO)
btn_cat_banderas = clases.BotonImg(rectangulos.REC_PP_CAT_BANDERAS, colores.VERDE,"imagenes\P_Principal\logo_bandera.png",(35,35))
btn_cat_comidas = clases.BotonImg(rectangulos.REC_PP_CAT_COMIDAS, colores.GRIS,"imagenes\P_Principal\logo_comida.png",(35,35))
btn_cat_clubes = clases.BotonImg(rectangulos.REC_PP_CAT_CLUBES, colores.GRIS,"imagenes\P_Principal\logo_clubes.png",(35,35))
btn_cat_autos = clases.BotonImg(rectangulos.REC_PP_CAT_AUTOS, colores.GRIS,"imagenes\P_Principal\logo_autos.png",(35,35))
btn_cat_tecno = clases.BotonImg(rectangulos.REC_PP_CAT_TECNO, colores.GRIS,"imagenes\P_Principal\logo_tecno.png",(35,35))
btn_categoria = clases.Boton(rectangulos.REC_PP_CATEGORIA, colores.VERDE)
btn_jugar = clases.BotonTxt(rectangulos.REC_PP_JUGAR, colores.OCRE, fuentes.FUENTE_55, "Jugar", colores.NEGRO,
                                colores.AMARILLO)
btn_nvl_jugador = clases.BotonTxt(rectangulos.REC_PP_NIVEL_EXP, colores.VERDE, fuentes.FUENTE_20, "Nivel", colores.NEGRO)
btn_exp_jugador = clases.BotonTxt(rectangulos.REC_PP_BARRA_EXP, colores.VERDE, fuentes.FUENTE_20, "Experiencia", colores.NEGRO)
btn_monedas = clases.BotonTxt(rectangulos.REC_PP_BARRA_MONEDAS, colores.BTN_MONEDAS, fuentes.FUENTE_20, "Monedas", 
                                  colores.BLANCO)
btn_gemas = clases.BotonTxt(rectangulos.REC_PP_BARRA_GEMAS, colores.VIOLETA_O, fuentes.FUENTE_20, "Tienda", 
                                  colores.AMARILLO, colores.VIOLETA)
btn_como_jugar = clases.BotonTxt(rectangulos.REC_PP_COMO_JUGAR, colores.OCRE, fuentes.FUENTE_35, "Como jugar", 
                                  colores.BLANCO, colores.AMARILLO) 
btn_config = clases.BotonImg(rectangulos.REC_PP_CONFIG, colores.OCRE,"imagenes\General\configuracion.png",(40,40), 
                                 colores.AMARILLO)
btn_dif_f = clases.BotonTxt(rectangulos.REC_PP_DIF_F, colores.VERDE, fuentes.FUENTE_25, "Fácil", 
                                  colores.NEGRO, colores.VERDE_C)
btn_dif_n = clases.BotonTxt(rectangulos.REC_PP_DIF_N, colores.NARANJA_O, fuentes.FUENTE_25, "Normal", 
                                  colores.NEGRO, colores.NARANJA_C)
btn_dif_d = clases.BotonTxt(rectangulos.REC_PP_DIF_D, colores.ROJO_O, fuentes.FUENTE_25, "Difícil", 
                                  colores.NEGRO, colores.ROJO_C)

#Botones del menu configuracion
menu_config = clases.Boton(rectangulos.REC_CONFIG, colores.BLANCO, False)
btn_cerrar_config = clases.BotonImg(rectangulos.REC_CERRAR_CONFIG, colores.ROJO_O, "imagenes\General\cruz_cerrar.png", (35,35), 
                                    colores.ROJO_C)