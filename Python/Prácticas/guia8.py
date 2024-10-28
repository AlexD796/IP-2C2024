import random
from queue import Queue as Cola
from queue import LifoQueue as Pila
p = Pila ()
c = Cola
p . put (1) # apilar
elemento = p . get () # desapilar
p . empty () # vacia ?

def generaṛ_nros_al_azar (c:int, desde:int,hasta:int)->Pila[int]:
    res:Pila = Pila()
    for i in range (c):
        aleatorio:int = random.randint (desde,hasta) #genera un numero random
        res.put(aleatorio) #ese numero "aleatorio" lo pone en la respuesta
    return res
    

def verPila (p:Pila) -> None:
    contenedor:Pila= Pila()
    numero:int #variable estacional
    while not p.empty():
        numero= p.get()
        print (numero)
        contenedor.put(numero) #al terminar el proceso, me printea la pila alrevez
        
    while not contenedor.empty ():
        p.put(contenedor.get()) # aca la vuelve poner en la pila (igual que la original)

#var = generaṛ_nros_al_azar (5,1,100)
#verPila(var) 

#print(var.queue) 
#print(generaṛ_nros_al_azar(5,1,100).queue) #ver cheating xq es una lista pero esta inclinada, el primer elemento es el ultimo de la lista

def buscar_el_maximo (p:Pila[int]) -> int: #suponemos que no esta vacia, sino metemos un if para checkear
    contenedor: Pila[int] = Pila ()   
    maximo:int= p.get() #guardar el get en una variable para no perder el valor
    contenedor.put (maximo)
    
    while not p.empty():
        elementoActual=p.get()
        if maximo < elementoActual:
            maximo = elementoActual
        contenedor.put (elementoActual)
        
    while not contenedor.empty():
        p.put(contenedor.get())
        
    return maximo

#print (buscar_el_maximo ([2,3,4,5])) #MAL... LA PILA NO TIENE ESA FORMA...
#pila=Pila()
#pila.put(2555)
#pila.put(8)
#pila.put(77)
#pila.put(293)
#pila.put(0)
#print (buscar_el_maximo (pila))

def armar_secuencia_bingo () -> Cola[int]:
    lista: list[int] = random.shuffle ([0,...,100]) #ya desorganiza la lista dada pero no la genera CREO
    cola: Cola[int] = Cola ()
    i:int=0
    numero=p.get ()
    while i <=12 :
       cola.put (numero)
       i+=1
    return cola

var = armar_secuencia_bingo ()
verPila(var) 

print(var.queue) 

def armar_secuencia_de_bingo () -> Cola[int]:
    res: Cola[int] = Cola ()
    bolillero: list[int] = [] #ya desorganiza la lista dada pero no la genera CREO
   
    for i in range(0,100):
       bolillero.append(i)
       
    random.shuffle(bolillero) #desordenar lista
    
    i = 0
    while i < len(bolillero):
       res.put(bolillero[i])
       i+=1
       
    return res

print(armar_secuencia_de_bingo().queue)

def jugar_carton_de_bingo(carton:list[int], bolillero:Cola[int])->int:
    bingo:int=0
    jugadas:int=0
    contenedor:Cola[int] = Cola()
    
    while bingo < len (carton):
        jugadas+=1
        bolita_actual= bolillero.get()
        contenedor.put(bolita_actual())
        
        if bolita_actual in carton:
            bingo += 1
            
    while not bolillero.empty (): 
        contenedor.put(bolillero.get())
        
    while not contenedor.empty(): #reconstruyo bolillero incial
        bolillero.put(contenedor.get())
        
    return jugadas

print(jugar_carton_de_bingo)


#>>> a = {} inicializo diccionario
#>>>a["clave1"] = "valor1"
#a["clave"] = [1,2,3]
#>>>a devuelve [["clave1"],[1,2,3]]
    
#def 
    
