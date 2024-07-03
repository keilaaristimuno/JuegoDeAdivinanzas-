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
btn_ver_usuarios = clases.BotonTxt(rectangulos.REC_IN_VER_USUARIOS, colores.OCRE, fuentes.FUENTE_45, "Ver Usuarios",
                                    colores.NEGRO, colores.AMARILLO)
btn_config = clases.BotonImg(rectangulos.REC_PP_CONFIG, colores.OCRE,"imagenes\General\configuracion.png",(40,40), 
                                 colores.AMARILLO)

#Botones de la pantalla principal
btn_dificultad = clases.BotonTxt(rectangulos.REC_PP_DIFICULTAD, colores.VERDE_O, fuentes.FUENTE_25, "Dificultad", colores.NEGRO)
btn_cat_banderas = clases.BotonImg(rectangulos.REC_PP_CAT_BANDERAS, colores.VERDE,"imagenes\P_Principal\logo_bandera.png",(35,35))
btn_cat_comidas = clases.BotonImg(rectangulos.REC_PP_CAT_COMIDAS, colores.GRIS,"imagenes\P_Principal\logo_comida.png",(35,35), 
                                  colores.GRIS_C)
btn_cat_equipos = clases.BotonImg(rectangulos.REC_PP_CAT_EQUIPOS, colores.GRIS,"imagenes\P_Principal\logo_clubes.png",(35,35),
                                  colores.GRIS_C)
btn_cat_autos = clases.BotonImg(rectangulos.REC_PP_CAT_AUTOS, colores.GRIS,"imagenes\P_Principal\logo_autos.png",(35,35),
                                colores.GRIS_C)
btn_cat_tecno = clases.BotonImg(rectangulos.REC_PP_CAT_TECNO, colores.GRIS,"imagenes\P_Principal\logo_tecno.png",(35,35),
                                colores.GRIS_C)
btn_categoria = clases.Boton(rectangulos.REC_PP_CATEGORIA, colores.VERDE)
btn_jugar = clases.BotonTxt(rectangulos.REC_PP_JUGAR, colores.OCRE, fuentes.FUENTE_55, "Jugar", colores.NEGRO,
                                colores.AMARILLO)
btn_nvl_jugador = clases.BotonTxt(rectangulos.REC_PP_NIVEL_EXP, colores.VERDE, fuentes.FUENTE_20, "Nivel", colores.NEGRO)
btn_exp_jugador = clases.BotonTxt(rectangulos.REC_PP_BARRA_EXP, colores.VERDE, fuentes.FUENTE_20, "Experiencia", colores.NEGRO)
btn_monedas = clases.BotonTxt(rectangulos.REC_PP_BARRA_MONEDAS, colores.BTN_MONEDAS, fuentes.FUENTE_20, "Monedas", 
                                  colores.BLANCO)
btn_gemas = clases.BotonTxt(rectangulos.REC_PP_BARRA_GEMAS, colores.VIOLETA_O, fuentes.FUENTE_20, "Tienda", 
                                  colores.AMARILLO, colores.VIOLETA)
btn_como_jugar = clases.BotonTxt(rectangulos.REC_PP_COMO_JUGAR, colores.OCRE, fuentes.FUENTE_30, "Como jugar", 
                                  colores.BLANCO, colores.AMARILLO) 
btn_config = clases.BotonImg(rectangulos.REC_PP_CONFIG, colores.OCRE,"imagenes\General\configuracion.png",(40,40), 
                                 colores.AMARILLO)
btn_dif_f = clases.BotonTxt(rectangulos.REC_PP_DIF_F, colores.VERDE, fuentes.FUENTE_25, "Fácil", 
                                  colores.NEGRO, colores.VERDE_C)
btn_dif_n = clases.BotonTxt(rectangulos.REC_PP_DIF_N, colores.NARANJA_O, fuentes.FUENTE_25, "Normal", 
                                  colores.NEGRO, colores.NARANJA_C)
btn_dif_d = clases.BotonTxt(rectangulos.REC_PP_DIF_D, colores.ROJO_O, fuentes.FUENTE_25, "Difícil", 
                                  colores.NEGRO, colores.ROJO_C)

