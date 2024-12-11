from queue import LifoQueue as Pila
from queue import Queue as Cola

import random

def generar_numeros_al_azar(cant: int, desde: int, hasta: int) -> Pila[int]:
    res: Pila[int] = Pila()
    for i in range(cant):
        res.put(random.randint(desde, hasta))

    return res

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
        print(elem, end=" ")
    print("-----")

    while not caux.empty():
        c.put(caux.get())


def armarSecuencideBingo() -> Cola[int]:
    #armo una lista con los numeros del 0 al 9
    lista: list[int] = list(range(0,10))
    #desordena de forma random la lista
    random.shuffle(lista)
    #creo una cola y la lleno con los elementos de la lista
    bolillero: Cola[int] = Cola()
    for bolilla in lista:
        bolillero.put(bolilla)
    return bolillero

def jugarCartonDeBingo(carton: list[int], bolillero: Cola[int]) -> int:
    res: int = 0
    bolillasCarton: int = 0
    bolAux: Cola[int] = Cola()
    while bolillasCarton < len(carton):
        bolilla: int = bolillero.get()
        bolAux.put(bolilla)
        if pertenece(bolilla, carton):
            bolillasCarton = bolillasCarton + 1
        res = res + 1

    while not bolillero.empty():
        bolAux.put(bolillero.get())
    
    while not bolAux.empty():
        bolillero.put(bolAux.get())

    return res

def pertenece(elem: int, lista: list[int]) -> bool:
    res: bool = False
    for x in lista:
        if x == elem:
            res = True

    return res

def perteneceS(elem: str, lista: list[str]) -> bool:
    res: bool = False
    for x in lista:
        if x == elem:
            res = True

    return res

def calcular_promedio_por_estudiante(notas: list[tuple[str, float]]) -> dict[str, float]:
    res: dict[str, float] = {}
    for nota in notas:
        if not perteneceS(nota[0], res.keys()):
            prom: float = calcular_promedio(nota[0], notas)
            res[nota[0]] = prom
        
    return res


def calcular_promedio(estudiante: str, notas: list[tuple[str, float]]) -> float:
    cant_notas: int = 0
    suma_notas: int = 0
    for nota in notas:
        if nota[0] == estudiante:
            cant_notas = cant_notas + 1
            suma_notas = suma_notas + nota[1]

    return suma_notas/cant_notas


notas = [["P1", 3], ["P2", 5],["P1", 6], ["P3", 10],["P3", 10]]
print(calcular_promedio_por_estudiante(notas))