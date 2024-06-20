import pygame
import colores

pygame.init() 

window = pygame.display.set_mode((1200,800)) 

#establezco titulo de la venta:
pygame.display.set_caption("Adivina el logo")

# pygame carga una imagen,el load representa una superficie
icon = pygame.image.load("imagenes\icono.png")
#seteo el icono:
pygame.display.set_icon(icon)

#rellena la ventana de un color:
window.fill(colores.LIGHT_BROWN)

flag = True
while flag:
    list_event = pygame.event.get()
    for event in list_event:
        if event.type == pygame.QUIT: #PREGUNTO SI PRESIONO la x de la ventana para salir
            flag = False
    #Todo los obejtos superficies que meta en la ventana lo tengo que actualizar con el update
    pygame.display.update() #hasta que no actualizo la ventana no la cambio de estado entonces el color no se pone

pygame.quit()

#probandooooooooooo