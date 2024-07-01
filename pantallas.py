import pygame
import json
import constantes.colores as colores
import constantes.rectangulos as rectangulos
import fuentes.fuentes as fuentes
from funciones import *
from constantes.botones import *

pygame.init()
pygame.mixer.init()

def mostrar_inicio(ventana, pos_mouse, lista_eventos, juego, jugadores):
    fondo = pygame.image.load("imagenes\Fondos\Fondo_inicio.png")
    ventana.blit(fondo, (0,0))
    #Creo el titulo
    titulo = "Adivina el logo"
    fuente_titulo = fuentes.FUENTE_75
    titulo = fuente_titulo.render(titulo, True, colores.AMARILLO)
    ventana.blit(titulo, centrar_txt(ventana.get_rect().centerx, 75, titulo))
    #Creo el boton de ingreso de texto
    largo_txt = len(juego.nombre_jugador)
    btn_ent_txt.rect = centrar_rect(ventana.get_rect().centerx, 250, btn_ent_txt.rect)
    btn_ent_txt.dibujar_btn(ventana, 0, 3, pos_txt_y = - 50)
    btn_ent_txt.validar_escritura(pos_mouse,lista_eventos, juego.nombre_jugador)
    #Creo el contorno del ingreso de texto
    btn_contorno_ent_txt.rect = btn_ent_txt.rect
    btn_contorno_ent_txt.dibujar_btn(ventana, 3, 3)
    
    txt_ingreso = fuentes.FUENTE_30.render(juego.nombre_jugador, True,colores.NEGRO)  
    ventana.blit(txt_ingreso, centrar_txt(btn_ent_txt.rect.centerx, btn_ent_txt.rect.centery, txt_ingreso))
    
    #Creo el ingreso del texto del nombre del jugador
    for evento in lista_eventos:
        if evento.type == pygame.TEXTINPUT and btn_ent_txt.escribiendo == True:
            if  largo_txt < 10:
                juego.nombre_jugador += evento.text 
        elif evento.type == pygame.KEYDOWN:
            teclas = pygame.key.get_pressed()
            if evento.key == pygame.K_BACKSPACE:
                juego.nombre_jugador = juego.nombre_jugador[0:-1]
    
    #Creo el boton de jugar
    btn_empezar.rect = centrar_rect(ventana.get_rect().centerx, ventana.get_rect().centery + 100, btn_empezar.rect)
    btn_empezar.dibujar_btn(ventana, 0, 5, 0, 0, pos_mouse)
    #Boton de configuraciones con hover
    btn_config.dibujar_btn(ventana, 0,5, pos_mouse = pos_mouse)
    #Valido si hizo click en jugar
    if btn_empezar.validar_click(lista_eventos) == True or (btn_ent_txt.escribiendo == True and validar_enter(lista_eventos)):
        for jugador in jugadores:
            if juego.nombre_jugador.lower() == jugador["nombre"].lower():
                juego.logear(jugador)
            else:
                agregar_jugador = mostrar_jugador_no_encontrado()
            
    if btn_config.validar_click(lista_eventos) == True:
        if juego.pausado == False:
            juego.pausado = True
        else:
            juego.pausado = False
            
    if juego.pausado == True:
        mostrar_configuracion(ventana, lista_eventos, pos_mouse, juego)

