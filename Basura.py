#---------------------------------------------------------------------------
import pygame
#---------------------------------------------------------------------------
class thrash:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        self.ancho = 30
        self.alto = 60
        self.color = (90,25,255)
#---------------------------------------------------------------------------
    def dibujar(self, ventana, font):
            ruta ="Imagenes/basura_3.png"
            imagen = pygame.image.load(ruta)
            imagen = pygame.transform.scale(imagen, ( self.ancho, self.alto))
            ventana.blit(imagen,(self.x,self.y))
            '''pygame.draw.rect(ventana, self.color, (self.x,
                                                self.y,
                                                self.ancho,
                                                self.alto))
            '''                                        
#---------------------------------------------------------------------------
    def get_espacio(self):
            return pygame.Rect(self.x, self.y, self.ancho, self.alto)
#---------------------------------------------------------------------------            