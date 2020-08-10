#---------------------------------------------------------------------------
import pygame
import random
from Protagonista import protagonista
from Clientes import Client
from Hornitos import Horno
from Objetos import Objeto
from Basura import thrash
from Portales import Portal
#---------------------------------------------------------------------------
def colision(objA, objB, nx, ny):
    if objA.get_futuro_espacio(nx, ny).colliderect(objB.get_espacio()):
        return True
    else:
        return False    
#---------------------------------------------------------------------------
def revisar_colisiones_prota(prota, objetos, nx, ny):
    contador = 0
    llave = False
    while contador < len(objetos) and llave!=True:
        if colision(prota, objetos[contador], nx, ny) == True:
            print("no te puedes mover, hay un objeto!")
            return False
        contador = contador +1
    return True    
#---------------------------------------------------------------------------
def interaccion(prota, clientes, hornos, basuras, puntaje): #,basuras
    if prota.orientacion == "Up":
        nx =0
        ny = -10 
    elif prota.orientacion == "Down":
        nx = 0
        ny = 10
    elif prota.orientacion == "Right":
        nx = 10
        ny = 0
    elif prota.orientacion == "Left":
        nx = -10
        ny = 0
    contador = 0  
    llave = True        
    while contador < len(clientes) and llave == True:
        if colision(prota, clientes[int(contador)], nx, ny) == True:
            print("interacicion con:!"+clientes[int(contador)].name)
            llave = False
            if (clientes[int(contador)].objeto == None):
                if prota.objeto != None:
                    if prota.objeto.name == clientes[int(contador)].antojo:
                        clientes[int(contador)].setObjeto(prota.getObjeto())
                        prota.setObjeto(None)
                        bien.play()
                    else:
                        fail.play()
                        print("sonar feo")
                else:
                    print("sonar feo")
                    fail.play()                        
            else:
                if clientes[int(contador)].objeto.name == "basura":
                        prota.setObjeto(clientes[int(contador)].objeto)
                        clientes[int(contador)].setObjeto(None)
                        bien.play()
                        clientes[contador].antojo = lista_comidas[random.randint(0, numero_comidas)]
                        puntaje = puntaje + (int(contador)+1)*1000
                else:
                    print("sonar feo")
                    fail.play()        
        contador = contador +1     
    contador = 0 
    llave = True           
    while contador < len(hornos) and llave == True:
        if colision(prota, hornos[int(contador)], nx, ny) == True:
            print("interacicion con:!"+hornos[int(contador)].name)
            if hornos[int(contador)].objeto != None and hornos[int(contador)].comida_lista  and prota.objeto == None:
                prota.setObjeto(hornos[int(contador)].getObjeto())
                hornos[int(contador)].setObjeto(None)
                bien.play(1)
                llave = False
            else:
                print("sonar feo")
                fail.play()    
        contador = contador +1
    contador = 0    
    llave = True           
    while contador < len(basuras) and llave == True: 
        if colision(prota, basuras[int(contador)], nx, ny) == True:
            prota.setObjeto(None)
            llave = True
            papelera.play(1)
        contador = contador +1 
    return puntaje            
#---------------------------------------------------------------------------
def tocar_portal(prota, portales):
    contador = 0
    while contador < len(portales):
        if prota.get_espacio().colliderect(portales[contador].get_espacio()):
            prota.x = portales[contador].x2-100
            prota.y =portales[contador].y2
            return prota
        elif prota.get_espacio().colliderect(portales[contador].get_espacio2()):
            prota.x = portales[contador].x1 + 100 
            prota.y = portales[contador].y1
            return prota
        contador = contador +1
    return prota    