def mostrar_principal(ventana, pos_mouse, lista_eventos, juego) -> None:
    
    juego.resetear_datos()
    if juego.pausado == False:
        fondo = pygame.image.load("imagenes\Fondos\Fondo_principal.png")
        ventana.blit(fondo, (0,0))
        #Creo los rectangulos necesarios en la pantalla
        #Boton de dificultad
        btn_dificultad.dibujar_btn(ventana,0, 5, pos_txt_y = -15)
        #Boton categoria banderas
        btn_cat_banderas.dibujar_btn(ventana, 0, 5, pos_img_y = -5, pos_mouse=pos_mouse)
        #Boton categoria comidas
        btn_cat_comidas.dibujar_btn(ventana, 0, 5,pos_img_y = -5, pos_mouse=pos_mouse)
        #Boton categoria clubes
        btn_cat_equipos.dibujar_btn(ventana, 0, 5,pos_img_y = -5, pos_mouse=pos_mouse)
        #Boton categoria autos
        btn_cat_autos.dibujar_btn(ventana, 0, 5,pos_img_y = -5, pos_mouse=pos_mouse)
        #Boton categoria tecnologia
        btn_cat_tecno.dibujar_btn(ventana, 0, 5,pos_img_y = -5, pos_mouse=pos_mouse)
        #Boton categoria
        btn_categoria.dibujar_btn(ventana,0,5)
        #Boton Jugar con hover
        btn_jugar.dibujar_btn(ventana, 0, 5, 0, 0, pos_mouse)
        #Boton nivel del jugador
        btn_nvl_jugador.dibujar_btn(ventana,0,5, pos_txt_y = -15)
        txt_num = fuentes.FUENTE_35.render(f"{juego.nivel_jugador}",True, colores.NEGRO)
        ventana.blit(txt_num, (centrar_txt(rectangulos.REC_PP_NIVEL_EXP.centerx, rectangulos.REC_PP_NIVEL_EXP.centery + 10, txt_num)))
        #Boton barra de experiencia
        btn_exp_jugador.dibujar_btn(ventana,0,5, pos_txt_y = -15)
        experiencia = lambda exp_actual, exp_necesaria: str(exp_actual) +  "/" + str(exp_necesaria)
        txt_numero_exp = fuentes.FUENTE_35.render(f"{experiencia(juego.exp_jugador[0], juego.exp_jugador[1])}",
                                                True, colores.NEGRO)
        ventana.blit(txt_numero_exp, (centrar_txt(rectangulos.REC_PP_BARRA_EXP.centerx, rectangulos.REC_PP_BARRA_EXP.centery + 10,
                                                txt_numero_exp)))
        #Boton barra de monedas   
        btn_monedas.dibujar_btn(ventana, 0,5, pos_txt_y = - 15)
        txt_num_monedas = fuentes.FUENTE_35.render(f"{juego.monedas}",True, colores.BLANCO)
        ventana.blit(txt_num_monedas, (centrar_txt(rectangulos.REC_PP_BARRA_MONEDAS.centerx, 
                                                rectangulos.REC_PP_BARRA_MONEDAS.centery + 10, txt_num_monedas)))
        #Boton barra de tienda de tienda con hover
        btn_gemas.dibujar_btn(ventana,0,5, pos_txt_y = -15,pos_mouse = pos_mouse)
        txt_num_gemas = fuentes.FUENTE_35.render(f"{juego.gemas}",True, colores.BLANCO)
        ventana.blit(txt_num_gemas, (centrar_txt(rectangulos.REC_PP_BARRA_GEMAS.centerx, rectangulos.REC_PP_BARRA_GEMAS.centery + 10, 
                                                txt_num_gemas)))
        if btn_gemas.validar_click(lista_eventos) == True:
            juego.pausado = True
            juego.mostrando_tienda = True 
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
        
        if btn_dif_f.validar_click(lista_eventos) == True:
            juego.dificultad = "f"
        if btn_dif_n.validar_click(lista_eventos) == True:
            juego.dificultad = "n"
        if btn_dif_d.validar_click(lista_eventos) == True:
            juego.dificultad = "d" 
            
        validar_dificultad_seleccionada(juego,  btn_dif_f, btn_dif_n, btn_dif_d)
        validar_categoria_seleccionada(juego, btn_cat_banderas, btn_cat_comidas, btn_cat_equipos)
        
        if btn_cat_banderas.validar_click(lista_eventos) == True:
            juego.categoria = "b"
            btn_jugar.color = colores.OCRE
            btn_jugar.hover = colores.AMARILLO
            btn_categoria.color = colores.VERDE
        if btn_cat_comidas.validar_click(lista_eventos) == True:
            if juego.nivel_jugador >= 5 and juego.monedas >= 50:
                btn_jugar.color = colores.OCRE
                btn_jugar.hover = colores.AMARILLO
                btn_categoria.color = colores.VERDE
            else:
                btn_jugar.color = colores.GRIS
                btn_jugar.hover = colores.GRIS_C
                btn_categoria.color = colores.GRIS_C
            juego.categoria = "c"
            
        if btn_cat_equipos.validar_click(lista_eventos) == True:
            if juego.nivel_jugador >= 10 and juego.monedas >= 100:
                btn_jugar.color = colores.OCRE
                btn_jugar.hover = colores.AMARILLO
                btn_categoria.color = colores.VERDE
            else:
                btn_jugar.color = colores.GRIS
                btn_jugar.hover = colores.GRIS_C
                btn_categoria.color = colores.GRIS_C
            juego.categoria = "e"
        
        if btn_jugar.color != colores.GRIS:
            #Valido si hizo click en jugar
            if btn_jugar.validar_click(lista_eventos) == True:
                juego.jugando = True
    
    if btn_config.validar_click(lista_eventos) == True:
        if juego.pausado == False:
            juego.pausado = True
            juego.mostrando_configuracion = True #probando
        else:
            juego.pausado = False
            
    #Valido si hizo click en el boton de como jugar
    if btn_como_jugar.validar_click(lista_eventos) == True:
        juego.pausado = True
        juego.mostrando_como_jugar = True #probando

    if juego.pausado == True:
        if juego.mostrando_configuracion:
            mostrar_configuracion(ventana, lista_eventos, pos_mouse, juego)
        elif juego.mostrando_como_jugar:
            mostrar_c_jugar(ventana, lista_eventos, pos_mouse, juego)
        elif juego.mostrando_tienda:
            mostrar_tienda(ventana,lista_eventos, pos_mouse,juego)

