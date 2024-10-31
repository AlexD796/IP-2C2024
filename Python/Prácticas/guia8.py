import random
from queue import Queue as Cola
from queue import LifoQueue as Pila
p = Pila ()
c = Cola ()

#MOSTRAR PILAS Y COLAS
def mostrar_pila(p: Pila[int]) -> None: 
    paux: Pila[int] = Pila()

    while not p.empty():
        elem: int = p.get()
        paux.put(elem)
        print(elem)
    print("-----")

    while not paux.empty():
        p.put(paux.get())

def mostrar_cola(c: Cola[int]) -> None: 
    caux: Cola[int] = Cola()

    while not c.empty():
        elem: int = c.get()
        caux.put(elem)
        print(elem, end=" ") #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    print("-----")

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
  
    for letra in s: 
        contenedor.put(letra)
   
    while not contenedor.empty(): 
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
esta_bien_balanceada("8*(9/3))"),
esta_bien_balanceada("8*(9/3)()") #no se como hacer para que esto de false y varios casos raros dan mal
)"""

#   EJERCICIO 6
def pertenece (s: list[int], e: int) -> bool:
    for i in range (len(s)):
        if s[i] == e:
            return True
    return False

def evaluar_expresion(s:str)->str:
    contenedor=Pila()
   
    for token in s:
        if pertenece ("123456789", token):
            contenedor.put(token)
        if pertenece ("+-/*", token):
            n2=int(contenedor.get()) #SE VUELVE INT EL STR..... SINO NO FUNCIONA
            n1=int(contenedor.get()) #SE VUELVE INT EL STR..... SINO NO FUNCIONA
         
            if token=="+":
                contenedor.put(n1+n2)
            if token=="-":
                contenedor.put(n1-n2)
            if token=="*":
                contenedor.put(n1*n2)
            if token=="/":
                contenedor.put(n1/n2)
   
    return contenedor.get()

#expresion = "3 4 + 5 * 2 -"
#resultado = evaluar_expresion(expresion)
#print(resultado) 

#   EJERCICIO 7
def intercalar(p1:Pila, p2:Pila)-> Pila:
    contenedor1:Pila=Pila()
    contenedor2:Pila=Pila()
    res:Pila=Pila()

    while not p1.empty():
        contenedor1.put(p1.get())

    while not p2.empty():
        contenedor2.put(p2.get())
    
    while not (contenedor1.empty() and contenedor1.empty()):
        res.put(contenedor1.get())
        res.put(contenedor2.get())

    return res
"""
pila1=Pila()
pila2=Pila()

pila1.put(1)
pila1.put(2)
pila1.put(3)
pila1.put(4)
pila1.put(5)
pila1.put(6)

pila2.put(7)
pila2.put(8)
pila2.put(9)
pila2.put(10)
pila2.put(11)
pila2.put(12)

resultado = intercalar (pila1,pila2)

verPila(resultado)
"""
#   EJERCICIO 8
def generar_nros_al_azar2(cantidad: int, desde: int,hasta: int) -> Cola:
    res:Cola=Cola()

    for i in range(cantidad):
        num:int=random.randint (desde,hasta)
        res.put(num)

    return res

#resultado= generar_nros_al_azar2(8,1,100)
#verPila (resultado)

#   EJERCICIO 9
def cantidad_elementos_cola (p : Cola) -> int:
    size:int=0
    contenedor:Cola= Cola ()
  
    while not p.empty():
        contenedor.put(p.get())
        size+=1

    while not contenedor.empty(): #pongo en la pila de a 1 lo del contenedor ¡restauré la variable in p:Pila[int]!
        p.put(contenedor.get())

    return size

#   EJERCICIO 10
def buscar_el_maximo(c : Cola[int]) ->int:
    max:int=c.get()
    contenedor:Cola=Cola()

    while not c.empty():
        num:int=c.get()
        if num > max:
            max=num
        contenedor.put(num)

    while not contenedor.empty():
        c.put(contenedor.get())

    return max

#   EJERCICIO 11
def buscar_nota_minima(c : Cola[str, int]) -> int:
    tuplaMin: tuple[str, int] = c.get()
    contenedor:Cola=Cola()

    while not c.empty():
        elem:tuple[str, int] = c.get()
        if elem[1] < tuplaMin[1]:
            tuplaMin = elem

    while not contenedor.empty():
        c.put(contenedor.get())

    return tuplaMin

#   EJERCICIO 12
def intercalar2(c1:Cola, c2:Cola)->Cola:
    res:Cola=Cola()
    contenedor=Cola()

    while not (c1.empty() and c2.empty()): 
        contenedor.put(c1.get())
        contenedor.put(c2.get())

    return contenedor
"""
cola1=Cola()
cola2=Cola()

