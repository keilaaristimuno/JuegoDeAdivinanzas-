import pygame

pygame.init()
pygame.mixer.init()

rta_correcta = pygame.mixer.Sound('sonidos/Rta_correcta.wav')
rta_incorrecta = pygame.mixer.Sound('sonidos/Rta_incorrecta.wav')
nuevo_record = pygame.mixer.Sound('sonidos/Nuevo_record.mp3')
final_partida = pygame.mixer.Sound('sonidos/Final.mp3')
jugar = pygame.mixer.Sound('sonidos/Jugar.wav')
click = pygame.mixer.Sound('sonidos/Click.mp3')
seleccion = pygame.mixer.Sound('sonidos/Seleccion.mp3') 