def mostrar_configuracion(ventana, lista_eventos, pos_mouse, juego):
    
    fondo_pausa = pygame.image.load("imagenes\Fondos\Fondo_pausa.png")
    ventana.blit(fondo_pausa, (0,0))
    if juego.musica == True:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()
    menu_config.dibujar_btn(ventana, 0, 3)
    marco_menu_config.dibujar_btn(ventana,10,3)
    btn_cerrar_config.dibujar_btn(ventana, 0, 5, pos_mouse = pos_mouse)
    
    btn_sonido.dibujar_btn(ventana, 0, 5)
    btn_sonido_icono.dibujar_btn(ventana, 0, 5)
    btn_musica.dibujar_btn(ventana, 0, 5)
    btn_musica_icono.dibujar_btn(ventana, 0, 5)

    #Verifico si se hizo click en cerrrar el menu de configuracion
    if btn_cerrar_config.validar_click(lista_eventos) == True:
        juego.pausado = False
        juego.mostrando_configuracion = False #probando
    #Verifico si se hizo click en el boton de sonido
    if btn_sonido_icono.validar_click(lista_eventos) == True:
        #Valido si el sonido esta encendido o apagado
        if juego.sonidos == True:
            #Cambio el estado de sonido a apagado
            btn_sonido_icono.actualizar_img_btn("imagenes\General\sonidos_off.png", (25,25))
            btn_sonido_icono.rect = centrar_rect(btn_sonido.rect.centerx - 70, btn_sonido.rect.centery, 
                                                    btn_sonido_icono.rect)
            btn_sonido.color = colores.ROJO_C
            btn_sonido.actualizar_txt("OFF")
            juego.sonidos = False
        else:
            #Cambio el estado de sonido a encendido
            btn_sonido_icono.actualizar_img_btn("imagenes\General\sonidos_on.png", (25,25))
            btn_sonido_icono.rect = centrar_rect(btn_sonido.rect.centerx + 70, btn_sonido.rect.centery, 
                                                    btn_sonido_icono.rect)
            btn_sonido.color = colores.VERDE_C
            btn_sonido.actualizar_txt("ON")
            juego.sonidos = True
    #Verifico si se hizo click en el boton de musica       
    if btn_musica_icono.validar_click(lista_eventos) == True:
        #Valido si la musica esta encendida o apagada
        if juego.musica == True:
            #Cambio el estado de musica a apagada
            btn_musica_icono.actualizar_img_btn("imagenes\General\musica_off.png", (25,25))
            btn_musica_icono.rect = centrar_rect(btn_musica.rect.centerx - 70, btn_musica.rect.centery, 
                                                    btn_musica_icono.rect)
            btn_musica.color = colores.ROJO_C
            btn_musica.actualizar_txt("OFF")
            juego.musica = False
        else:
            #Cambio el estado de musica a encendida
            btn_musica_icono.actualizar_img_btn("imagenes\General\musica_on.png", (25,25))
            btn_musica_icono.rect = centrar_rect(btn_musica.rect.centerx + 70, btn_musica.rect.centery, 
                                                    btn_musica_icono.rect)
            btn_musica.color = colores.VERDE_C
            btn_musica.actualizar_txt("ON")
            juego.musica = True

