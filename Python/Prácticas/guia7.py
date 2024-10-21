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

#EJERCICIO 1

def pertenece (s: list[int], e: int) -> bool:
    i:int=0
    while i < len(s):
        if s[i] == e:
            return True
        i+=1
    return False

def pertenece2 (s: list[int], e: int) -> bool:
    for i in range (len(s)):
        if s[i] == e:
            return True
    return False
#no se me ocurrió otra forma
    
def divide_a_todos (s:list[int], e :int)->bool:
    i:int=0
    while i < len(s):
        if s[i] % e != 0:
            return False
        i+=1
    return True

def divide_a_todos2 (s:list[int], e :int)->bool:
    for i in range (len(s)):
        if s[i] % e != 0:
            return False
    return True

def suma_total (s:list[int])-> int:
    i:int=1
    aux:int= s[0]
    while i < len (s):
        aux+= s[i]
        i+=1
    return aux
        

def suma_total2 (s:list[int])-> int:
    aux:int= 0
    for i in range(len(s)):
        aux += s[i]
    return aux

def maximo (s:list[int])->int:
    max:int=0
    for i in s:
        if i > max:
            max=i
    return max
    
def maximo2 (s:list[int])->int:
    max:int=0
    i:int=0
    while i < len(s):
        if s[i] > max:
            max= s[i]
        i+=1
    return max

def minimo (s:list[int])->int:
    min:int = maximo(s)
    i:int=0
    while i < len(s):
        if s[i] < min:
            min= s[i]
        i+=1
    return min

def minimo2 (s:list[int])->int:
    min:int= max(s)
    for i in s:
        if i < min:
            min=i
        i+=1
    return min



#POR QUE NO ME FUNCIONA ORD1 SI ES IGUAL????????????????
def ordenados (seq:list[int])-> bool:
    for i in range(0,len(seq),-1):
        if (not(seq[i]<seq[i+1])):
            return False
    return True

#print (ordenados ([13,64,67,13]))

def ordenados2 (seq:[int])->bool:
    for i in range(0,len(seq)-1):
        if (not(seq[i]<seq[i+1])):
            return False
    return True

#print (ordenados2 ([13,64,67,13]))

#RANGE (LONG-1,-1,-1) RECORRER LISTA ALREVEZ

def listaAlrevez (s:list[int]):
    longitud = len(s)
    for i in range(longitud-1, -1, -1):
        print (s[i])
#NO FUNCIONA POS_MAX NI POS_MIN
def pos_maximo (s:list[int]) -> int:
    i:int=-1
    max:int=0
    if len(s)== 0:
        return -1

    for n in s:
        if n > max:
         max=n
         i+=1
    return i

#print (pos_maximo ([112,23,22,121212]))

def pos_minimo(s:list[int]) -> int:
    i:int=-1
    min:int= maximo (s)
    n:int=0
    if len (s)== 0:
        return -1
    
    for n in s:
        if n < min:
            min=n
            n+=1
            i+=1
    return i

#print (pos_minimo ([112,23,22,1]))

def palabraLarga (s:[[chr]]):
    for i in s:
        if len(i) > 7:
            return True
    return False
