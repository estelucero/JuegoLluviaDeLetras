#-*- coding: utf-8 -*-
import pygame, sys
from pygame import *
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *

from configuracion import *
from funcionesVACIAS import *
from extras import *
import time

menu = pygame.display.set_mode((ANCHO, ALTO),0,32)
pantallaDespuesde=pygame.display.set_mode((ANCHO, ALTO),0,32)
creditos=pygame.display.set_mode((ANCHO, ALTO),0,32)
juego=pygame.display.set_mode((ANCHO, ALTO),0,32)
record=pygame.display.set_mode((ANCHO, ALTO),0,32)
opciones=pygame.display.set_mode((ANCHO, ALTO),0,32)
screen = pygame.display.set_mode((ANCHO, ALTO))


font = pygame.font.SysFont("none", 40)
font1 = pygame.font.SysFont("none", 30)
font2 = pygame.font.SysFont("none", 28)
font3 = pygame.font.SysFont("none", 26)


sonidoclick=pygame.mixer.Sound("click5.ogg")

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False
musica=True
def main_menu(persona,puntos,musica):

    click = False
    if persona !="" and puntos !="":
        archivoRecords= open("records","a")
        archivoRecords.write(str(persona)+"\n")
        archivoRecords.write(str(puntos)+"\n")
        archivoRecords.close()

    archivoRecords= open("records","r")
    listaRecords=[]

    for linea in archivoRecords.readlines():
         listaRecords.append(linea[0:-1])
    archivoRecords.close()



    pygame.mixer.music.load("Child's Nightmare.ogg")

    if musica==True:
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)

    while True:

        menu.fill((235,235,235))        ##Color pantalla


        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(300, 100, 200, 50)#Iniciar
        button_2 = pygame.Rect(300, 200, 200, 50)#Opciones    ##Crea los botones

        button_4 = pygame.Rect(300, 300, 200, 50)#Records
        button_5 = pygame.Rect(600, 500, 150, 50)#Salir
##        Prueba = pygame.Rect(300, 400, 100, 50)
        cartelMenu=pygame.Rect(160, 10, 500, 60)       #Cartel de el menu




        if button_1.collidepoint((mx, my)):
            if click:
                sonidoclick.play()
                game(musica)
        if button_2.collidepoint((mx, my)):
            if click:
                sonidoclick.play()                           #EL CLICK DE LOS BOTONES
                musica=options(musica)

##        if Prueba.collidepoint((mx, my)):
##
##            if click:
##                pantallaDespuesDeJugar(12,musica)



        if button_4.collidepoint((mx, my)) :
            if click:
                sonidoclick.play()
                records(listaRecords)



        if button_5.collidepoint((mx, my))  :

            if click:
                sonidoclick.play()
                pygame.quit()
                sys.exit()







        pygame.draw.rect(menu, (50, 100, 100), button_1)
        pygame.draw.rect(menu, (50, 100, 100), button_2)     ##Dibuja los botones

        pygame.draw.rect(menu, (50, 100, 100), button_4)
        pygame.draw.rect(menu, (50, 100, 100), button_5)
##        pygame.draw.rect(menu, (50, 100, 100), Prueba)

        pygame.draw.rect(menu, (50, 100, 100), cartelMenu)

        draw_text('INICIAR', font1, (255, 255, 255), menu, 365, 115)              #Dibujo letras del menu
        draw_text('LLUVIA DE LETRAS', font, (255, 255, 255), menu, 280, 25)         #Texto del menu principal
        draw_text('OPCIONES', font1, (255, 255, 255), menu, 347, 215)             #TECTO DE OPCIONES
        draw_text('RECORDS', font1, (255, 255, 255), menu, 348, 315)              #TEXTO DE RECORDS
        draw_text('SALIR', font1, (255, 255, 255), menu, 646, 515)