# botones pantalla jugando
btn_pausa = clases.BotonImg(rectangulos.REC_PJ_PAUSA, colores.NARANJA_C, "imagenes\P_Jugando\pausa.png", (25,25), colores.AMARILLO)
btn_rta_1 = clases.BotonTxt(rectangulos.REC_RESP_1, colores.AZUL_O, fuentes.FUENTE_35, "None", colores.BLANCO, colores.CELESTE)
btn_rta_2 = clases.BotonTxt(rectangulos.REC_RESP_2, colores.AZUL_O, fuentes.FUENTE_35, "None", colores.BLANCO, colores.CELESTE)
btn_rta_3 = clases.BotonTxt(rectangulos.REC_RESP_3, colores.AZUL_O, fuentes.FUENTE_35, "None", colores.BLANCO, colores.CELESTE)
btn_rta_4 = clases.BotonTxt(rectangulos.REC_RESP_4, colores.AZUL_O, fuentes.FUENTE_35, "None", colores.BLANCO, colores.CELESTE)
btn_bandera = clases.BotonImg(rectangulos.REC_BANDERAS,colores.NEGRO, "imagenes\General\icono.png", (100,100))
btn_fondo_bandera = clases.Boton(rectangulos.REC_FONDO_BANDERAS, colores.BLANCO)

btn_cant_monedas = clases.BotonImg(rectangulos.REC_PJ_MONEDAS, colores.NARANJA_C,"imagenes\P_Jugando\moneda.png",(25,25))
btn_cant_tiempo = clases.BotonImg(rectangulos.REC_PJ_TIEMPO, colores.NARANJA_C,"imagenes\P_Jugando\Reloj.png",(25,25))

btn_nivel_banderas = clases.BotonTxt(rectangulos.REC_NIVEL_BANDERAS, colores.BLANCO, fuentes.FUENTE_20, "Banderas: ", colores.NEGRO)

#Botones del menu configuracion
menu_config = clases.Boton(rectangulos.REC_MC_CONFIG, colores.AMARILLO, False)
marco_menu_config = clases.Boton(rectangulos.REC_MC_MARCO_CONFIG, colores.OCRE, False)
btn_cerrar_config = clases.BotonImg(rectangulos.REC_MC_CERRAR, colores.ROJO_O, "imagenes\General\cruz_cerrar.png", (35,35), 
                                    colores.ROJO_C)
btn_cerrar_config.rect = centrar_rect(menu_config.rect.centerx + 215, menu_config.rect.centery - 90, btn_cerrar_config.rect)

btn_sonido_icono = clases.BotonImg(rectangulos.REC_SONIDO_ICONO, colores.OCRE, "imagenes\General\sonidos_on.png",(25,25))
btn_sonido = clases.BotonTxt(rectangulos.REC_SONIDO, colores.VERDE_C,fuentes.FUENTE_25, "ON", colores.NEGRO)
btn_sonido.rect = centrar_rect(menu_config.rect.centerx, menu_config.rect.centery - 50, btn_sonido.rect)
btn_sonido_icono.rect = centrar_rect(btn_sonido.rect.centerx+70, btn_sonido.rect.centery, btn_sonido_icono.rect)

btn_musica_icono = clases.BotonImg(rectangulos.REC_MUSICA_ICONO, colores.OCRE, "imagenes\General\musica_on.png",(25,25))
btn_musica = clases.BotonTxt(rectangulos.REC_MUSICA, colores.VERDE_C,fuentes.FUENTE_25, "ON", colores.NEGRO)
btn_musica.rect = centrar_rect(menu_config.rect.centerx, menu_config.rect.centery + 50, btn_musica.rect)
btn_musica_icono.rect = centrar_rect(btn_musica.rect.centerx + 70, btn_musica.rect.centery, btn_musica_icono.rect)

#Botones del menu de ver jugadores
ventana_jugadores = clases.Boton(rectangulos.REC_VENTANA_JUGADORES, colores.AZUL_C, False)
marco_ventana_jugadores = clases.BotonTxt(rectangulos.REC_MARCO_VENTANA_JUGADORES, colores.CREMA, fuentes.FUENTE_40, "", 
                                         colores.NEGRO)