def mostrar_pausa(ventana, lista_eventos, pos_mouse, juego):
    
    fondo_pausa = pygame.image.load("imagenes\Fondos\Fondo_pausa.png")
    ventana.blit(fondo_pausa, (0,0))
    if juego.musica == True:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()
    menu_pausa.dibujar_btn(ventana, 0, 3)
    marco_menu_pausa.dibujar_btn(ventana,10,3)
    btn_cerrar_pausa.dibujar_btn(ventana, 0, 5, pos_mouse = pos_mouse)
    
    btn_sonido.dibujar_btn(ventana, 0, 5)
    btn_sonido_icono.dibujar_btn(ventana, 0, 5)
    btn_musica.dibujar_btn(ventana, 0, 5)
    btn_musica_icono.dibujar_btn(ventana, 0, 5)
    btn_mp_menu_ppal.dibujar_btn(ventana, 0, 5, pos_mouse = pos_mouse)

    #Verifico si se hizo click en cerrrar el menu de pausa
    if btn_cerrar_pausa.validar_click(lista_eventos) == True:
        juego.pausado = False
    if btn_mp_menu_ppal.validar_click(lista_eventos) == True:
        juego.pausado = False
        juego.jugando = False
    #Verifico si se hizo click en el boton de sonido
    if btn_sonido_icono.validar_click(lista_eventos) == True:
        #Valido si el sonido esta encendido o apagado
        if juego.sonidos == True:
            #Cambio el estado de sonido a apagado
            btn_sonido_icono.actualizar_img_btn("imagenes\General\sonidos_off.png", (25,25))
            btn_sonido_icono.rect = centrar_rect(btn_sonido.rect.centerx - 70, btn_sonido.rect.centery, 
                                                    btn_sonido_icono.rect)
            btn_sonido.color = colores.ROJO_C
            btn_sonido.actualizar_txt("OFF")
            juego.sonidos = False
        else:
            #Cambio el estado de sonido a encendido
            btn_sonido_icono.actualizar_img_btn("imagenes\General\sonidos_on.png", (25,25))
            btn_sonido_icono.rect = centrar_rect(btn_sonido.rect.centerx + 70, btn_sonido.rect.centery, 
                                                    btn_sonido_icono.rect)
            btn_sonido.color = colores.VERDE_C
            btn_sonido.actualizar_txt("ON")
            juego.sonidos = True
    #Verifico si se hizo click en el boton de musica       
    if btn_musica_icono.validar_click(lista_eventos) == True:
        #Valido si la musica esta encendida o apagada
        if juego.musica == True:
            #Cambio el estado de musica a apagada
            btn_musica_icono.actualizar_img_btn("imagenes\General\musica_off.png", (25,25))
            btn_musica_icono.rect = centrar_rect(btn_musica.rect.centerx - 70, btn_musica.rect.centery, 
                                                    btn_musica_icono.rect)
            btn_musica.color = colores.ROJO_C
            btn_musica.actualizar_txt("OFF")
            juego.musica = False
        else:
            #Cambio el estado de musica a encendida
            btn_musica_icono.actualizar_img_btn("imagenes\General\musica_on.png", (25,25))
            btn_musica_icono.rect = centrar_rect(btn_musica.rect.centerx + 70, btn_musica.rect.centery, 
                                                    btn_musica_icono.rect)
            btn_musica.color = colores.VERDE_C
            btn_musica.actualizar_txt("ON")
            juego.musica = True
            
