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

file = open("myfile.txt","w")
L = ["This is Lagos \n","This is Python \n","This is Fcc \n"]

#Asignando ["This is Lagos \n","This is Python \n","This is Fcc \n"]  a 
#la variable L, se puede usar cualquier letra o palabra de tu elección.
#Las variables son contenedores en los que se pueden almacenar valores.
#El \n se coloca para indicar el final de la línea.

file.write("Hello There \n")
file.writelines(L)
file.close()

def invertir_lineas(nombre_archivo : str): #???????????????????????????????????????????????????????????'
    archivo_entrada =  open (nombre_archivo, "r")

    lineas = archivo_entrada.readlines()

    lineas_alrevez = invertir_lineas(lineas)
    
    for linea in lineas_alrevez:
        reverso.write (linea)
    
    reverso.close()
    archivo_entrada.close()

def invertir_lineas (listaLineas: list[str]) -> list[str]:
    res:str=[]
    for i in range (len(listaLineas)-1, -1, -1):
        res.append (listaLineas[i])
    return res

reverso = open("reverso.txt","w")
invertir_lineas("himno.txt")

# declara diccionario
capitales:dict[str,str] = {'Chile':'Santiago',
              'España':'Madrid',
              'Francia':'París'}
              
print('La capital de Chile es', capitales['Chile'])  # 'Santiago'
del capitales['Francia']  # borra el par Francia:París
print('\nHay {0} países\n'.format(len(capitales)))  # 'Hay 2 países'
for pais, capital in capitales.items():  # recorre diccionario