##        if Prueba.collidepoint((mx, my)):
##            pygame.draw.rect(menu, (50, 150, 100), Prueba)


        if button_1.collidepoint((mx, my)):

            pygame.draw.rect(menu, (50, 150, 100), button_1)
            draw_text('INICIAR', font1, (255, 255, 255), menu, 365, 115)


        if button_2.collidepoint((mx, my)):                                                    #Hace que se pongan colores
            pygame.draw.rect(menu, (50, 150, 100), button_2)
            draw_text('OPCIONES', font1, (255, 255, 255), menu, 347, 215)

        if button_4.collidepoint((mx, my)):
            pygame.draw.rect(menu, (50, 150, 100), button_4)
            draw_text('RECORDS', font1, (255, 255, 255), menu, 348, 315)

        if button_5.collidepoint((mx, my)):
            pygame.draw.rect(menu, (50, 150, 100), button_5)
            draw_text('SALIR', font1, (255, 255, 255), menu, 646, 515)





        click = False



        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def game(musica):
    running = True
    click = False
    while running:
        juego.fill((235,235,235))

        mx, my = pygame.mouse.get_pos()

        cartelDificultad=pygame.Rect(160, 10, 500, 60)

        button_6 = pygame.Rect(300, 100, 200, 50)#Facil
        button_7 = pygame.Rect(300, 200, 200, 50)#Medio
        button_8 = pygame.Rect(300, 300, 200, 50)#Dificil
        button_9 = pygame.Rect(600, 450, 100, 50)#Atras

        if button_9.collidepoint((mx, my)):
            if click:
                sonidoclick.play()
                return


        if button_6.collidepoint((mx, my)): #Dificultad Facil
            if click:
                sonidoclick.play()
                jugar(10,0,musica)
        if button_7.collidepoint((mx, my)): #Dificultad Medio
            if click:
                sonidoclick.play()
                jugar(5,3,musica)
        if button_8.collidepoint((mx, my)):#Dificultad Dificil
            if click:
                sonidoclick.play()
                jugar(3,5,musica)

        pygame.draw.rect(juego, (50, 100, 100), cartelDificultad)
        pygame.draw.rect(juego, (50, 100, 100), button_7)
        pygame.draw.rect(juego, (50, 100, 100), button_6)          #Carteles de dificultad
        pygame.draw.rect(juego, (50, 100, 100), button_8)
        pygame.draw.rect(juego, (50, 100, 100), button_9)
        draw_text('DIFICULTAD', font, (255, 255, 255), juego, 325, 25)
        draw_text('FACIL', font, (255, 255, 255), juego, 360, 113)
        draw_text('MEDIO', font, (255, 255, 255), juego, 357, 213)
        draw_text('DIFICIL', font, (255, 255, 255), juego, 355, 313)
        draw_text('ATRAS', font1, (255, 255, 255), juego, 615, 466)

        if button_9.collidepoint((mx, my)):
            pygame.draw.rect(record, (50, 150, 100), button_9)
            draw_text('ATRAS', font1, (255, 255, 255), juego, 615, 466)

        if button_6.collidepoint((mx, my)):
            pygame.draw.rect(juego, (50, 150, 100), button_6)
            draw_text('FACIL', font, (255, 255, 255), juego, 360, 113)

        if button_7.collidepoint((mx, my)):
            pygame.draw.rect(juego, (50, 150, 100), button_7)
            draw_text('MEDIO', font, (255, 255, 255), juego, 357, 213)

        if button_8.collidepoint((mx, my)):
            pygame.draw.rect(juego, (50, 150, 100), button_8)
            draw_text('DIFICIL', font, (255, 255, 255), juego, 355, 313)

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def options(musica):

    tocado=musica
    noTocado=100
    running = True
    click = False
    while running:
        opciones.fill((235,235,235))

        px, py = pygame.mouse.get_pos()


        cartelOpciones=pygame.Rect(260, 10, 300, 60)
        musica=pygame.Rect(150, 150, 200, 60)
        musicaSi=pygame.Rect(600, 150, 70, 60)
        musicaNo=pygame.Rect(680, 150, 70, 60)
        creditos=pygame.Rect(150, 250, 200, 60)
        atras =pygame.Rect(600, 450, 100, 50)



        if atras.collidepoint((px, py)):
            if click:
                sonidoclick.play()

                return tocado
        if creditos.collidepoint((px, py)):
            if click:
                sonidoclick.play()
                credito()




        pygame.draw.rect(opciones, (50, 100, 100), cartelOpciones)
        pygame.draw.rect(opciones, (50, 100, 100), musica)
        pygame.draw.rect(opciones, (50, noTocado, 100), musicaSi)
        pygame.draw.rect(opciones, (50, noTocado, 100), musicaNo)
        pygame.draw.rect(opciones, (50, 100, 100), creditos)
        pygame.draw.rect(opciones, (50, 100, 100), atras)
        draw_text('OPCIONES', font, (255, 255, 255), opciones, 340, 25)
        draw_text('ATRAS', font1, (255, 255, 255), juego, 615, 466)
        draw_text('MUSICA', font, (255, 255, 255), opciones, 197, 167)
        draw_text('SI', font, (255, 255, 255), opciones, 620, 167)
        draw_text('NO', font, (255, 255, 255), opciones, 697, 167)
        draw_text('CREDITOS', font, (255, 255, 255), opciones, 180, 267)

        if musicaNo.collidepoint((px, py)):
            if click:
                sonidoclick.play()

                pygame.mixer.music.stop()
                tocado=False


        if musicaSi.collidepoint((px, py)):
            if click:
                if tocado==False:
                    sonidoclick.play()

                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.2)
                    tocado=True

        if atras.collidepoint((px, py)):
            pygame.draw.rect(record, (50, 150, 100), atras)
            draw_text('ATRAS', font1, (255, 255, 255), juego, 615, 466)

        if creditos.collidepoint((px, py)):
            pygame.draw.rect(opciones, (50, 150, 100), creditos)
            draw_text('CREDITOS', font, (255, 255, 255), opciones, 80, 267)

        if musicaSi.collidepoint((px, py)):
            pygame.draw.rect(opciones, (50, 150, 100), musicaSi)
            draw_text('SI', font, (255, 255, 255), opciones, 620, 167)

        if musicaNo.collidepoint((px, py)):
            pygame.draw.rect(opciones, (50, 150, 100), musicaNo)
            draw_text('NO', font, (255, 255, 255), opciones, 697, 167)

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def burbuja(scores,nombre):
    for i in range(1,len(scores)):
        for j in range(0,len(scores)-i):
            if(int(scores[j+1]) > int(scores[j])):
                aux = scores[j];
                scores[j] = scores[j+1];
                scores[j+1] = aux;

                aux_nombre=nombre[j];
                nombre[j]=nombre[j+1];
                nombre[j+1]=aux_nombre;
    return scores, nombre




