from principal import *
from configuracion import *

import random
import math



def cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer,repetida):
    #elige una palabra de la lista y la carga en las 3 listas
    # y les inventa una posicion para que aparezca en la columna correspondiente

    azar=random.choice(lista)
    while azar in repetida :
        azar=random.choice(lista)


    opciones=[listaIzq,listaMedio,listaDer]
    posicionxIzq=0
    posicionxMed=0
    posicionxDer=0

    espacio1=[] #ColumnaIzq
    espacio2=[] #ColumnaMed           #Espacio que ocupa una letra, no es igual a la posicion ya que la misma es solo un punto en la pantalla
    espacio3=[] #ColumnaDer

    LimiteInferiorIzq=10
    LimiteSuperiroIzq=233
    LimiteInferiorMed=300
    LimiteSuperiorMed=510       ##Limites que sectoriza cada bloque
    LimiteInferiorDer=540
    LimiteSuperiorDer=785

    for letra in azar:
        eleccion=random.choice(opciones)    #Metiendo en una lista letras de la palabra que sale en azar
        eleccion.append(letra)

        if eleccion==listaIzq:

            if int(len(espacio1))==0:
                posicionxIzq=abs(random.randrange(LimiteInferiorIzq,LimiteSuperiroIzq))
                posicionesIzq.append([posicionxIzq,30])

                for i in range(8):
                    espacio1.append(posicionxIzq+i)  #Ocupo el espacio en un bloque


            else:
                while  posicionxIzq in espacio1 or posicionxIzq+1 in espacio1 or posicionxIzq+2 in espacio1 or posicionxIzq+4 in espacio1 or posicionxIzq+5 in espacio1 or posicionxIzq+6 in espacio1 or posicionxIzq+7 in espacio1 or  posicionxIzq-1 in espacio1 or posicionxIzq-2 in espacio1 or posicionxIzq-3 in espacio1 or posicionxIzq-4 in espacio1 or posicionxIzq-5 in espacio1 :
                    posicionxIzq=abs(random.randrange(LimiteInferiorIzq,LimiteSuperiroIzq))            #Saca una posicon que no este en el espacio
                posicionesIzq.append([posicionxIzq,30])

                for i in range(8):
                    espacio1.append(posicionxIzq+i)   #Ocupo el espacio en un bloque




        if eleccion==listaMedio:


            if int(len(espacio2))==0:
                posicionxMed=abs(random.randrange(LimiteInferiorMed,LimiteSuperiorMed))
                posicionesMedio.append([posicionxMed,30])

                for i in range(8):
                    espacio2.append(posicionxMed+i)  #Ocupo el espacio en un bloque



            else:
                while posicionxMed in espacio2 or posicionxMed+1 in espacio2 or posicionxMed+2 in espacio2 or posicionxMed+4 in espacio2 or posicionxMed+5 in espacio2 or posicionxMed+6 in espacio2 or posicionxMed+7 in espacio2 or posicionxMed-1 in espacio2 or posicionxMed-2 in espacio2 or posicionxMed-3 in espacio2 or posicionxMed-4 in espacio2 or posicionxMed-5 in espacio2 :#posicionx+8 in espacio2 or posicionx+9 in espacio2 or posicionx+10 in espacio2 or posicionx-1 in espacio2 or posicionx-2 in espacio2 or posicionx-3 in espacio2 or posicionx-4 in espacio2 or posicionx-5 in espacio2 :
                    posicionxMed=abs(random.randrange(LimiteInferiorMed,LimiteSuperiorMed))            #Saca una posicon que no este en el espacio
                posicionesMedio.append([posicionxMed,30])
                for i in range(8):
                    espacio2.append(posicionxMed+i) #Ocupo el espacio en un bloque








        if eleccion==listaDer:





            if int(len(espacio3))==0:
                posicionxDer=abs(random.randrange(LimiteInferiorDer,LimiteSuperiorDer))
                posicionesDer.append([posicionxDer,30])
                for i in range(8):
                    espacio3.append(posicionxDer+i)  #Ocupo el espacio en un bloque



            else:
                while posicionxDer in espacio3 or posicionxDer+1 in espacio3 or posicionxDer+2 in espacio3 or posicionxDer+4 in espacio3 or posicionxDer+5 in espacio3 or posicionxDer+6 in espacio3 or posicionxDer+7 in espacio3 or posicionxDer-1 in espacio3 or posicionxDer-2 in espacio3 or posicionxDer-3 in espacio3 or posicionxDer-4 in espacio3 or posicionxDer-5 in espacio3 : #posicionx+8 in espacio3 or posicionx+9 in espacio3 or posicionx+10 in espacio3 or posicionx-1 in espacio3 or posicionx-2 in espacio3 or posicionx-3 in espacio3 or posicionx-4 in espacio3 or posicionx-5 in espacio3 :
                    posicionxDer=abs(random.randrange(LimiteInferiorDer,LimiteSuperiorDer))            #Saca una posicon que no este en el espacio

                posicionesDer.append([posicionxDer,30])
                for i in range(8):
                    espacio3.append(posicionxDer+i)  #Ocupo el espacio en un bloque













    pass








