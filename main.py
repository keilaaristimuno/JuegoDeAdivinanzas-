import pygame
import pantallas
import herraminetas
import funciones
import clases

pygame.init() 
pygame.mixer.init()
ventana = pygame.display.set_mode((1000,500))
#establezco titulo de la venta:
pygame.display.set_caption("Adivina el logo")
# pygame carga una imagen,el load representa una superficie
logo = pygame.image.load("imagenes\General\icono.png")
#seteo el icono:
pygame.display.set_icon(logo)
# #Ponemos un fondo distinto para la ventana de jugar:
with open("datos_jugador.csv", "r") as archivo:
    datos = archivo.read().split("\n")
    cabecera = datos[0].split(",")
    datos.pop(0)
    jugadores = funciones.crear_lista_jugadores(datos, cabecera)

juego = clases.Juego()
juego.cancion = "musica\musica_general.mp3"
pygame.mixer.music.load(juego.cancion)
pygame.mixer.music.play(-1)
pygame.mixer.music.pause()
reloj = pygame.time.Clock()
ejecutar = True

while ejecutar:
    lista_eventos = pygame.event.get()
    pos_mouse = pygame.mouse.get_pos()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT: #PREGUNTO SI PRESIONO la x de la ventana para salir
            ejecutar = False
        herraminetas.obtener_pos_click_izq_mouse(evento)

    if juego.logeado == False:
        pantallas.mostrar_inicio(ventana,pos_mouse, lista_eventos, juego, jugadores)
    elif juego.jugando == False:
        pantallas.mostrar_principal(ventana, pos_mouse, lista_eventos, juego)
    else:
        pantallas.mostrar_jugando(ventana, pos_mouse, lista_eventos, juego)
    #Todo los obejtos superficies que meta en la ventana lo tengo que actualizar con el update
    pygame.display.update() #hasta que no actualizo la ventana no la cambio de estado entonces el color no se pone
    
    reloj.tick(60)

jugadores_csv = ""
jugadores_csv = funciones.set_cabecera_csv(cabecera, jugadores_csv)
jugadores_csv = funciones.set_data_csv(jugadores, jugadores_csv, juego)

with open("datos_jugador.csv", "w") as file:     
    file.write(jugadores_csv)
    
pygame.quit()