def records(l):
    running = True
    click = False
    personas=[]
    scores=[]
    indices=[]
    espacio=""
    puntos="............................."
    puntos2="............................"
    fuente=font
    color=(0,0,0)
    x=250
    for i in range(len(l)):
        if i %2==0:
            personas.append(l[i])
        else:
            scores.append(l[i])

    burbuja(scores,personas)


    for pp in range(len(personas)):
        if int(len(personas[pp]))==2:
            personas[pp]=personas[pp]+"   "
        if int(len(personas[pp]))==1:           #Le agrego un espacio
            personas[pp]=personas[pp]+"     "

    while running:
        record.fill((235,235,235))
        sx, sy = pygame.mouse.get_pos()


        cartelRecords=pygame.Rect(280, 10, 300, 60)

        atras = pygame.Rect(600, 450, 100, 50)


        if atras.collidepoint((sx, sy)):
            if click:
                sonidoclick.play()
                return




        pygame.draw.rect(record, (50, 100, 100), cartelRecords)
        pygame.draw.rect(record, (50, 100, 100), atras)

        draw_text('RECORDS', font, (255, 255, 255), record, 365, 25)
        draw_text('ATRAS', font1, (255, 255, 255), juego, 615, 466)




        if int(len(personas))>=1:
            texto1="1."+str(personas[0])+espacio+puntos+str(scores[0])
            draw_text(texto1.upper(), fuente, color, record, x-2, 100)

        if int(len(personas))>=2:
            texto2="2."+str(personas[1])+espacio+puntos+str(scores[1])
            draw_text(texto2.upper(), fuente, color, record, x, 120)
        if int(len(personas))>=3:
            texto3="3."+str(personas[2])+espacio+puntos+str(scores[2])
            draw_text(texto3.upper(), fuente, color, record, x-4, 140)
        if int(len(personas))>=4:
            texto4="4."+str(personas[3])+espacio+puntos+str(scores[3])
            draw_text(texto4.upper(), fuente, color, record, x, 160)

        if int(len(personas))>=5:
            texto5="5."+str(personas[4])+espacio+puntos+str(scores[4])
            draw_text(texto5.upper(), fuente, color, record, x, 180)
        if int(len(personas))>=6:
            texto6="6."+str(personas[5])+espacio+puntos+str(scores[5])
            draw_text(texto6.upper(), fuente, color, record, x, 200)
        if int(len(personas))>=7:
            texto7="7."+str(personas[6])+espacio+puntos+str(scores[6])
            draw_text(texto7.upper(), fuente, color, record, x, 220)

        if int(len(personas))>=8:
            texto8="8."+str(personas[7])+espacio+puntos+str(scores[7])
            draw_text(texto8.upper(), fuente, color, record, x, 240)

        if int(len(personas))>=9:
            texto9="9."+str(personas[8])+espacio+puntos+str(scores[8])
            draw_text(texto9.upper(), fuente, color, record, x, 260)
        if int(len(personas))>=10:
            texto10="10."+str(personas[9])+espacio+puntos+str(scores[9])
            draw_text(texto10.upper(), fuente, color, record, x-12, 280)


        if atras.collidepoint((sx, sy)):
            pygame.draw.rect(record, (50, 150, 100), atras)
            draw_text('ATRAS', font1, (255, 255, 255), juego, 615, 466)

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)



