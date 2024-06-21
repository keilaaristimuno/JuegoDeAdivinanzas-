import pygame

pygame.init()

def centrar_txt(centerx, centery, txt):
    """ 
    Centra una etiqueta.
    
    Args: 
        centerx: Valor de la coordenada x del centro.
        centry: Valor de la coordenada y del centro.
        
    Returns:
        pos_et: Coordenadas del texto centradas.
    
    """
    pos_txt = txt.get_rect()
    pos_txt.centerx = centerx
    pos_txt.centery = centery
    
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
    diccionario["tiempo"] = int(diccionario["tiempo"])
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
    