import random
from queue import Queue as Cola
from queue import LifoQueue as Pila
p = Pila ()
c = Cola ()
p . put (1) # apilar
elemento = p . get () # desapilar
p . empty () # esta vacia ?


#EJERCICIO 1
def generaṛ_nros_al_azar (c:int, desde:int,hasta:int)->Pila[int]:
    res:Pila = Pila()
    for i in range (c):
        aleatorio:int = random.randint (desde,hasta) #genera un numero random
        res.put(aleatorio) #ese numero "aleatorio" lo pone en la respuesta
    return res
    

def verPila (p:Pila[int]) -> None:
    contenedor:Pila= Pila() 
    while not p.empty():
        numero:int = p.get() #variable estacional
        print (numero)
        contenedor.put(numero) #al terminar el proceso, me printea la pila en ORDEN!
        
    while not contenedor.empty ():
        p.put(contenedor.get()) # aca la vuelve poner en la pila (igual que la original)

#var = generaṛ_nros_al_azar (5,1,100) #asignamos variable a la funcion
#verPila(var) #así la podemos ver

#print(var.queue) # podemos ver la "lista" de la pila inclinada (primer elementocola = ultimo de la lista)

#print(generaṛ_nros_al_azar(5,1,100).queue) #otra forma cheater de ver en forma lista sin usar funcion verLista

#   EJERCICIO 2

def cantidad_elementos (p : Pila[int]) -> int:
    size:int=0
    contenedor:Pila[int]= Pila ()
    while not p.empty(): #pongo en el contenedor de a 1 lo de la pila
        contenedor.put(p.get())
        size+=1

    while not contenedor.empty(): #pongo en la pila de a 1 lo del contenedor ¡restauré la variable in p:Pila[int]!
        p.put(contenedor.get())

    return size

#p.put (55)
#p.put (32)
#p.put (9)
#p.put (1)
#p.put (6)
#print (cantidad_elementos (p))

#   EJERCICIO 3

def buscar_el_maximo (p:Pila[int]) -> int: #suponemos que no esta vacia, sino metemos un if para checkear
    contenedor: Pila[int] = Pila ()   
    maximo:int= p.get() #guardar el get en una variable para no perder el valor
    
    while not p.empty(): # pongo en el contenedor la pila
        elem = p.get() #SIN ESTA VARIABLE NO FUNCIONA
        if maximo < elem:
            maximo = elem
        contenedor.put (elem)
        
    while not contenedor.empty(): #vuelvo a establecer la pila
        p.put(contenedor.get())
        
    return maximo

#pila=Pila()
#pila.put(2555)
#pila.put(8)
#pila.put(77444)
#pila.put(293)
#pila.put(11111111111)
#print (buscar_el_maximo (pila))

#   EJERCICIO 4

def buscar_nota_maxima (p : Pila[tuple[str, int]])  -> tuple[str,int]:
    contenedor:Pila[tuple[str, int]] = Pila ()
    tuplaNotaMax:tuple[str, int]= p.get ()

    while not p.empty:
        elem = p.get ()
        if elem[1] > tuplaNotaMax[1]:
            tuplaNotaMax=elem    
        contenedor.put (elem)

    while not contenedor.empty(): #variable in -> p (Pila) no puede ser modificada porque es IN
        p.put(contenedor.get())

    return tuplaNotaMax

#pila=Pila()
#pila.put(("mat", 6))
#pila.put(("jor", 9))
#pila.put(("kir", 6))
#pila.put(("fer", 1))
#pila.put(("lau", 10))
#print (buscar_nota_maxima (pila))

#   EJERCICIO 5
def esta_bien_balanceada(s : str) -> bool:
    parentesis:int=0
    res:bool=True
    contenedor:Pila[str]= Pila ()
    for letra in s: #whatever...
        contenedor.put(letra)
   
    while not contenedor.empty: #???? me pone como que esta empty
        letra_sacada = contenedor.get ()
        if letra_sacada == "(":
            parentesis+=1
        if letra_sacada == ")":
            parentesis-=1
        if parentesis !=0: #si lo pongo afuera no funciona porque es una variable por copia no referencia no?¿?¿
            res= False
    
    return res

"""print(
esta_bien_balanceada("3*(1x2)-(5-4)"),
esta_bien_balanceada("7((2x7)"),
esta_bien_balanceada("8*(9/3))")
)"""

#   EJERCICIO 6
def armar_secuencia_bingo () -> Cola[int]:
    lista: list[int] = random.shuffle ([0,...,100]) #ya desorganiza la lista dada pero no la genera CREO
    cola: Cola[int] = Cola ()
    i:int=0
    numero=p.get ()
    while i <=12 :
       cola.put (numero)
       i+=1
    return cola

#var = armar_secuencia_bingo ()
#verPila(var) 

#print(var.queue) 

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

#print(armar_secuencia_de_bingo().queue)

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

#print(jugar_carton_de_bingo)


#>>> a = {} inicializo diccionario
#>>>a["clave1"] = "valor1"
#a["clave"] = [1,2,3]
#>>>a devuelve [["clave1"],[1,2,3]]
    
#def 


