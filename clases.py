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
        self.gemas = 0
        self.monedas = 0
        self.nivel_jugador = 0
        self.exp_jugador = 0
        self.categoria = "b"
        self.dificultad = "f"
        self.record_monedas = 0
        self.vidas = 5
        self.preguntas_posibles = []
        self.pregunta_actual = None
        self.pregunta_acertada = False
        self.sonidos = True
        self.musica = True
        self.cancion = None
        self.tiempo_in_preg = None
        self.tiempo_act_preg = None
        self.tiempo_rest_preg = 30
        self.mostrando_configuracion = False
        self.mostrando_como_jugar = False
        self.mostrando_tienda = False
        self.mostrando_jugadores = False

    def logear(self, jugador):
        
        self.logeado = True
        self.nombre_jugador = jugador["nombre"]
        self.monedas = jugador["monedas"]
        self.gemas = jugador["gemas"]
        self.nivel_jugador = jugador["nivel_exp"]
        self.exp_jugador = jugador["puntaje_exp"]
        self.record_monedas = jugador["record_monedas"]
        
#Generar las preguntas de manera aleatoria
    def obtener_pregunta(self):
        numero_random = random.randint(0,len(self.preguntas_posibles)-1)
        self.pregunta_actual = self.preguntas_posibles[numero_random]
        self.preguntas_posibles.pop(numero_random)
        
    #Genera las respuestas de manera aleatoria random
    def obtener_rtas(self, btns: list):
        indices_usados = []
        indice_btns = 0
        rtas = self.pregunta_actual["rtas_incorrectas"]
        rtas.append(self.pregunta_actual["rta_correcta"])
        
        while len(indices_usados) < 4:
            indice_random = random.randint(0,3)
            agregar = True
            for indice_usado in indices_usados:
                if indice_random == indice_usado:
                    agregar = False   
            if agregar == True:
                btns[indice_btns].actualizar_txt(rtas[indice_random])
                indice_btns += 1
                indices_usados.append(indice_random)
                
    def validar_click_rtas(self, btns: list,  lista_eventos):
        for evento in lista_eventos:
            for btn in btns:
                if btn.validar_click(lista_eventos) == True and btn.color != colores.VERDE_C:
                    if btn.txt == self.pregunta_actual["rta_correcta"]:
                        btn.color = colores.VERDE_C
                        self.recompensar_rta()
                        self.actualizar_exp_jugador()
                        self.actualizar_record()
                        self.pregunta_acertada = True
                        self.tiempo_acumulado += int((self.tiempo_act_preg - self.tiempo_in_preg) * 0.001) 
                        if self.pregunta_acertada == True:
                            self.esperar(1000)
                            
                    elif btn.color !=  colores.ROJO_C:
                        btn.color = colores.ROJO_C
                        btn.hover = False
                        self.penalizar_rta()
                        self.vidas -= 1
                        if self.vidas == 0:
                            self.esperar(2000)
                            self.jugando = False
    def actualizar_record(self):
        
        if self.record_monedas < self.monedas:
            self.record_monedas = self.monedas
                            
    def obtener_multiplicador(self):
        if self.dificultad == "f":
            multiplicador = 1
        elif self.dificultad == "n":
            multiplicador = 2
        else:
            multiplicador = 3
        return multiplicador 
                    
    def recompensar_rta(self):
        
        multiplicador = self.obtener_multiplicador()
        match self.categoria:
        
            case "b":
                monedas = 20 * multiplicador
                self.monedas += monedas 
            case "c":
                monedas = 35 * multiplicador
                gemas = 1 * multiplicador
                self.monedas += monedas
                self.gemas += gemas
            case "e":
                monedas = 50 * multiplicador
                gemas = 2 * multiplicador
                self.monedas += monedas
                self.gemas += gemas
                
    def penalizar_rta(self):
        
        if self.dificultad == "f":
            penalizacion = 10
        elif self.dificultad == "n":
            penalizacion = 15
        else:
            penalizacion = 20
        
        match self.categoria:
        
            case "b":
                pass
            case "c":
                if self.monedas - penalizacion >= 0:
                    self.monedas -= penalizacion
                else:
                    self.monedas = 0
            case "e":
                if self.monedas - penalizacion >= 0:
                    self.monedas -= penalizacion
                else:
                    self.monedas = 0
                    
    def esperar(self, espera):
        pygame.time.delay(espera)
        self.tiempo_rest_preg = 0
            
    def calcular_tiempo_restante(self):
        self.tiempo_act_preg = pygame.time.get_ticks()
        tiempo_transcurrido = int((self.tiempo_act_preg - self.tiempo_in_preg) * 0.001)
        if self.tiempo_rest_preg != 0 and self.pregunta_acertada == False:
            self.tiempo_rest_preg = 30 - tiempo_transcurrido
            
    def resetear_datos(self):
        self.pregunta_actual = None
        self.preguntas_posibles = []
        self.vidas = 5
        self.pregunta_acertada = False
        self.jugando = False
        self.tiempo_acumulado = 0
    
    def resetear_tiempo(self):
        self.tiempo_in_preg = None
        self.tiempo_act_preg = None
        self.tiempo_rest_preg = 30
        
    def actualizar_exp_jugador(self):
        multiplicador = self.obtener_multiplicador()
        self.exp_jugador[0] += 5 * multiplicador
        if self.exp_jugador[0] >= self.exp_jugador[1]:
            self.nivel_jugador += 1
            if self.exp_jugador[0] == self.exp_jugador[1]:
                self.exp_jugador[0] = 0
            else:
                self.exp_jugador[0] = self.exp_jugador[0] - self.exp_jugador[1]
            self.exp_jugador[1] = self.nivel_jugador * 10
            
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

    