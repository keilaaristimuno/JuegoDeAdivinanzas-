import pygame
from funciones import *

pygame.init()

class Boton():
    def __init__(self, rect, color, hover = False) -> None:
        self.rect = pygame.Rect(rect)
        self.color = color
        self.hover = hover
    
    def dibujar_btn(self, superficie, ancho = 0, redondeado = 0, pos_img_x = 0, pos_img_y = 0, pos_mouse = (0,0)):
        
        if self.hover == False:
            pygame.draw.rect(superficie, self.color, self.rect, ancho, redondeado)
        else:
            pygame.draw.rect(superficie, self.hover_btn(pos_mouse, self.color, self.hover), self.rect, ancho, redondeado)
            
    def hover_btn(self, pos_mouse, color_n, color_h):
        #Valido si el mouse esta sobre el boton
        if self.rect.collidepoint(pos_mouse):
            #El mouse esta sobre el boton entonces retorno el color hover
            return color_h
        else:
            #El mouse no esta sobre el boton entonces retorno el color normal
            return color_n    

class BotonTxt():
    def __init__(self, rect, color, fuente, txt: str = '', color_txt = (0,0,0), hover = False) -> None:
        self.rect = pygame.Rect(rect)
        self.color = color
        self.fuente = fuente
        self.txt = txt
        self.color_txt = color_txt
        self.txt_renderizado = self.fuente.render(self.txt, True, self.color_txt)
        self.hover = hover

    def hover_btn(self, pos_mouse, color_n, color_h):
        #Valido si el mouse esta sobre el boton
        if self.rect.collidepoint(pos_mouse):
            #El mouse esta sobre el boton entonces retorno el color hover
            return color_h
        else:
            #El mouse no esta sobre el boton entonces retorno el color normal
            return color_n

    def dibujar_btn(self, superficie, ancho = 0, redondeado = 0, pos_txt_x = 0, pos_txt_y = 0, pos_mouse = (0,0)):
        
        if self.hover == False:
            pygame.draw.rect(superficie, self.color, self.rect, ancho, redondeado)
        else:
            pygame.draw.rect(superficie, self.hover_btn(pos_mouse, self.color, self.hover), self.rect, ancho, redondeado)
        superficie.blit(self.txt_renderizado, (centrar_txt(self.rect.centerx + pos_txt_x, self.rect.centery + pos_txt_y, \
            self.txt_renderizado)))
        
    def validar_click(self, evento):
        #Valido si se hizo click en el boton
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # Botón izquierdo del ratón
                #Valido si el click fue dentro del boton
                if self.rect.collidepoint(evento.pos):
                    return True
        return False
    
class BotonImg():
    def __init__(self, rect, color, ruta_imagen, medida_img, hover = False) -> None:
        self.rect = pygame.Rect(rect)
        self.color = color
        self.ruta_imagen = ruta_imagen
        self.imagen = pygame.image.load(self.ruta_imagen)
        self.imagen = pygame.transform.scale(self.imagen, medida_img)
        self.hover = hover
    
    def dibujar_btn(self, superficie, ancho = 0, redondeado = 0, pos_img_x = 0, pos_img_y = 0, pos_mouse = (0,0)):
        
        if self.hover == False:
            pygame.draw.rect(superficie, self.color, self.rect, ancho, redondeado)
        else:
            pygame.draw.rect(superficie, self.hover_btn(pos_mouse, self.color, self.hover), self.rect, ancho, redondeado)
        superficie.blit(self.imagen, (centrar_txt(self.rect.centerx + pos_img_x, self.rect.centery + pos_img_y, self.imagen)))
        
    def hover_btn(self, pos_mouse, color_n, color_h):
        #Valido si el mouse esta sobre el boton
        if self.rect.collidepoint(pos_mouse):
            #El mouse esta sobre el boton entonces retorno el color hover
            return color_h
        else:
            #El mouse no esta sobre el boton entonces retorno el color normal
            return color_n   
