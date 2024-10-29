import random
from queue import Queue as Cola
from queue import LifoQueue as Pila
p = Pila ()
c = Cola ()
p . put (1) # apilar
elemento = p . get () # desapilar
p . empty () # esta vacia ?

def evaluar_expresion(s:str)->str:
    contenedor=Pila()
   
    for token in s:
        if token in "123456789":
            contenedor.put(token)
        elif token in "+-/*":
            n2=int(contenedor.get()) #SE VUELVE INT EL STR..... SINO NO FUNCIONA
            n1=int(contenedor.get())
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

def esta_bien_balanceada(s:str)->bool:
    res:bool=True
    p=Pila()
    parentesis_abiertos:int=0
    for letra in s:
        p.put(letra)
    while not p.empty():
        letra_sacada=p.get()
        if letra_sacada=="(":
            parentesis_abiertos+=1
        if letra_sacada==")":
            parentesis_abiertos-=1
   
    if parentesis_abiertos!=0:
        res=False
    return res

print(
esta_bien_balanceada("3*(1x2)-(5-4)"),
esta_bien_balanceada("7((2x7)"),
esta_bien_balanceada("8*(9/3))")
)