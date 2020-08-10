#---------------------------------------------------------------------------
import pygame
#---------------------------------------------------------------------------
class Portal:
    def __init__(self, x1, y1, x2, y2, color):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.alto = 70
        self.ancho = 70
        self.especial = False
        self.color = color
#---------------------------------------------------------------------------
    def dibujar(self, ventana, nsprite):
            #sprites:
            ruta ="Imagenes/portal_"+self.color+str(nsprite)+".png"
            if self.especial == True:
                ruta ="Imagenes/portal_especial.png"
                self.especial = False
            imagen = pygame.image.load(ruta)
            imagen = pygame.transform.scale(imagen, ( self.ancho, self.alto))
            ventana.blit(imagen,(self.x1,self.y1))
            ventana.blit(imagen,(self.x2,self.y2))
            '''
            pygame.draw.rect(ventana, self.color, (self.x,
                                                self.y,
                                                self.ancho,
                                                self.alto))
            '''                                              
#---------------------------------------------------------------------------
    def get_espacio(self):
        return pygame.Rect(self.x1, self.y1, self.ancho, self.alto)  
#---------------------------------------------------------------------------        
    def get_espacio2(self):
        return pygame.Rect(self.x2, self.y2, self.ancho, self.alto)  
#---------------------------------------------------------------------------  

