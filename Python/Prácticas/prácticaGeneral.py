from queue import Queue as Cola
from queue import LifoQueue as Pila
p = Pila ()
c = Cola ()

def mostrar_pila (p:Pila[int]):
    contenedor:Pila[int] = Pila()

    while not p.empty():
        valorActual = p.get()
        print (valorActual)
        contenedor.put(valorActual)

    while not contenedor.empty():
        p.put(contenedor.get())


aux = Pila ()

aux.put(8) #principio
aux.put(9)
aux.put(1) #final

#mostrar_pila (aux)

def mostrar_cola (p:Cola[int]):
    contenedor:Pila[int] = Pila()

    while not p.empty():
        valorActual = p.get()
        print (valorActual)
        contenedor.put(valorActual)

    while not contenedor.empty():
        p.put(contenedor.get())

f = Cola ()

f.put(5) #principio
f.put(4)
f.put(7) #final

#mostrar_cola (f)

f.get()

#mostrar_cola (f)

# neuquen -> true 
def palindromoBis (s: str)-> bool:
    palabraInvertida:str = ""

    for letra in s: #n #e
        palabraInvertida = letra + palabraInvertida  #n # e n

    if s == palabraInvertida:
        return True
    
    return False

#print (palindromoBis ("nelwen"))

def CerosIndexPar (s:list[int])-> list[int]:
    for i in range (0, len(s), 2):
        s[i] = 0

    return s

#print (CerosIndexPar([2,4,1,2,4]))

#[33,1,2,4,11,668] -> 5
def cant_digitos_impares (lista:list[int]) -> int:
    aux_str:list[int] = []
    contador:int=0
    for numero in lista:
        numero_str = str (numero)

        for digito in numero_str:
            aux_str.append(digito)

    for d in aux_str:
        if int(d) % 2 != 0:
            contador+=1

    return contador

#print (cant_digitos_impares ([33,1,2,4441,11,668]))

def buscar_nota_minima(c : Cola[str, int]) -> int:
    tuplaMin: tuple[str, int] = c.get()
    contenedor:Cola=Cola()
    contenedor.put(tuplaMin)

    while not c.empty():
        elem:tuple[str, int] = c.get()
        contenedor.put(elem)

        if elem[1] < tuplaMin[1]:
            tuplaMin = elem

    while not contenedor.empty():
        c.put(contenedor.get())

    return tuplaMin[1]