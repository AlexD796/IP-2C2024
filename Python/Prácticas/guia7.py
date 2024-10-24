""" COMENTARIOS GENERALES DE LA GUIA

["a", "b", "c"] : list[str]  en PYTHON --> no existe chr como tipo sino como funcion! (asigna ascii)
este ejemplo en haskell es una list[chr]

# [].append (1) = [1] --> [0].append 0 [1,0]


OBSERVACIONES: esPalindromo, pertenece_a_cada_uno, cant_digitos_impares, CerosEnPosicionesPares

"""

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

def ordenados2 (s:list[int])->bool:
    for i in range(0,len(s)-1):
        if (not(s[i]<s[i+1])):
            return False
    return True

def pos_maximo (s:list[int]) -> int:
   i:int=0
   for n in range(len(s)):
       if maximo (s) == s[n]:
           return n

def pos_minimo(s:list[int]) -> int:
    i:int=0
    for n in range(len(s)):
        if minimo (s) == s[n]:
          return n

def palabraLarga (s:list[list[chr]]) -> bool:
    for i in s:
        if len(i) > 7:
            return True
    return False
    
def palindromo (s: str)->bool:
    cadena_invertida = ""
    for letra in s:
        cadena_invertida = letra + cadena_invertida
    
    if cadena_invertida == s:
        return True
    else:
        return False

def esPalindromo(palabra:str)->bool: #nice.......................
    l:int=len(palabra)
    for i in range(0,l//2):
        if(palabra[i]!=palabra[(l-1)-i]):
            return False
    return True


def tresNumIguales (num:list[int])->bool:
    i=0
    while i < len(num)-2:
        if num[i]==num[i+1]==num[i+2]:
            return True
        i+=1 ##importante esta identacion
    return False

def contarVocalesDist (s:list[str]) -> int: #hay forma mas eficiente?
    lista:list[str]=[]
    for letra in s:
        if letra in "aeiou":
            lista+=letra

    sinRepetidos:list[str]= []
    for n in lista:
        if n not in sinRepetidos:
            sinRepetidos.append (n)
    
    return len(sinRepetidos)
    
def tresVocalesDist (s:str)->bool:
    if contarVocalesDist (s)== 3:
        return True
    return False

def cant_digitos_impares (s:list) -> int: #????
    i:int=0
    res:int=0
    while i < len (s):
        if s[i] % 2 !=0:
            res+=1
        i+=1
    return res

#print (cant_digitos_impares ([57, 2383, 812, 246])) #5

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

def CerosEnPosicionesPares2 (s:list[int]) -> list[int]: 
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

#lista= [2,3,4,2]
#CerosEnPosicionesPares(lista)
#print(lista)

#cd a carpeta
#python3 guia7.py 
#ponele print en el archivo
#control shift p > interprete python3

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
    lista:str= s
    for i in range(len(s)-1, -1, -1):
        return (s[i])

def dar_vuelta_str2 (s:str) -> str:
    lista:str=""
    for letra in s:
        lista = letra + lista
    return lista

def eliminar_repetidos (s:str)-> str:
    res:int=[]
    i:int=0
    while i < len (s):
        if s[i] not in res:
            res+=s[i]
        i+=1
    return res

#EJERCICIO 3

def promedio(s:list[int]) -> float:
    return (suma_total (s) / len (s))

def hayMenorA4 (s:list[int])-> bool:
    for i in range(len(s)):
        if s[i] <= 4:
            return True
    return False

def resultadoMateria (s:list[int])-> int:
    if not hayMenorA4 (s) and promedio (s) >= 7:
            return 1
    if not hayMenorA4 (s) and 4 <= promedio (s) < 7:
            return 2
    if hayMenorA4 (s) or promedio (s) < 4:
            return 3

#EJERCICIO 4

def saldoActual (historial:list[tuple[str,int]]) -> int:
    saldo:int=0
    for movimiento in historial:
        if movimiento[0] == "I":
            saldo+=movimiento[1]
        if movimiento [0] == "R":
            saldo-=movimiento[1]
    return saldo 

#EJERCICIO 5

def pertenece_a_cada_uno_version_1 (s:list[list[int]], e:int, res:list[bool]) -> list[bool]: #CON O SIN EL RES EN LA SIGNATURA ##como hago¿'¡?¿¡¿¿¡?
    for fila in range(len(s)):
        lista= res.append (pertenece (s[fila],e)) + #??
    return lista

def pertenece_a_cada_uno_version_2 (s:list[list[int]], e:int, res:list[bool]) -> list[bool]:
    res=[]
    for fila in range(len(s)):
        res.append (pertenece (s[fila],e))
    return res

def pertenece_a_cada_uno_version_3 (s:list[list[int]], e:int) -> list[bool]:
    res=[]
    for fila in range(len(s)):
        res.append (pertenece (s[fila],e))
    return res

#print (pertenece_a_cada_uno_version_1([[2,4,6,7],[11,22,7],[7,9,6,2,35,77]], 6, [True,False,False])) #-->[True,False,True,True,False,False]
#print (pertenece_a_cada_uno_version_2([[2,4,6,7],[11,22,7],[7,9,6,2,35,77]], 6, [True,False,False])) #-->[True,False,False]
#print (pertenece_a_cada_uno_version_3([[2,4,6,7],[11,22,7],[7,9,6,2,35,77]], 6) #-->[True,False,False]

