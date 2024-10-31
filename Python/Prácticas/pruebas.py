import random
from queue import Queue as Cola
from queue import LifoQueue as Pila
p = Pila ()
c = Cola ()
p . put (1) # apilar
elemento = p . get () # desapilar
p . empty () # esta vacia ?


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

gente = Cola()
gente.put(("a",48,True,False))
gente.put(("b",45,False,True))
gente.put(("c",34,True,True))
gente.put(("d",84,False,False))
gente.put(("e",44,False,True))
gente.put(("f",41,True,True))
gente.put(("g",14,False,False))
gente.put(("h",49,True,False))

mostrar_cola(atencion_a_clientes(gente)) 