def credito():
    running = True
    click = False
    while running:
        creditos.fill((235,235,235))
        tx, ty = pygame.mouse.get_pos()


        cartelRecords=pygame.Rect(50, 120, 400, 210)

        atras = pygame.Rect(380, 420, 100, 50)


        if atras.collidepoint((tx, ty)):
            if click:
                sonidoclick.play()
                return




        pygame.draw.rect(creditos, (50, 100, 100), cartelRecords)
        pygame.draw.rect(creditos, (50, 100, 100), atras)

        draw_text('HECHO POR ESTEBAN EZEQUIEL LUCERO', font2, (255, 255, 255), creditos, 50, 200)
        draw_text('UNIVERSIDAD GENERAL SARMIENTO(UNGS)', font3, (255, 255, 255), creditos, 50, 230)
        draw_text('ATRAS', font1, (255, 255, 255), creditos, 395, 435)


        if atras.collidepoint((tx, ty)):
            pygame.draw.rect(record, (50, 150, 100), atras)
            draw_text('ATRAS', font1, (255, 255, 255), record, 395, 435)












        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def pantallaDespuesDeJugar(puntos,musica):
    running = True
    persona=""
    click = False


    while running:
        pantallaDespuesde.fill((235,235,235))
        cx, cy = pygame.mouse.get_pos()




        cartelRecords=pygame.Rect(280, 10, 300, 60)
        irAlMenu = pygame.Rect(330, 420, 200, 50)

        cartelLetras=pygame.Rect(230, 120, 400, 210)
        cartelEscribir=pygame.Rect(336, 240, 200, 50)

        if irAlMenu.collidepoint((cx, cy)):
            if click:

                sonidoclick.play()
                main_menu(persona,puntos,musica)






        pygame.draw.rect(pantallaDespuesde, (50, 100, 100), cartelRecords)
        pygame.draw.rect(pantallaDespuesde, (50, 100, 100), irAlMenu)

        pygame.draw.rect(pantallaDespuesde, (50, 100, 100), cartelLetras)
        pygame.draw.rect(pantallaDespuesde, (255, 255, 255), cartelEscribir,2)
        draw_text('FIN DEL JUEGO', font, (255, 255, 255), pantallaDespuesde, 332, 25)
        draw_text('IR AL', font1, (255, 255, 255), pantallaDespuesde, 405, 425)
        draw_text('MENU PRICINPAL', font1, (255, 255, 255), pantallaDespuesde, 345, 445)

        draw_text('INGRESE SU APODO', font, (255, 255, 255), pantallaDespuesde, 298, 180)

        draw_text('SU RECORD ES:'+str(puntos), font, (255, 255, 255), pantallaDespuesde, 313, 140)
        personamayus=persona.upper()
        espacioRecords=font.render(personamayus[:3],True,(255,255,255))
        pantallaDespuesde.blit(espacioRecords,(407,250))

        if irAlMenu.collidepoint((cx, cy)):
            pygame.draw.rect(pantallaDespuesde, (50, 150, 100), irAlMenu)
            draw_text('IR AL', font1, (255, 255, 255), pantallaDespuesde, 405, 425)
            draw_text('MENU PRICINPAL', font1, (255, 255, 255), pantallaDespuesde, 345, 445)
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            if event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key==pygame.K_BACKSPACE:
                    persona=persona[0:-1]
                else:
                    if int(len(persona))<=2:            #hago que si o si use tres letras
                        persona+=event.unicode
                    else:
                        persona=persona


        pygame.display.update()
        mainClock.tick(60)