btn_sig_pag_jugadores = clases.BotonTxt(rectangulos.REC_SIG_PAG_JUGADORES, colores.OCRE,fuentes.FUENTE_45, ">", 
                                       colores.NEGRO, colores.AMARILLO)
btn_ant_pag_jugadores = clases.BotonTxt(rectangulos.REC_ANT_PAG_JUGADORES, colores.OCRE,fuentes.FUENTE_45, "<", 
                                       colores.NEGRO, colores.AMARILLO)
btn_cerrar_ver_jugadores = clases.BotonImg(rectangulos.REC_MC_CERRAR, colores.ROJO_O, "imagenes\General\cruz_cerrar.png", (35,35), 
                                    colores.ROJO_C)
#Botones del menu configuracion
menu_pausa = clases.Boton(rectangulos.REC_MP_PAUSA, colores.AMARILLO, False)
marco_menu_pausa = clases.Boton(rectangulos.REC_MP_MARCO_PAUSA, colores.OCRE, False)
btn_cerrar_pausa = clases.BotonImg(rectangulos.REC_MP_CERRAR, colores.ROJO_O, "imagenes\General\cruz_cerrar.png", (35,35), 
                                    colores.ROJO_C)
btn_cerrar_pausa.rect = centrar_rect(menu_pausa.rect.centerx + 215, menu_pausa.rect.centery - 140, btn_cerrar_pausa.rect)

btn_sonido_icono = clases.BotonImg(rectangulos.REC_SONIDO_ICONO, colores.OCRE, "imagenes\General\sonidos_on.png",(25,25))
btn_sonido = clases.BotonTxt(rectangulos.REC_SONIDO, colores.VERDE_C,fuentes.FUENTE_25, "ON", colores.NEGRO)
btn_sonido.rect = centrar_rect(menu_pausa.rect.centerx, menu_pausa.rect.centery - 100, btn_sonido.rect)
btn_sonido_icono.rect = centrar_rect(btn_sonido.rect.centerx+70, btn_sonido.rect.centery, btn_sonido_icono.rect)

btn_musica_icono = clases.BotonImg(rectangulos.REC_MUSICA_ICONO, colores.OCRE, "imagenes\General\musica_on.png",(25,25))
btn_musica = clases.BotonTxt(rectangulos.REC_MUSICA, colores.VERDE_C,fuentes.FUENTE_25, "ON", colores.NEGRO)
btn_musica.rect = centrar_rect(menu_pausa.rect.centerx, menu_pausa.rect.centery, btn_musica.rect)
btn_musica_icono.rect = centrar_rect(btn_musica.rect.centerx + 70, btn_musica.rect.centery, btn_musica_icono.rect)

btn_mp_menu_ppal = clases.BotonTxt(rectangulos.REC_MP_MENU_PPAL, colores.AZUL_C,fuentes.FUENTE_25, "Menu principal",
                                   colores.NEGRO, colores.CELESTE)
btn_mp_menu_ppal.rect = centrar_rect(menu_pausa.rect.centerx, menu_pausa.rect.centery + 100, btn_mp_menu_ppal.rect)

#Botones del menu como jugar
btn_cerrar_c_jugar = clases.BotonImg(rectangulos.REC_C_JUGAR_CERRAR, colores.ROJO_O, "imagenes\General\cruz_cerrar.png", (35,35), 
                                    colores.ROJO_C)
btn_explicacion_c_jugar = clases.BotonImg(rectangulos.REC_C_JUGAR_TEXTO, colores.CELESTE, "imagenes\P_Principal\Como_jugar.png", (360,480))

#Botones del menu de tienda:
btn_cerrar_tienda = clases.BotonImg(rectangulos.REC_TIENDA_CERRAR, colores.ROJO_O, "imagenes\General\cruz_cerrar.png", (35,35), 
                                    colores.ROJO_C)
btn_titulo_tienda = clases.BotonTxt(rectangulos.REC_TITULO_TIENDA, colores.NARANJA_C, fuentes.FUENTE_40, "PROXIMAMENTE ", colores.ROSA_C)
btn_candado_tienda = clases.BotonImg(rectangulos.REC_CANDADO_TIENDA, colores.NARANJA_C, "imagenes\General\candado_tienda.png", (90,90), 
                                    colores.OCRE)

