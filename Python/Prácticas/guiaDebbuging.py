#EJERCICIO 1 >>> estaba mal asignado el esMenor = "False" y el return era otra cosa

def esta_ordenado_asc(v):
    i = 0
    longitud = len(v)
    esMenor = True
    while i <= longitud -2 and esMenor:
        esMenor = v[i] <= v[i + 1]
        i += 1
    return esMenor

def esta_ordenado_desc(v):
    longitud = len(v)
    i = 0
    esMayor = True
    while i <= longitud - 2 and esMayor:
        esMayor = v[i] >= v[i + 1]
        i += 1
    return i == longitud - 1


def fibo (n:int) -> int:
    if n <= 1:
        return n 
    un_fibo: int = 0
    un_fibo_sig: int = 1
    i: int= 2
    while i <= n:
        aux: int= un_fibo + un_fibo_sig
        un_fibo = un_fibo_sig
        un_fibo_sig = aux
        i = i + 1
    return un_fibo

# NO FUNCIONA ??? (lo saqué de la clase práctica que no fui...) print (fibo (3))

def es_primo (n:int) -> bool:
    cant_divisores: int = 0
    i: int = 1
    while i < n and cant_divisores < 2:
        if n % i == 0:
            cant_divisores += 1
            i +=1
    return cant_divisores < 2 and i == n

# lo copié también y no me funciona con los primos ok... print (es_primo (11))
