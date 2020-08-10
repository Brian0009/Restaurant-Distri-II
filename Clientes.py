#---------------------------------------------------------------------------
import pygame
from Objetos import Objeto
#---------------------------------------------------------------------------********
class Client:
#---------------------------------------------------------------------------
    def __init__(self, id, posx, posy, calma, antojo):
        self.name = id
        self.x = posx
        self.y =posy
        self.ancho = 100
        self.alto = 100
        self.color = (255,0,0)
        self.objeto = None
        self.calma = calma
        self.antojo = antojo
        self.activo = False
        self.game_over = False 
#---------------------------------------------------------------------------
    def dibujar(self, ventana, font, coef_calma, coef_violencia):
            '''
            pygame.draw.rect(ventana, self.color, (self.x,
                                                self.y,
                                                self.ancho,
                                                self.alto))
            '''
            #sprites:
            ruta ="Imagenes/mesa_"+self.name+".png"
            if self.activo == False:
               ruta ="Imagenes/mesa.png" 
               if self.name == "9":
                    ruta ="Imagenes/mesa_e"+".png"   
            imagen = pygame.image.load(ruta)
            imagen = pygame.transform.scale(imagen, ( self.ancho, self.alto))
            ventana.blit(imagen,(self.x,self.y))            
            if self.activo:
                if self.calma <= 0:
                    aux = "0"
                else:
                    aux = str(self.calma)                                        
                texto = font.render("calma: "+aux, 1, self.color)
                ventana.blit(texto, (self.x+30, self.y+ self.alto +5))
                #ventana.blit(texto, (self.x, self.y+ self.alto +30))  
                if self.objeto == None:
                    ruta = ruta ="Imagenes/"+self.antojo+"_p.png"
                    imagen = pygame.image.load(ruta)
                    imagen = pygame.transform.scale(imagen, (40, 40))
                    ventana.blit(imagen,(self.x+15,self.y-20))                                      
                if self.objeto != None:
                    self.objeto.dibujar(ventana, self.x, self.y, font)
                self.comer(coef_calma, coef_violencia)                                           
#---------------------------------------------------------------------------
    def comer(self, coef_calma,  coef_violencia ):
        if self.objeto != None:
            if self.objeto.name != "basura":
                self.calma = self.calma + coef_calma
                self.objeto.procesar()
                self.color = (0,255,0)
                return True
            else:
                self.calma = self.calma -  coef_violencia
                self.color = (255,0,0)
        else:
            self.calma = self.calma -coef_violencia
            self.color = (255,0,0)
        if self.calma <= 0:
            self.game_over = True               
    def get_espacio(self):
        return pygame.Rect(self.x, self.y, self.ancho, self.alto)
#---------------------------------------------------------------------------   
    def getObjeto(self):
        return self.objeto
#---------------------------------------------------------------------------           
    def setObjeto(self, objeto):
        self.objeto = objeto   
#---------------------------------------------------------------------------********   