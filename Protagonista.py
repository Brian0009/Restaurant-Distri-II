#---------------------------------------------------------------------------
import pygame
from Objetos import Objeto
#---------------------------------------------------------------------------********
class protagonista:
#---------------------------------------------------------------------------
    def __init__(self, nombre):
        self.name = nombre
        self.x = 430 #pos Inicial
        self.y = 130
        self.ancho = 70
        self.alto = 70
        self.color = (0,0,255)
        self.objeto = None
        self.orientacion = "Down"
        self.especial = False
#---------------------------------------------------------------------------
    def dibujar(self, ventana, font, nsprite):
            #sprites:
            ruta ="Imagenes/"+self.orientacion+"__"+str(nsprite)+".png"
            if self.especial == True:
                ruta ="Imagenes/special__1.png"
                self.especial = False
            imagen = pygame.image.load(ruta)
            imagen = pygame.transform.scale(imagen, ( self.ancho, self.alto))
        
            ventana.blit(imagen,(self.x,self.y))
            '''
            pygame.draw.rect(ventana, self.color, (self.x,
                                                self.y,
                                                self.ancho,
                                                self.alto))
            '''
            if self.objeto != None:
                self.objeto.dibujar(ventana, self.x, self.y, font)                                         
#---------------------------------------------------------------------------
    def movimiento(self, x,y):
        if (self.x+x)>0:
            self.x = self.x + x
        if (self.y+y)>0:
            self.y = self.y + y
#---------------------------------------------------------------------------
    def get_espacio(self):
        return pygame.Rect(self.x, self.y, self.ancho, self.alto)  
#---------------------------------------------------------------------------
    def get_futuro_espacio(self, x, y):
        return pygame.Rect(self.x+x, self.y+y, self.ancho, self.alto)
#---------------------------------------------------------------------------   
    def getObjeto(self):
        return self.objeto
#---------------------------------------------------------------------------           
    def setObjeto(self, objeto):
        self.objeto = objeto 
#--------------------------------------------------------------------------- 
    def tieneObjeto(self):
        if self.objeto== None:
            return False
        else:
            return True                                              
#---------------------------------------------------------------------------*********