cola1.put(1)
cola1.put(2)
cola1.put(3)

cola2.put(4)
cola2.put(5)
cola2.put(6)


lista = intercalar2 (cola1,cola2)

mostrar_cola(lista)
"""

#   EJERCICIO 13
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

#var = armar_secuencia_de_bingo ()
#verPila(var) 

def pertenece (e:int, s:list[int]):
    res:bool=False
    for i in s:
        if e==i:
            res=True
    return res


def jugar_carton_de_bingo(carton:list[int], bolillero:Cola[int])->int:
    bingo:int=0
    jugadas:int=0
    contenedor:Cola[int] = Cola()
    
    while bingo < 12: #Sigo sacando bolillas hasta que marque todos los numeros
        bolilla_sacada:int = bolillero.get()
        contenedor.put(bolilla_sacada)
        if pertenece(bolilla_sacada, carton):
            bingo += 1
        jugadas+=1
            
    while not bolillero.empty (): #Una vez que marque todos, paso todas las bolillas restantes al bolillero auxiliar
        contenedor.put(bolillero.get())
        
    while not contenedor.empty(): #Reconstruyo bolillero incial
        bolillero.put(contenedor.get())
        
    return jugadas

#print(jugar_carton_de_bingo([1,20,21,50,71,22,41,28,9,78,51,91],armar_secuencia_de_bingo()))

#   EJERCICIO 14
def n_pacientes_urgentes(pacientes: Cola[tuple[int, str, str]]) -> int:
    contenedor:Cola=Cola()
    res:int=0

    while not pacientes.empty():
        p=pacientes.get()
        contenedor.put(p)
        if 1<= p[0] <=3:
            res+=1

    while not contenedor.empty():
        pacientes.put(contenedor.get())

    return res

#   EJERCICIO 15
def atencion_a_clientes (clientes: Cola[tuple[str, int, bool, bool]]) -> Cola[tuple[str, int, bool, bool]]:
    res:Cola=Cola()
    prioridad1:Cola=Cola()
    prioridad2:Cola=Cola()
    noPrioridad:Cola=Cola()

    while not clientes.empty():
        persona: tuple[str, int, bool, bool]= clientes.get()
        if persona[3] == True:
            prioridad1.put(persona)
        if persona[3] == False and persona[2] == True:
            prioridad2.put(persona)
        if persona[3] == False and persona[2] == False:
            noPrioridad.put(persona)

    while not prioridad1.empty():
        res.put(prioridad1.get())

    while not prioridad2.empty():
        res.put(prioridad2.get())

    while not noPrioridad.empty():
        res.put(noPrioridad.get())
    
    return res

"""gente = Cola()
gente.put(("a",48,True,False))
gente.put(("b",45,False,True))
gente.put(("c",34,True,True))
gente.put(("d",84,False,False))
gente.put(("e",44,False,True))
gente.put(("f",41,True,True))
gente.put(("g",14,False,False))
gente.put(("h",49,True,False))

mostrar_cola(atencion_a_clientes(gente)) """

#>>> a = {} inicializo diccionario
#>>>a["clave1"] = "valor1"
#a["clave"] = [1,2,3]
#>>>a devuelve [["clave1"],[1,2,3]]
    
#def 


