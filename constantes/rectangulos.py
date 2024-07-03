import pygame

pygame.init()
#Rectangulos pantalla de inicio
REC_IN_JUGAR = pygame.Rect(0,0,400,90)
REC_IN_VER_USUARIOS = pygame.Rect(0,0,300,90)
REC_IN_ENT_TXT = pygame.Rect(0,0, 300, 65)
REC_IN_ESCRITURA = pygame.Rect(0,0, 260, 45)
REC_IN_IMG = pygame.Rect(0,0,400,90)
#Rectangulos pantalla principal
REC_PP_DIFICULTAD = pygame.Rect(500,285,400,70)
REC_PP_CAT_BANDERAS = pygame.Rect(500,160,60,60)
REC_PP_CAT_COMIDAS = pygame.Rect(585,160,60,60)
REC_PP_CAT_EQUIPOS = pygame.Rect(670,160,60,60)
REC_PP_CAT_AUTOS = pygame.Rect(755,160,60,60)
REC_PP_CAT_TECNO = pygame.Rect(840,160,60,60)
REC_PP_CATEGORIA = pygame.Rect(500,210,400,80)
REC_PP_NIVEL_EXP = pygame.Rect(10,15,50,50)
REC_PP_BARRA_EXP = pygame.Rect(70,15,150,50)
REC_PP_BARRA_MONEDAS = pygame.Rect(287,15,150,50)
REC_PP_BARRA_GEMAS = pygame.Rect(504,15,150,50)
REC_PP_COMO_JUGAR = pygame.Rect(722,15,150,50)
REC_PP_CONFIG = pygame.Rect(940,15,50,50)
REC_PP_JUGAR = pygame.Rect(500,350,400,90)
REC_PP_DIF_F = pygame.Rect(540,320,90,25)
REC_PP_DIF_N = pygame.Rect(650,320,95,25)
REC_PP_DIF_D = pygame.Rect(765,320,95,25)
#Rectangulos menu ver jugadores
REC_VENTANA_JUGADORES = pygame.Rect(250,75,550,450)
REC_MARCO_VENTANA_JUGADORES = pygame.Rect(250,75,500,400)
REC_SIG_PAG_JUGADORES = pygame.Rect(150,150,50,50)
REC_ANT_PAG_JUGADORES = pygame.Rect(150,50,50,50)

#Rectangulos pantalla jugando
REC_PJ_PAUSA = pygame.Rect(10,5,30,30)
REC_RESP_1 = pygame.Rect(56, 280, 390, 90)
REC_RESP_2 = pygame.Rect(56, 390, 390, 90)
REC_RESP_3 = pygame.Rect(555, 280, 390, 90)
REC_RESP_4 = pygame.Rect(555, 390, 390, 90)
REC_FONDO_BANDERAS = pygame.Rect(305,60, 390,195)
REC_BANDERAS = pygame.Rect(305,60, 210,140)

REC_PJ_MONEDAS = pygame.Rect(890, 0, 100, 30 )
REC_PJ_TIEMPO = pygame.Rect(890, 30, 100, 30 )

REC_NIVEL_BANDERAS = pygame.Rect(450,10,100,30)


#Rectangulo menu de configuracion
REC_MC_CONFIG = pygame.Rect(250,75,500,250)
REC_MC_MARCO_CONFIG = pygame.Rect(250,75,500,250)
REC_MC_CERRAR = pygame.Rect(0,0,40,40)
REC_SONIDO_ICONO = pygame.Rect(0,0,50,50)
REC_SONIDO = pygame.Rect(0,0,175,50)
REC_MUSICA_ICONO = pygame.Rect(0,0,50,50)
REC_MUSICA = pygame.Rect(0,0,175,50)

#Rectangulo menu de pausa
REC_MP_PAUSA = pygame.Rect(250,75,500,350)
REC_MP_MARCO_PAUSA = pygame.Rect(250,75,500,350)
REC_MP_CERRAR = pygame.Rect(0,0,40,40)
REC_MP_MENU_PPAL = pygame.Rect(0,0,175,50)

#Rectangulos opcion como jugar
REC_C_JUGAR_CERRAR = pygame.Rect(630,15,40,40)
REC_C_JUGAR_TEXTO = pygame.Rect(500,250,0,0)

# Rectangulos Menu de tiendas:
REC_MENU_TIENDA = pygame.Rect(250,100,0,0)
REC_TIENDA_CERRAR = pygame.Rect(950,20,40,40)
REC_TITULO_TIENDA = pygame.Rect(510,350,0,0)
REC_CANDADO_TIENDA = pygame.Rect(500,270,0,0)