def mostrar_jugando(ventana, pos_mouse, lista_eventos, juego) -> None:
    
    fondo_superior_jugando = pygame.image.load("imagenes\Fondos\Fondo_jugando.png")
    fondo_superior_jugando = pygame.transform.scale(fondo_superior_jugando, (1000, 300))
    data_archivo = obtener_archivo_categoria(juego)
    
    if juego.tiempo_in_preg == None:
        juego.tiempo_in_preg = pygame.time.get_ticks()
        
    juego.calcular_tiempo_restante()
    
    if juego.vidas == 0:
        juego.esperar(2000)
        juego.jugando = False
        
    if len(juego.preguntas_posibles) == 0:
        with open(data_archivo, "r") as archivo:
            data = json.load(archivo)
            for i in range(len(data)):
                if data[i]["dificultad"] == juego.dificultad:
                    juego.preguntas_posibles.append(data[i])
    elif len(juego.preguntas_posibles) == 4:
        juego.pausado = False
        juego.jugando = False
        
    if juego.pregunta_actual == None or juego.tiempo_rest_preg == 0:
        juego.obtener_pregunta()   
        juego.obtener_rtas([btn_rta_1, btn_rta_2, btn_rta_3, btn_rta_4])
        if juego.tiempo_rest_preg == 0 and juego.pregunta_acertada == False:
            juego.vidas -= 1
        juego.resetear_tiempo()
        juego.pregunta_acertada = False
        resetear_btns_rtas([btn_rta_1, btn_rta_2, btn_rta_3, btn_rta_4])
    elif juego.pregunta_acertada == True:
        btn_rta_1.hover = False
        btn_rta_2.hover = False
        btn_rta_3.hover = False
        btn_rta_4.hover = False
    
     
    #Fondo de pantalla para las respuestas
    fondo_inferior_jugando = pygame.image.load("imagenes\Fondos\Fondo_respuestas.jpg")
    fondo_inferior_jugando = pygame.transform.scale(fondo_inferior_jugando, (1000,320))
    ventana.blit(fondo_inferior_jugando, (0, 265))
    ventana.blit(fondo_superior_jugando, (0,0))
    # Boton de pausa con hover
    btn_pausa.dibujar_btn(ventana, 0, 5, pos_mouse = pos_mouse)
    #Imagen vidas
    imagen_vidas = pygame.image.load("imagenes\P_Jugando\Vida.png")
    imagen_vidas = pygame.transform.scale(imagen_vidas, (30,30))

    # Posición inicial y separación entre vidas
    posicion_inicial = (50, 5)
    separacion = 20

    # Dibujar las vidas
    for i in range(juego.vidas):
        ventana.blit(imagen_vidas, (posicion_inicial[0] + i * separacion, posicion_inicial[1]))

#Imagen del personaje
    imagen_personaje = pygame.image.load("imagenes\P_Principal\personaje.png")
    imagen_personaje = pygame.transform.scale(imagen_personaje, (100,180))
    ventana.blit(imagen_personaje, (100, 85))

# Cantidad de monedas y tiempo:
    btn_cant_monedas.dibujar_btn(ventana, 0, 0, -30, 0)
    txt_cant_monedas = fuentes.FUENTE_25.render(f"{juego.monedas}", True, colores.BLANCO)
    ventana.blit(txt_cant_monedas, (centrar_txt(rectangulos.REC_PJ_MONEDAS.centerx + 23, rectangulos.REC_PJ_MONEDAS.centery, 
                                                txt_cant_monedas )))
    
    btn_cant_tiempo.dibujar_btn(ventana, 0, 0, -30, -2)
    txt_cant_tiempo = fuentes.FUENTE_25.render(str(juego.tiempo_rest_preg), True, colores.BLANCO)
    ventana.blit(txt_cant_tiempo, (centrar_txt(rectangulos.REC_PJ_TIEMPO.centerx +23 , rectangulos.REC_PJ_TIEMPO.centery, 
                                               txt_cant_tiempo )))
