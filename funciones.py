import pygame
import constantes.colores as colores

pygame.init()

def centrar_rect(centerx, centery, rect):
    """ 
    Centra un rectangulo en base a otro.
    
    Args: 
        centerx: Valor de la coordenada x del centro.
        centry: Valor de la coordenada y del centro.
        rect: Rectangula a centrar.
        
    Returns:
        pos_et: Coordenadas del texto centradas.
    
    """
    rect.centerx = centerx
    rect.centery = centery
    
    return(rect)

def centrar_txt(centerx, centery, txt):
    
    pos_txt = txt.get_rect()
    pos_txt = centrar_rect(centerx, centery, pos_txt)
    
    return(pos_txt)
   
def crear_dic_jugador(datos_jugador: list, cabecera: list) -> dict:
    #Creo el diccionario del jugador
    jugador  = {}
    
    #Recorro la cabecera y completo el diccionario
    for i in range(len(cabecera)):
        jugador[cabecera[i]] = datos_jugador[i]
    
    #Normalizo los datos del diccionario
    normalizar_datos_jugador(jugador)
    return jugador

def normalizar_datos_jugador(diccionario: dict) -> None:
    
    diccionario["monedas"] = int(diccionario["monedas"])
    diccionario["gemas"] = int(diccionario["gemas"])
    diccionario["nivel_exp"] = int(diccionario["nivel_exp"])
    diccionario["puntaje_exp"] = diccionario["puntaje_exp"].split("/")
    for i in range(len(diccionario["puntaje_exp"])):
        diccionario["puntaje_exp"][i] = int(diccionario["puntaje_exp"][i])

def crear_lista_jugadores(datos: list, cabecera: list) -> list:
    """Crea una lista

    Args:
        datos (list): lista 
        cabecera (list): _description_

    Returns:
        list: _description_
    """
    #Creo la lista de jugadores
    lista_jugadores = []
    
    #Recorro la lista de los datos
    for elemento in datos:
        datos_jugador = elemento.split(",")
        lista_jugadores.append(crear_dic_jugador(datos_jugador,cabecera))  
        
    return lista_jugadores

def pintar_btn(rect_btn, pos_mouse, color_n, color_h):
    
    #Valido si el mouse esta sobre el boton
    if rect_btn.collidepoint(pos_mouse):
        #El mouse esta sobre el boton entonces retorno el color hover
        return color_h
    else:
        #El mouse no esta sobre el boton entonces retorno el color normal
        return color_n
 
def validar_click_en_boton(lista_eventos, pos_mouse, boton):
    
    for evento in lista_eventos:
        #Valido que el evento sea un click y este dentro del cuadro de texto
        if evento.type == pygame.MOUSEBUTTONDOWN and boton.collidepoint(pos_mouse) and evento.button == 1:   
            return True
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            return False

def mostrar_jugador_no_encontrado():
    print("jugador no encontrado")

def obtener_categoria(juego):
    
    match juego.categoria:
        
        case "b":
            categoria = "Banderas"
        case "c":
            categoria = "Comidas"
        case "e":
            categoria = "Equipos"
        case "a":
            categoria = "Autos"
        case "t":
            categoria = "Tecnologia"
    
    return categoria

def obtener_archivo_categoria(juego):
    
    match juego.categoria:
        case "b":
            categoria = "datos_banderas.json"
        case "c":
            categoria = "datos_comidas.json"
        case "e":
            categoria = "datos_equipos.json"
            
    return categoria

def obtener_dificultad(juego):

    match juego.dificultad:
        case "f":
            dificultad = "Facil"
        case "n":
            dificultad = "Normal"
        case "d":
            dificultad = "Dificil"
    
    return dificultad

def validar_dificultad_seleccionada(juego, btn_dif_f, btn_dif_n, btn_dif_d):
    match juego.dificultad:
        case "f":
            btn_dif_f.color = colores.VERDE_C
            btn_dif_n.color = colores.OCRE
            btn_dif_d.color = colores.ROJO_O
        case "n":
            btn_dif_f.color = colores.VERDE
            btn_dif_n.color = colores.AMARILLO
            btn_dif_d.color = colores.ROJO_O
        case "d":
            btn_dif_f.color = colores.VERDE
            btn_dif_n.color = colores.OCRE
            btn_dif_d.color = colores.ROJO_C
            
def validar_categoria_seleccionada(juego, btn_cat_banderas, btn_cat_comidas, btn_cat_equipos):
    match juego.categoria:
        case "b":
            btn_cat_banderas.color = colores.VERDE
            btn_cat_banderas.hover = colores.VERDE
            btn_cat_comidas.color = colores.GRIS
            btn_cat_comidas.hover = colores.GRIS_C
            btn_cat_equipos.color = colores.GRIS
            btn_cat_equipos.hover = colores.GRIS_C
        case "c":
            btn_cat_banderas.color = colores.GRIS
            btn_cat_banderas.hover = colores.GRIS_C
            btn_cat_comidas.color = colores.VERDE
            btn_cat_comidas.hover = colores.VERDE
            btn_cat_equipos.color = colores.GRIS
            btn_cat_equipos.hover = colores.GRIS_C
        case "e":
            btn_cat_banderas.color = colores.GRIS
            btn_cat_banderas.hover = colores.GRIS_C
            btn_cat_comidas.color = colores.GRIS
            btn_cat_comidas.hover = colores.GRIS_C
            btn_cat_equipos.color = colores.VERDE
            btn_cat_equipos.hover = colores.VERDE

def validar_enter(lista_eventos):
    for evento in lista_eventos:
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                return True