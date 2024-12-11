from queue import LifoQueue as Pila
from queue import Queue as Cola
import random
from typing import Any

"""
Ejercicio resueltos el 28/10 en el labo 1104 para comA, en labo 1105 para comB.
Se completaron los ejercicios que no llegamos a ver en clase.
Se agregaron comentarios y corrigieron notaciones de tipos.
"""


# Esta es la versión del enunciado que vimos
def generar_nros_al_azar(cantidad:int, desde:int, hasta:int) -> Pila[int]:
    res:Pila[int] = Pila()
    for _ in range(0, cantidad):
        elem:int = random.randint(desde, hasta)
        res.put(elem)
    
    return res


# Esta es una versión donde no retorna una pila, sino que la pila es un parámtro más pero "out"
# Lo importante es "limpiar" lo que traiga ya que puede ser basura.
# generar_nros_al_azar2(in cantidad:int, in desde:int, in hasta:int, out pila: Pila[int])
def generar_nros_al_azar2(cantidad:int, desde:int, hasta:int, pila: Pila[int]) -> None:
    #limpiamos la pila si tiene algo
    while not pila.empty():
        pila.get()

    for _ in range(0, cantidad):
        elem:int = random.randint(desde, hasta)
        pila.put(elem)

def mostrar_elems_pila(p:Pila[int]):
    pilaAux:Pila[int] = Pila()
    print("Comienzo mostrando los elementos de pila")
    while not p.empty():
        elem:int = p.get() 
        print(elem)
        pilaAux.put(elem)
    print("Terminé de mostrar los elementos de pila")
    while not pilaAux.empty():
        elem = pilaAux.get()
        p.put(elem)

def mostrar_elems_cola(c:Cola[int]):
    colaAux:Cola[int] = Cola()
    print("Comienzo mostrando los elementos de cola")
    while not c.empty():
        elem:int = c.get()
        #Podemos agregar 'end=" "' para que muestre uno al lado de otro, en lugar de uno debajo de otro
        #si no le pasamos el parámetro end=, entonces el final es un salto de lineas
        print(elem, end=" ")
        colaAux.put(elem)
    print("\nTerminé de mostrar los elementos de cola")
    while not colaAux.empty():
        elem = colaAux.get()
        c.put(elem)
    

print("\tEJERCICIO GENERAR NUMEROS AL AZAR")
cantidad = 5
desde = 5
hasta = 15
pila:Pila[int] = generar_nros_al_azar(cantidad, desde, hasta)
mostrar_elems_pila(pila)
print("Muestro de nuevo los elementos para ver si son los mismos")
mostrar_elems_pila(pila) #Notar que si llamamos dos veces la misma fn, los elementos no se modifican

pout:Pila[int] = Pila()
pout.put(5)
# Este es un ejemplo donde pila se pasa como parámetro out
# Notar que tiene "basura" al pasar el parámetro, pero no importa porque debemos limpiarlo.
generar_nros_al_azar2(cantidad, desde, hasta, pout)

mostrar_elems_pila(pout)
print("Muestro de nuevo los elementos para ver si son los mismos")
mostrar_elems_pila(pout)


#Notar que agregamos None como posible tipo de salida, esto va a depender de qué diga la especificación
def buscar_el_maximo(p:Pila[int]) -> int|None:
    paux: Pila[int] = Pila() # En esta pilaauxiliar vamos a guardar los elems que desapilamos
    maximo:None|int = None
    #IMPORTANTE! recordar que siempre que hagamos get(), antes debemos
    #asegurarnos que la pila/cola no está vacía.
    if not p.empty():
        maximo = p.get() # cada vez que hacemos p.get(), tenemos que agregarlo a la pilaux
        paux.put(maximo)
        while not p.empty():
            elem:int = p.get() # cada vez que hacemos p.get(), tenemos que agregarlo a la pilaux
            paux.put(elem)
            if elem >= maximo:
                maximo = elem

        #Como es de tipo "in" la pila, debemos dejarla como estaba
        while not paux.empty():
            p.put(paux.get())
    
    return maximo


print("\n\n\tEJERCICIO MAXIMO DE LA PILA")
pmax:Pila[int] = Pila()
pmax.put(-3)
pmax.put(-2)
pmax.put(-1)
print("El maximo de la pila es:", buscar_el_maximo(pmax))




def armar_secuencia_de_bingo() -> Cola[int]:
    cola:Cola[int] = Cola()
    lista:list[int] = list(range(0,100))#Esto crea una lista con los elementos 0..99
    random.shuffle(lista)#esto desordena los elementos, modificando la lista
    
    for elem in lista:
        cola.put(elem)

    return cola

def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    cant_jugadas_necesarias: int = 0
    acertadas: int = 0
    bolAux: Cola[int] = Cola()
    while acertadas < len(carton):
        bolilla: int = bolillero.get()
        bolAux.put(bolilla)
        if pertenece(bolilla, carton):
            acertadas += 1
        cant_jugadas_necesarias += 1

    # Si acerté todas antes de llegar a la última bolilla, entonces agrego las restantes a la colaAux
    while not bolillero.empty():
        bolAux.put(bolillero.get())
    
    # Dejo bolillero como estaba originalmente porque es un parámetro "in"
    while not bolAux.empty():
        bolillero.put(bolAux.get())

    return cant_jugadas_necesarias

# Notar que si queremos que la lista sea de cualquier tipo, podemos usar "any"
# cuidado que el tipo tiene que saber responder a la operación ==
def pertenece(elem: Any, lista: list[Any]) -> bool:
    res: bool = False
    for x in lista:
        if x == elem:
            res = True
    return res

print("\n\n\tEJERCICIO BINGO")
bolillero:Cola[int] = armar_secuencia_de_bingo()
# si queremos mostrar los valores, en orden, del bolillero
mostrar_elems_cola(bolillero)
carton = [20,10,5,7,99,15,25,30,42,11,47,69] #creamos un carton con 12 elementos
res:int = jugar_carton_de_bingo(carton, bolillero)
print("Para ganar con el carton ", carton, "se necesitaron ", res, "jugadas")




def calcular_promedio_por_estudiante(notas: list[tuple[str, float]]) -> dict[str, float]:
    res: dict[str, float] = {}
    for estudiante, _ in notas:
        if not pertenece(estudiante, list(res.keys())):
            prom: float = calcular_promedio(estudiante, notas)
            res[estudiante] = prom
    return res


def calcular_promedio(estudiante: str, notas: list[tuple[str, float]]) -> float:
    cant_notas: int = 0
    suma_notas: float = 0
    for nota in notas:
        if nota[0] == estudiante:
            cant_notas += 1
            suma_notas += nota[1]

    return suma_notas/cant_notas

print("\n\n\tCALCULAR PROMEDIO")
notas:list[tuple[str, float]] = [("Fulanito", 3), ("Cosme", 7),("Fulanito", 6), ("Cosme", 10)]
print(calcular_promedio_por_estudiante(notas))