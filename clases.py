import pygame
import random
from funciones import *

pygame.init()
pygame.mixer.init()

class Juego():
    def __init__(self) -> None:
        self.logeado = False
        self.jugando = False
        self.pausado = False
        self.nombre_jugador = ""
        self.puntaje = 0
        self.gemas = 0
        self.monedas = 0
        self.nivel_jugador = 0
        self.exp_jugador = 0
        self.categoria = "b"
        self.dificultad = "f"
        self.preguntas_posibles = []
        self.pregunta_actual = None
        self.sonidos = True
        self.musica = True
        self.cancion = None
        self.mostrando_configuracion = False
        self.mostrando_como_jugar = False
        self.mostrando_tienda = False
    
    def obtener_pregunta(self):
        numero_random = random.randint(0,len(self.preguntas_posibles)-1)
        self.pregunta_actual = self.preguntas_posibles[numero_random]
        self.preguntas_posibles.pop(numero_random)
        
class Boton():
    def __init__(self, rect, color, hover = False) -> None:
        self.rect = pygame.Rect(rect)
        self.color = color
        self.hover = hover
    
    def dibujar_btn(self, superficie, ancho = 0, redondeado = 0, pos_mouse = (0,0)):
        
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
    def validar_click(self, lista_eventos):
        #Valido si se hizo click en el boton
        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  # Botón izquierdo del ratón
                    #Valido si el click fue dentro del boton
                    if self.rect.collidepoint(evento.pos):
                        return True
            return False

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
        
    def validar_click(self, lista_eventos):
        #Valido si se hizo click en el boton
        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  # Botón izquierdo del ratón
                    #Valido si el click fue dentro del boton
                    if self.rect.collidepoint(evento.pos):
                        return True
            return False
    
    def actualizar_txt(self, txt):
        self.txt = txt
        self.txt_renderizado = self.fuente.render(self.txt, True, self.color_txt)
    
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
        
    def validar_click(self, lista_eventos):
        #Valido si se hizo click en el boton
        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  # Botón izquierdo del ratón
                    #Valido si el click fue dentro del boton
                    if self.rect.collidepoint(evento.pos):
                        return True
            return False 
        
    def actualizar_img_btn(self, ruta_imagen, medida_img):
        self.imagen = pygame.image.load(ruta_imagen)
        self.imagen = pygame.transform.scale(self.imagen, medida_img)

class BotonEntradaTxt():
    def __init__(self, rect, color_inact, color_act, txt = "", fuente = None, color_txt = None) -> None:
        self.rect = pygame.Rect(rect)
        self.color_inact = color_inact
        self.color_act = color_act
        self.escribiendo = False
        self.txt = txt
        if txt != "":
            self.color_txt = color_txt
            self.fuente = fuente
            self.txt_renderizado = self.fuente.render(self.txt, True, self.color_txt)
        else:
            self.txt_renderizado = None
        
    def dibujar_btn(self, superficie, ancho = 0, redondeado = 0, pos_txt_x = 0, pos_txt_y = 0):
        
        if self.escribiendo == False:
            pygame.draw.rect(superficie, self.color_inact, self.rect, ancho, redondeado)
        else:
            pygame.draw.rect(superficie, self.color_act, self.rect, ancho, redondeado)
        if self.txt_renderizado != None: 
            superficie.blit(self.txt_renderizado, (centrar_txt(self.rect.centerx + pos_txt_x, self.rect.centery + pos_txt_y, \
                self.txt_renderizado)))
            
    def validar_escritura(self, pos_mouse, lista_eventos, txt_ingreso):
        
        if validar_click_en_boton(lista_eventos, pos_mouse, self.rect) == True or txt_ingreso != "":
            #Cambio el estado escribiendo del objeto segun corresponda
            self.escribiendo = True
        elif validar_click_en_boton(lista_eventos, pos_mouse, self.rect) == False:
            self.escribiendo = False
# class Entrada():
    
#     def __init__(self, fuente, pos_x = 0, pos_y= 0) -> None:
#         self.caracteres =  [""]
#         self.fuente = fuente
#         self.distancia = 20
#         self.pos_x = pos_x
#         self.pos_y = pos_y
        
#     def escribir_ingreso(self, evento):
        
#         if evento.type == pygame.KEYDOWN:
#             if evento.key == pygame.K_RETURN:
#                 self.caracteres.append('\R')
#             elif evento.key == pygame.K_BACKSPACE:
#                 if len(self.caracteres) > 1:
#                     self.caracteres.pop()
#             else:
#                 self.caracteres.append()
#     def leer_tecla(self, evento):
        
#         if evento.type == pygame.KEYDOWN:
#             if evento.key == pygame.K_RETURN:
#                 return "\R"
#             elif evento.key == pygame.K_BACKSPACE:
#                 return "\B"
#             else
    