def bajar(lista, posiciones,dificultad,cont):
    # hace bajar las letras y elimina las que tocan el piso
    indices=0

    while indices<int(len(lista)):
        if dificultad==10:
            if cont<120:
                posicion=posiciones[indices]
                posicion[1]=posicion[1]+10
            else:
                posicion=posiciones[indices]
                posicion[1]=posicion[1]+20
        if dificultad==5:
            if cont<120:
                posicion=posiciones[indices]
                posicion[1]=posicion[1]+20
            else:
                posicion=posiciones[indices]
                posicion[1]=posicion[1]+25
        if dificultad==3:
            if cont<120:
                posicion=posiciones[indices]
                posicion[1]=posicion[1]+23
            else:
                posicion=posiciones[indices]
                posicion[1]=posicion[1]+28        #A la lista la estoy manipulando en tiempo real, cambia posiciones
        if posicion[1]>=515:
            lista.pop(indices)
            posiciones.pop(indices)
            indices-=1
        indices+=1
















    pass

def actualizar(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer,cont,repetida,dificultad):
    ## llama a otras funciones para bajar bajar las letras, eliminar las que tocan el piso y
    ## cargar nuevas letras a la pantalla (esto puede no hacerse todo el tiempo para que no se llene de letras la pantalla)

    bajar(listaIzq,posicionesIzq,dificultad,cont)
    bajar(listaMedio,posicionesMedio,dificultad,cont)
    bajar(listaDer,posicionesDer,dificultad,cont)


    if cont%2==0:               ##la dificultad determina las palabras por segundo
        cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer,repetida)     #Cargo una lista cada x segundos

    pass

def estaCerca(elem, lista):









    pass

def Puntos(candidata):
    #devuelve el puntaje que le corresponde a candidata

    consonantesFaciles="rtpsdfghlcvbnmÃ±"
    consonantesDificiles="jkqwxyz"
    vocales="aeiouÃ¡Ã©Ã­Ã³Ãº"
    puntosCandidata=0
    for letra in candidata:
        if letra in vocales:
            puntosCandidata+=1
        if letra in consonantesFaciles:
            puntosCandidata+=2
        if letra in consonantesDificiles:
            puntosCandidata+=5

    return puntosCandidata

    # pass

def procesar(lista, candidata, listaIzq, listaMedio, listaDerecha,repetida,largoPalabra):
    #chequea que candidata sea correcta en cuyo caso devuelve el puntaje y 0 si no es correcta
    sonidoacierto=pygame.mixer.Sound("correcto2.wav") #sonido
    sonidoequivocado=pygame.mixer.Sound("equivocado2.wav")
    Chequeo= esValida(lista, candidata, listaIzq, listaMedio, listaDerecha,repetida,largoPalabra)
    if Chequeo:
        sonidoacierto.play()
        CantidadPuntos=Puntos(candidata)

    else:
        sonidoequivocado.play()
        CantidadPuntos=0



    return CantidadPuntos
    # pass





def esValida(lista, candidata, listaIzq, listaMedio, listaDerecha,repetida,largoPalabra):
    #devuelve True si candidata cumple con los requisitos
    EstanLetras=0
    casoIzq=True
    casoMed=True
    casoDer=True
    for letra in candidata:
        if letra in listaIzq and casoIzq:
            EstanLetras+=1
        else:
            if letra in listaMedio and casoMed:
                EstanLetras+=1
                casoIzq=False
            else:
                if letra in listaDerecha and casoDer:
                    EstanLetras+=1
                    casoIzq=False
                    casoMed=False

    if EstanLetras==int(len(candidata) ):
        if candidata in lista and candidata not in repetida and int(len(candidata))>=largoPalabra:
            repetida.append(candidata)
            salida=True
        else:
            salida=False
    else:
        salida=False


    return salida

    # pass