pygame.init()
nsprite=1
limite_X_m = 0
limite_Y_m = 0
limite_X = 1000
limite_y = 750
tiempo_juego = 0
numero_comidas = 0
coef_calma = 5
coef_violencia = 1
nivel = 1
n_sprite_portal = 1
puntaje = int("0")
ventana = pygame.display.set_mode((limite_X, limite_y))
pygame.display.set_caption("RESTAURANT DISTRI II")
myfont = pygame.font.SysFont("textos", 13)
puntajeFont = pygame.font.SysFont("puntajes", 20)
#musica
#-----------------------
tema_principal = pygame.mixer.Sound("Audio/seels 2.wav")
tema_principal.play(-1)
fail = pygame.mixer.Sound("Audio/error.wav")
bien = pygame.mixer.Sound("Audio/bien.wav")
papelera = pygame.mixer.Sound("Audio/papelera.wav")
game_over = pygame.mixer.Sound("Audio/GameOver.wav")
prreo = pygame.mixer.Sound("Audio/perreo.wav")
nivel_up = pygame.mixer.Sound("Audio/nivel.wav")
#-----------------------
run = True
#---------------------------------------------------------------------------
prota = protagonista("Brian") 
clientes = [ ]
hornos = [ ]
basuras = [ ]
portales = [ ]
lista_comidas = ["cheescake", "salchipapa", "arepas", "hamburguesa", "remolacha","sandwich", "kokoro"]
clientes.append(Client("1", 50, 200, 3500, lista_comidas[0]))
clientes[0].activo = True
clientes.append(Client("2", 250, 200,  2500, lista_comidas[1]))
clientes.append(Client("3", 450, 200,  2500, lista_comidas[2]))
clientes.append(Client("4", 650, 200,  2500, lista_comidas[3]))
clientes.append(Client("5", 50, 400,  2500, lista_comidas[3]))
clientes.append(Client("6", 250, 400,  5000, lista_comidas[1]))
clientes.append(Client("7", 450, 400,  5000, lista_comidas[2]))
clientes.append(Client("8", 650, 400,  4000, lista_comidas[3]))
#clientes.append(Client("9", 800, 300, 100, 6000, lista_comidas[3]))
hornos.append(Horno("horno de cheescake", 30, 10, lista_comidas[0], 60))
hornos[0].activo = True
hornos.append(Horno("horno de salchipapa",  150, 10, lista_comidas[1], 80))
hornos.append(Horno("horno de arepas",270, 10, lista_comidas[2], 80))
hornos.append(Horno("horno de hamburguesa",390, 10, lista_comidas[3], 100))
hornos.append(Horno("horno de remolacha",510, 10, lista_comidas[4], 150))
hornos.append(Horno("horno de sandwich",630, 10, lista_comidas[5], 300))
hornos.append(Horno("horno de vidas",750, 10, lista_comidas[6], 400))
basuras.append(thrash(250, 600))
#basuras.append(thrash(100, 600))
#basuras.append(thrash(200, 600))
portales.append(Portal(10,300, 900, 300, "azul"))
#portales.append(Portal(850,130, 490, 580, "verde"))
portales.append(Portal(10,580, 850, 130, "verde"))
#---------------------------------------------------------------------------
while run:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Se sale del juego
            run = False  
    #Controles:
    #----------------------------------------
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and prota.y > limite_Y_m:
        prota.orientacion = "Up"
        nsprite = nsprite +1
        if nsprite == 3:
            nsprite = 1 
        if revisar_colisiones_prota(prota, clientes+ hornos + basuras, 0, -10):
            prota.movimiento(0,-10)
    if key[pygame.K_DOWN] and prota.y < limite_y:
        prota.orientacion = "Down"
        nsprite = nsprite +1
        if nsprite == 3:
            nsprite = 1         
        if revisar_colisiones_prota(prota, clientes + hornos + basuras, 0, 10):
            prota.movimiento(0,10)
    if key[pygame.K_LEFT] and prota.x > limite_X_m:
        prota.orientacion = "Left"
        nsprite = nsprite +1
        if nsprite == 3:
            nsprite = 1         
        if revisar_colisiones_prota(prota, clientes + hornos + basuras, -10, 0):
            prota.movimiento(-10,0)             
    if key[pygame.K_RIGHT] and prota.x < limite_X:
        prota.orientacion = "Right"
        nsprite = nsprite +1
        if nsprite == 3:
            nsprite = 1            
        if revisar_colisiones_prota(prota, clientes + hornos +basuras, 10, 0):
            prota.movimiento(10,0)
    prota = tocar_portal(prota, portales)        
    #interaccion         
    if key[pygame.K_SPACE]:
        print("...")
        prota.especial = True
        puntaje = interaccion(prota, clientes, hornos, basuras, puntaje)   
    ventana.fill((0, 0, 0))
    prota.dibujar(ventana, myfont, nsprite)
    contador =0
    while contador < len(clientes):
        clientes[int(contador)].dibujar(ventana, myfont, coef_calma, coef_violencia)
        if clientes[int(contador)].game_over == True:
            tema_principal.stop()
            game_over.play()
            pygame.time.delay(1000)
            run = False
        contador = contador+1    
    contador =0
    while contador < len(hornos):
        hornos[int(contador)].dibujar(ventana, myfont)
        hornos[int(contador)].cocinar()
        contador = contador+1
    contador = 0    
    while contador < len(basuras):
        basuras[int(contador)].dibujar(ventana, myfont)
        contador = contador+1
    contador = 0    
    while contador < len(portales):
        portales[int(contador)].dibujar(ventana, n_sprite_portal)
        n_sprite_portal = n_sprite_portal+1
        if n_sprite_portal ==5:
            n_sprite_portal =1
        contador = contador+1      
    texto = puntajeFont.render("tiempo juego:"+str(tiempo_juego), 1, (0, 255, 255))
    ventana.blit(texto, (850, 20))
    texto = puntajeFont.render("puntaje:"+str(puntaje), 1, (0, 255, 255))
    ventana.blit(texto, (850, 40))
    texto = puntajeFont.render("Nivel:"+str(nivel), 1, (0, 255, 255))
    ventana.blit(texto, (850, 60))                             
    pygame.display.update()
    #Niveles
    if puntaje >= 4000 and nivel ==1:
        clientes[1].activo = True
        clientes[1].antojo = lista_comidas[random.randint(0, numero_comidas)]
        coef_calma = 4
        coef_violencia = 1
        nivel = 2
        nivel_up.play()
    if puntaje >= 16000 and nivel ==2:
        clientes[2].activo = True
        clientes[2].antojo = lista_comidas[random.randint(0, numero_comidas)]
        hornos[1].activo = True
        coef_calma = 4
        coef_violencia = 2
        nivel = 3
        numero_comidas = numero_comidas+1
        nivel_up.play()
    if puntaje >= 25000 and nivel ==3:
        clientes[3].activo = True
        clientes[3].antojo = lista_comidas[random.randint(0, numero_comidas)]
        hornos[2].activo = True
        numero_comidas = numero_comidas+1
        coef_calma = 3
        coef_violencia = 3
        nivel = 4
        nivel_up.play() 
    if puntaje >= 40000 and nivel ==4:
        clientes[4].activo = True
        clientes[4].antojo = lista_comidas[random.randint(0, numero_comidas)]
        hornos[3].activo = True
        hornos[4].activo = True
        coef_calma = 3
        coef_violencia = 4
        nivel = 5
        numero_comidas = numero_comidas+2
        nivel_up.play()
    if puntaje  >= 80000 and nivel ==5:
        tema_principal.stop()
        prreo.play(-1)
        clientes[5].activo = True
        clientes[5].antojo = lista_comidas[random.randint(0, numero_comidas)]
        nivel = 6
        coef_calma = 3
        coef_violencia = 5
        nivel_up.play()
    if puntaje  >= 200000 and nivel ==6:
        prreo.stop()
        tema_principal.play(-1)
        clientes[6].activo = True
        clientes[6].antojo = lista_comidas[random.randint(0, numero_comidas)]
        nivel = 7
        nivel_up.play()
    if puntaje >= 500000 and nivel ==7:
        clientes[7].activo = True
        clientes[7].antojo = lista_comidas[random.randint(0, numero_comidas)]
        hornos[5].activo
        numero_comidas = numero_comidas+1
        coef_calma = 2
        coef_violencia = 6
        nivel =8
        nivel_up.play()
    if puntaje >= 1000000 and nivel ==8:
        clientes[8].activo = True
        clientes[8].antojo = lista_comidas[random.randint(0, numero_comidas)]
        nivel =9
        coef_calma = 10
        coef_violencia = 50
        nivel_up.play()                           
    tiempo_juego = tiempo_juego +1
#---------------------------------------------------------------------------    
pygame.quit()  # Se cierra pygame     
#---------------------------------------------------------------------------          