# Nivel que se encuentra
    categoria = obtener_categoria(juego)
    dificultad = obtener_dificultad(juego)
    txt_dif_cat = fuentes.FUENTE_25.render(f"{categoria}: {dificultad}",True, colores.BLANCO)
    ventana.blit(txt_dif_cat, (centrar_txt(rectangulos.REC_NIVEL_BANDERAS.centerx, rectangulos.REC_NIVEL_BANDERAS.centery + 10, 
                                             txt_dif_cat)))
# Fondo de la imagen que debe contestar
    btn_fondo_bandera.rect = centrar_rect(ventana.get_rect().centerx, ventana.get_rect().centery - 80, btn_fondo_bandera.rect)
    btn_fondo_bandera.dibujar_btn(ventana, 0, 5)
    btn_bandera.rect = centrar_rect(btn_fondo_bandera.rect.centerx, btn_fondo_bandera.rect.centery, btn_bandera.rect)
    btn_bandera.actualizar_img_btn(juego.pregunta_actual["url_imagen"], (200,200))
    btn_bandera.dibujar_btn(ventana, 0, 5)
#Rectangulo de respuestas:
    btn_rta_1.dibujar_btn(ventana, 0, 5, pos_mouse= pos_mouse )
    btn_rta_2.dibujar_btn(ventana, 0, 5, pos_mouse= pos_mouse)
    btn_rta_3.dibujar_btn(ventana, 0, 5, pos_mouse= pos_mouse)
    btn_rta_4.dibujar_btn(ventana, 0, 5, pos_mouse= pos_mouse )
    juego.validar_click_rtas([btn_rta_1, btn_rta_2, btn_rta_3, btn_rta_4],  lista_eventos)
# Agrego menu de pausa
    if btn_pausa.validar_click(lista_eventos) == True:
        if juego.pausado == False:
            juego.pausado = True
        else:
            juego.pausado = False
    if juego.pausado == True:
        mostrar_pausa(ventana, lista_eventos, pos_mouse, juego)
    
def mostrar_c_jugar(ventana, lista_eventos, pos_mouse, juego):
    fondo_c_jugar = pygame.image.load("imagenes\Fondos\Fondo_como_jugar.jpg")
    fondo_c_jugar = pygame.transform.scale(fondo_c_jugar, (1000, 500))
    ventana.blit(fondo_c_jugar, (0,0))
    
    btn_explicacion_c_jugar.dibujar_btn(ventana,0,5)
    btn_cerrar_c_jugar.dibujar_btn(ventana, 0, 5, pos_mouse = pos_mouse)
    #Verifico si hizo click al cerrar el menu de como jugar
    if btn_cerrar_c_jugar.validar_click(lista_eventos) == True:
        juego.pausado = False
        juego.mostrando_como_jugar = False  #prueba

def mostrar_tienda(ventana, lista_eventos, pos_mouse, juego):
    fondo_tienda = pygame.image.load("imagenes\Fondos\Fondo_tienda.jpg")
    fondo_tienda = pygame.transform.scale(fondo_tienda, (1000, 500))
    ventana.blit(fondo_tienda, (0,0))

    # menu_tienda.dibujar_btn(ventana, 0, 3)
    btn_cerrar_tienda.dibujar_btn(ventana, 0, 5, pos_mouse = pos_mouse)
    btn_titulo_tienda.dibujar_btn(ventana, 0, 0)
    btn_candado_tienda.dibujar_btn(ventana, 0, 5)
    #Verifico si hizo click al cerrar el menu de TIENDA
    if btn_cerrar_tienda.validar_click(lista_eventos) == True:
        juego.pausado = False
        juego.mostrando_tienda = False

