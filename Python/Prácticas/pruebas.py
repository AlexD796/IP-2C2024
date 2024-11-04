import random
from queue import Queue as Cola
from queue import LifoQueue as Pila
p = Pila ()
c = Cola ()
p . put (1) # apilar
elemento = p . get () # desapilar
p . empty () # esta vacia ?

def mostrar(capitales):  
    #for p,c in capitales.items():  # recorre diccionario
      #  print(p,":",c)

    #for e in capitales.items(): # otra forma más incomoda
        #print("Pais:" + e[0] + " Capital:" + e[1])

    for k in capitales.keys(): 
      print(k + ": " + capitales[k])  # recorre las claves
      #print(capitales[k])

    if 'Portugal' in capitales:  # comprueba si existe clave
        print('\nCapital Portugal:', capitales['Portugal'])

    #print('\nHay {0} países\n'.format(len(capitales)))  # 'Hay 2 países'
    
    for pais, capital in capitales.items():  # recorre diccionario
            print('Capital de {1}:{0} '.format(capital, pais)) 

    print('\nHay {0} países\n'.format(len(capitales))) #very useful

capitales:dict[str,str] = {'Chile':'Santiago', 'España':'Madrid', 'Francia':'París'}
#mostrar(capitales)

infoPaisFrancia = {'Capital':'París',
                'Campeonatos de Mundo':2}

infoPaisArgentina = {'Capital':'Buenos Aires',
                'Campeonatos de Mundo':3}

infoPaisChile = {'Capital':'Santiago',
                'Campeonatos de Mundo':0}

infoPaises = {'Chile': infoPaisChile ,
              'Argentina': infoPaisArgentina,
              'Francia':infoPaisFrancia}

#def aVer ():
for pais, info in infoPaises.items():
        print("Información de " + pais + ": ")
        for clave, valor in info.items():
            print(" - " + clave + ": " + str(valor)) 

print(infoPaises['Chile']['Capital'])