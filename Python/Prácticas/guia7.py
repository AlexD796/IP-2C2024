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

def pertenece3 (s: list[int], e: int) -> bool:
    res: bool= False
    for n in s:
        if n == e:
            res= True
    return res
    
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

def palabraLarga (s:list[list[chr]]) -> bool:
    for i in s:
        if len(i) > 7:
            return True
    return False

def invertir_cadena(c: str) -> str:
    cadena_invertida = ""
    for letra in c:
        cadena_invertida = letra + cadena_invertida
    return cadena_invertida

def palindromo (s: str)->bool:
    if invertir_cadena (s) == s:
        return True
    else:
        return False

def tresNumIguales (num:list[int])->bool:
    i=0
    while i < len(num)-2:
        if num[i]==num[i+1]==num[i+2]:
            return True
        i+=1 ##importante esta identacion
    return False

def contarVocalesDist (s:str) -> int:
    i=0
    for letra in s:
        if letra in "aeiou":
            i+=1
    return i

contarVocalesDist ("lolaso")

def tresVocalesDist (s:str)->bool:
    if contarVocalesDist (s)== 3:
        return True
    return False

#from typing import List

def maximo (s:list[int])->int:
    max:int=0
    for i in s:
        if i > max:
            max=i
    return max

def pos_maximo (s:list[int]) -> int:
   i:int=0
   for n in range(len(s)):
       if maximo (s) == s[n]:
           return n

#def cant_digitos_impares (s:list) -> int

#EJERCICIO 2

def CerosEnPosicionesPares (s:list[int]):
    for i in (s):
        if i % 2 == 0:
            s[i]= 0

def Ceros2 (s:list[int]):
    i:int=0
    while i < len (s):
        s[i] = 0
        i+=2

def Ceros3 (s:list[int]):
    for i in range (0, len(s), 2):
        s[i]= 0

def CerosEnPosicionesPares2 (s:list[int]) -> list[int]: # [].append (0) = [0] > [0].append 0 [0,1]
    res:list[int] = []
    i:int= 0

    while i < len(s):
        if i % 2 == 0:
            res.append(0)
        else:
            res.append (s[i])
        i+=1
    return res


#print (CerosEnPosicionesPares ([2,3,4,2,2])) #NO FUNCIONA PORQUE NO HAY RETURN 

#print (CerosEnPosicionesPares2 ([2,3,4,2,2]))

#lista= [2,3,4,2,2]
#CerosEnPosicionesPares(lista)
#print(lista)

#cd a carpeta
#python3 guia7.py 
#pone le print en el archivo
#control shift p > interprete python3
#print (CerosEnPosicionesPares2 ([2,234,21,2,1]))

def borrarVocales (s:str) -> str:
    res:str= []
    for i in s:
        if i not in "aeiou":
            res.append (i)

    return res 

def remplaza_vocales (s:str) -> str:
    res:str = []
    for i in s:
        if i in "aeiou":
            res.append ("-")
        if i not in "aeiou":
            res.append (i)
    return res


def dar_vuelta_str (s:str) -> str:
    lista = s
    for i in range(len(s)-1, -1, -1):
        return (s[i])

# ["a", "b", "c"] : list[str]  #en Python no existe chr como tipo sino como funcion! (asigna ascii)
# ese ejemplo en haskell es una list[chr]
