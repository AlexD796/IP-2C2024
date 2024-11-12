""" COMENTARIOS GENERALES DE LA GUIA

["a", "b", "c"] : list[str]  en PYTHON --> no existe chr como tipo sino como funcion! (asigna ascii)
este ejemplo en haskell es una list[chr]

# [].append (1) = [1] --> [0].append --> [1,0]


OBSERVACIONES: esPalindromo, dar_vuelta_str, pertenece_a_cada_uno, cant_digitos_impares, CerosEnPosicionesPares, Tateti
!!! HACER EL OPCIONAL !!!

cd a carpeta
python3 guia7.py 
ponele print en el archivo
control shift p > interprete python3
"""
import copy

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

def ordenados (s:list[int])->bool:
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
    print (s[0])
    #while i < len (s):
      #  if s[i] % 2 !=0:
      #      res+=1
       # i+=1
  #  return res

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
    lista:str= ""
    for i in range(len(s)-1, -1, -1):
        lista.apend (s[i])
    return lista

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

def pertenece_a_cada_uno_version_1 (s:list[list[int]], e:int, res:list[bool]) -> list[bool]:
    copia:list[bool]= copy.deepcopy(res)
    res=[]
    for fila in range(len(s)):
        res.append (pertenece (s[fila],e)) 
    return res+copia

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

def es_matriz (s:list[list[int]]):
    i:int=0
    while i < len(s)-1:
        if len(s[i]) != len(s[i+1]):
            return False
        i+=1
    return True

def filas_ordenadas (s:list[list[int]], res:list[bool]):
    res=[]
    for i in range(len(s)):
        res.append (ordenados (s[i]))
    return res

def columna (s:list[list[int]], e:int)-> list[int]:
    res:list[int]=[]
    for i in range (len(s)):
        res.append (s[i][e])
    return res

def columna_ordenada (s:list[list[int]])->list[bool]:
    columnas:list[list[int]]=[]
    res:list[bool]=[]
    for i in range (len(s)):
        columnas.append((columna (s, i)))
    for i in range (len (s)):
        res.append(ordenados (columnas[i]))
    return res

def trasponer (s:list[list[int]])->list[list[int]]:
    res:list[list[int]]=[]
    for i in range (len(s)):
        res.append((columna (s, i)))
    return res

#print (trasponer (["XXO","OOX","OOO"]))

def verificaPosHorizontal (s:list[str])-> bool:
    for i in range (len (s)):
        if s[i][0] == s[i][1] == s[i][2]:
            return True
    return False

def devuelveInt (s:list[str])->int:
    for i in range (len (s)):
        if s[i][0] == s[i][1] == s[i][2]:
            if s[i][1] == "X":
                return 1
            if s[i][1] == "O":
                return 0

def extraerInt (s:list[str])->int:
    if s[1][1] == "X":
        return 1
    else:
        return "0"

def ganadorTateti (s:list[str])->int:
    traspuesto:list[str]=trasponer (s)
    if verificaPosHorizontal (s) == True:
        return devuelveInt(s)
    if verificaPosHorizontal (traspuesto) == True:
        return devuelveInt(traspuesto)
    if s[0][0] == s [1][1] == s [2][2]:
        return extraerInt (s)
    if s[0][2] == s [1][1] == s [2][0]:
        return extraerInt (s)
    else:
        return 2

"""print (ganadorTateti (["XXX","OOX","XOX"])) # 1
print (ganadorTateti (["XOX","XXX","XOX"])) # 1
print (ganadorTateti (["XOX","OOX","OOO"])) # 0
print (ganadorTateti (["OOX","OXO","OXX"])) # 0
print (ganadorTateti (["OXX","XXO","OXO"])) # 1
print (ganadorTateti (["XOX","XOX","OXX"])) # 1
print (ganadorTateti (["XOO","OXO","XOX"])) # 1
print (ganadorTateti (["OXO","OXX","XOO"])) # 2
print (ganadorTateti (["OXX","XOX","OXO"])) # 0
print (ganadorTateti (["OXX","OOX","XXO"])) # 0
print (ganadorTateti (["XOX","OOX","OXO"])) # 2"""

#EJERCICIO 7

def listaDeEstudiantes()->list[str]: #okay...........
    res:list[str]=[]
    nombre=""
    while(nombre!="listo"):
        print("Ingrese un nombre: ")
        nombre=input()
        if(nombre!='listo'):
            res.append(nombre)
    return res

def cargaSUBE () -> list[tuple[str,int]]:
    historial: list[tuple[str,int]] = []
    accion:str=""
    carga:int=0
    while accion != "X":
        print ("Ingrese:\n “C” = Cargar créditos\n “D” = Descontar créditos\n “X” = Finalizar el programa: ")
        accion=input()
        if accion== "C":
            print ("Ingrese un monto: ")
            carga=input()
            historial.append ((accion,carga))
        if accion=="D":
            print ("Ingrese un monto: ")
            carga=input()
            historial.append ((accion,carga))
    return historial

def hay_minuscula (s:str) ->bool:
    for c in s:
        if (c>="a") and (c<="z"):
            return True
    return False

def hay_mayuscula (s:str) ->bool:
    for c in s:
        if (c>="A") and (c<="Z"):
            return True
    return False

def hay_numero (s:str) ->bool:
    for c in s:
        if (c>="0") and (c<="9"):
            return True
    return False

def fortalezaContraseña ():
    print ("Ingresá contraseña: ")
    contraseña=input()
    if len(contraseña) > 8 and hay_minuscula (contraseña) and hay_mayuscula (contraseña) and hay_numero (contraseña):
        return "La seguridad de tu contraseña es: VERDE"
    if len(contraseña) < 5:
        return "La seguridad de tu contraseña es: ROJA"
    else:
        return "La seguridad de tu contraseña es: AMARILLA"
    
#print (fortalezaContraseña ())
#input ()