def jugar(dificultad,largoPalabra,musica):
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        #pygame.mixer.init()

        #Preparar la ventana
        pygame.display.set_caption("Armar palabras...")
        # screen = pygame.display.set_mode((ANCHO, ALTO))
        opciones.fill((232,232,235))
        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial

        puntos = 0
        candidata = ""
        listaIzq = []
        listaMedio = []
        listaDer = []
        posicionesIzq = []
        posicionesMedio = []
        posicionesDer = []
        lista = []
        repetida=[]

        archivo= open("lemario.txt","r")   #Aca abre el archivo, carga palabras, y las agrega a una lista
        for linea in archivo.readlines():
            lista.append(linea[0:-1])

        cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer,repetida)##aca cargar la lista con palabras
        dibujar(screen, candidata, listaIzq, listaMedio, listaDer, posicionesIzq ,
                posicionesMedio, posicionesDer, puntos,segundos)
        cont=0

        while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            if True:
            	fps = 3

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    candidata += letra
                    if e.key == K_BACKSPACE:
                        candidata = candidata[0:len(candidata)-1]
                    if e.key == K_RETURN:
                        puntos += procesar(lista, candidata, listaIzq, listaMedio, listaDer,repetida,largoPalabra)#Funcion a desarrollar
                        candidata = ""

            segundos = TIEMPO_MAX -cont/(3)

            #Limpiar pantalla anterior
            screen.fill(COLOR_FONDO)

            #Dibujar de nuevo todo
            dibujar(screen, candidata, listaIzq, listaMedio, listaDer, posicionesIzq ,
                posicionesMedio, posicionesDer, puntos,segundos)

            pygame.display.flip()
            cont+=1

            actualizar(lista, listaIzq, listaMedio, listaDer, posicionesIzq,
                posicionesMedio, posicionesDer,cont,repetida,dificultad)




            if segundos<=0:
                pantallaDespuesDeJugar(puntos,musica)
        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return


















persona=""
puntos=""
main_menu(persona,puntos,musica)

