#---------------------------------------------------------------------------
import pygame
import random
from Objetos import Objeto
#---------------------------------------------------------------------------********
class Horno:
#---------------------------------------------------------------------------
    def __init__(self, id, posx, posy, tipoComida, tiempo_cocinado):
        self.name = id
        self.x = posx
        self.y =posy
        self.ancho = 100
        self.alto = 100
        self.color = (255,0,0)
        self.tipoComida = tipoComida
        self.objeto = None
        self.comida_lista = False
        self.contador = 0
        self.tiempo_cocinado = tiempo_cocinado
        self.activo = False
#---------------------------------------------------------------------------
    def dibujar(self, ventana, font):
            #sprites:
            ruta ="Imagenes/estufa_"+self.tipoComida+".png"
            if self.activo == False:
               ruta ="Imagenes/estufa.png" 
            imagen = pygame.image.load(ruta)
            imagen = pygame.transform.scale(imagen, ( self.ancho, self.alto))
            ventana.blit(imagen,(self.x,self.y))
            '''
            pygame.draw.rect(ventana, self.color, (self.x,
                                                self.y,
                                                self.ancho,
                                                self.alto))
            '''
            #texto = font.render(self.name, 1, (255, 255, 255))
            color_font = (255,0,0)
            #ventana.blit(texto, (self.x, self.y-10))
            if self.activo:
                aux = self.tiempo_cocinado - self.contador
                if aux <= 0:
                    aux = 0
                    color_font = (0,200,10)
                texto = font.render(str(aux), 1, color_font)
                ventana.blit(texto, (self.x, self.y+ self.alto +5))
                if self.objeto != None:
                    self.objeto.dibujar(ventana, self.x, self.y, font)                                           
#---------------------------------------------------------------------------
    def cocinar(self):
           if self.activo == True:
                self.contador = self.contador +1
                if self.contador == self.tiempo_cocinado:
                        self.objeto = Objeto(self.tipoComida, (self.contador*random.randint(1, 3))) #cambiar a aleatorio 
                        self.comida_lista = True
                        alarma = pygame.mixer.Sound("Audio/sorpresa.wav")
                        alarma.play()
                        #hacer sonido de listo                                          
#--------------------------------------------------------------------------- 
    def get_espacio(self):
        return pygame.Rect(self.x, self.y, self.ancho, self.alto)
#---------------------------------------------------------------------------   
    def getObjeto(self):
        return self.objeto
#---------------------------------------------------------------------------           
    def setObjeto(self, objeto):
        self.contador = 0
        self.objeto = objeto   
#---------------------------------------------------------------------------  
    def interactuar(self):
        return True        
#---------------------------------------------------------------------------********   