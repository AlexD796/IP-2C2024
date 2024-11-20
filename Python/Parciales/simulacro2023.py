# Ejercicio 1
#
#  problema ultima_aparicion (s: seq⟨Z⟩, e: Z) : Z {
#    requiere: {e pertenece a s }
#    asegura: {res es la posición de la última aparición de e en s}
#  }

# Por ejemplo, dados
#   s = [-1,4,0,4,100,0,100,0,-1,-1]
#   e = 0
# se debería devolver res=7

def ultima_aparicion (s:list[int], e:int) -> int:
    listaAlrevez:list[int] = []

    for i in range (len(s)-1, -1, -1):
        listaAlrevez.append(s[i])

    for j in range (len(listaAlrevez)):
        if e == listaAlrevez[j]:
            return len(s) - j - 1

#print (ultima_aparicion ([-1,4,0,4,100,0,100,0], e=100))


# Ejercicio 2
#
#  problema elementos_exclusivos (s: seq⟨Z⟩, t: seq⟨Z⟩) : seq⟨Z⟩ {
#    requiere: -
#    asegura: {Los elementos de res pertenecen o bien a s o bien a t, pero no a ambas }
#    asegura: {res no tiene elementos repetidos }
#  }

# Por ejemplo, dados
#   s = [-1,4,0,4,3,0,100,0,-1,-1]
#   t = [0,100,5,0,100,-1,5]
# se debería devolver res = [3,4,5] ó res = [3,5,4] ó res = [4,3,5] ó res = [4,5,3] 
# ó res = [5,3,4] ó res = [5,4,3]

def pertenece (e:int, seq:list[int]) -> bool:
    res:bool=False

    for elem in seq:
        if elem==e:
            res = True
    
    return res

def elementos_exclusivos (s:list[int], t: list[int]) -> list[int]:
    res:list[int]=[]
    aux:list[int] = s+t

    for elem in aux:
        if (pertenece(elem, s) and not pertenece (elem, t)) or (pertenece(elem, t) and not pertenece (elem, s)): #podria haber hecho una f auxiliar "pertenece a ambsa" -> return pertenece e l1 and pertenece e l2 - que el res sea un bool
           if not pertenece (elem, res):
               res.append(elem)

    return res

#s = [-1,4,0]
#t = [0,100,100]

#print(elementos_exclusivos (s,t))

# Ejercicio 3
#
# Se cuenta con un diccionario que contiene traducciones de palabras del idioma castellano (claves) a palabras
# en inglés (valores), y otro diccionario que contiene traducciones de palabras en castellano (claves) a palabras
# en alemán (valores). Se pide escribir un programa que dados estos dos diccionarios devuelva la cantidad de 
# palabras que tienen la misma traducción en inglés y en alemán.

#  problema contar_traducciones_iguales (ing: dicc⟨String,String⟩, ale: dicc⟨String,String⟩) : Z {
#    requiere: -
#    asegura: {res = cantidad de palabras que están en ambos diccionarios y además tienen igual valor en ambos}
#  }

# ing = {"vidrio" : "glass", "arbol" : "tree", "palo" : "stick", "luz" : "light"}
# ale = {"arbol" : "jasjas", "luz" : "light", "palo" : "stick", "cactus" : "cactus"}
# res = 2 ya q palo y luz tienen misma traduccion

def contar_traducciones_iguales (ing: dict[str,str], ale: dict[str,str]) -> int:
    contador:int=0

    for c, v in ing.items (): #c=vidrio #v=glass
        if pertenece (c, ale.keys()): #no... #c=arbol #v=tree 
           v2:str = ale[c] #v2= jasjas
           if v2==v:
               contador+=1

    return contador

#ingles = {"vidrio" : "glass", "arbol" : "tree", "palo" : "stick", "luz" : "light"}
#aleman = {"arbol" : "jasjak", "luz" : "light", "palo" : "stick", "cactus" : "cactus"}

#print (contar_traducciones_iguales (ingles, aleman)) #2

# Ejercicio 4
#
# Dada una lista de enteros s, se desea devolver un diccionario cuyas claves sean los valores presentes en s, 
# y sus valores la cantidad de veces que cada uno de esos números aparece en s

#  problema convertir_a_diccionario (lista: seq⟨Z⟩) : dicc⟨Z,Z⟩) {
#    requiere: -
#    asegura: {res tiene como claves los elementos de lista y res[n] = cantidad de veces que aparece n en lista}
#  }

#seq= [1,2,3,101,2,101,101,3,2,1,1,2] -> res = {1 : 3, 2 : 4, 3 : 2, 101 : 3}
def cantidad_apariciones (e:int, seq:list[int]) -> int:
    contador:int=0

    for numero in seq:
        if e == numero:
            contador +=1
    
    return contador

def convertir_a_diccionario (lista: list[int]) -> dict[int,int]:
    res:dict[int,int] = {}

    for n in lista:
        if not pertenece (n,res.keys()):
            res[n] = cantidad_apariciones (n,lista)
    
    return res


#s= [1,2,3,101,2,101,101,3,2,1,1,2] #-> res = {1 : 3, 2 : 4, 3 : 2, 101 : 3}
#print (convertir_a_diccionario (s))