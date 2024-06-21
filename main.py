import pygame
import colores
import pantallas
import herraminetas
import funciones

pygame.init() 

ventana = pygame.display.set_mode((1000,500))

#establezco titulo de la venta:
pygame.display.set_caption("Adivina el logo")

# pygame carga una imagen,el load representa una superficie
logo = pygame.image.load("imagenes\icono.png")
#seteo el icono:
pygame.display.set_icon(logo)

#Ponemos un fondo a la ventana:
fondo = pygame.image.load("imagenes\muro_menu.png")
ventana.blit(fondo, (0,0))

with open("datos_jugador.csv", "r") as archivo:
    datos = archivo.read().split("\n")
    cabecera = datos[0].split(",")
    datos.pop(0)
    jugadores = funciones.crear_lista_jugadores(datos, cabecera)

jugador = jugadores[0]

ejecutar = True
while ejecutar:
    lista_eventos = pygame.event.get()
    pos_mouse = pygame.mouse.get_pos()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT: #PREGUNTO SI PRESIONO la x de la ventana para salir
            ejecutar = False
        herraminetas.obtener_pos_mouse(evento)
    pantallas.mostrar_principal(ventana, jugador, pos_mouse)
    
    #Todo los obejtos superficies que meta en la ventana lo tengo que actualizar con el update
    pygame.display.update() #hasta que no actualizo la ventana no la cambio de estado entonces el color no se pone

pygame.quit()