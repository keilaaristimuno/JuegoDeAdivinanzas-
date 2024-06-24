import pygame
import pantallas
import herraminetas
import funciones
import clases


pygame.init() 

ventana = pygame.display.set_mode((1000,500))

#establezco titulo de la venta:
pygame.display.set_caption("Adivina el logo")

# pygame carga una imagen,el load representa una superficie
logo = pygame.image.load("imagenes\General\icono.png")
#seteo el icono:
pygame.display.set_icon(logo)

#Ponemos un fondo a la ventana:
fondo = pygame.image.load("imagenes\General\muro_menu.png")
ventana.blit(fondo, (0,0))

# #Ponemos un fondo distinto para la ventana de jugar:
fondo_jugando = pygame.image.load("imagenes\P_Jugando\Fondo_jugando.png")
fondo_jugando = pygame.transform.scale(fondo_jugando, (1000, 300))

with open("datos_jugador.csv", "r") as archivo:
    datos = archivo.read().split("\n")
    cabecera = datos[0].split(",")
    datos.pop(0)
    jugadores = funciones.crear_lista_jugadores(datos, cabecera)

jugador = jugadores[0]
juego = clases.Juego()
ejecutar = True
while ejecutar:
    lista_eventos = pygame.event.get()
    pos_mouse = pygame.mouse.get_pos()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT: #PREGUNTO SI PRESIONO la x de la ventana para salir
            ejecutar = False
        herraminetas.obtener_pos_click_izq_mouse(evento)

    if juego.logeado == False:
        pantallas.mostrar_inicio(ventana,pos_mouse, lista_eventos, juego)
    elif juego.jugando == False:
        ventana.blit(fondo, (0,0))
        pantallas.mostrar_principal(ventana, jugador, pos_mouse, lista_eventos, juego)
    else:
        print(herraminetas.obtener_pos_click_izq_mouse(evento))
        # ventana.blit(fondo, (0,0))
        ventana.blit(fondo_jugando, (0,0))
        pantallas.mostrar_jugando(ventana, jugador, pos_mouse)
    #Todo los obejtos superficies que meta en la ventana lo tengo que actualizar con el update
    pygame.display.update() #hasta que no actualizo la ventana no la cambio de estado entonces el color no se pone

pygame.quit()