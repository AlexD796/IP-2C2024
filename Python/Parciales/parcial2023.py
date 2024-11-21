#Implementar la función ind_nesima_aparicion que dada una secuencia de enteros s, 
#y dos enteros n y elem devuelve la posición en la cual elem aparece por n-ésima vez 
#en s. En caso de que elem aparezca menos de n veces en s, devolver -1.

#problema ind_nesima_aparicion (in s: seq⟨Z⟩, in n: Z, in elem: Z) : Z {
#  requiere: {n>0}
#  asegura: {Si el elemento aparece menos de n veces en la secuencia, res= -1 }
#  asegura: {Si el elemento aparece al menos n veces en la secuencia, s[res] = elem }
#  asegura: {Si el elemento aparece al menos n veces en la secuencia, elem aparece n-1 
#  veces en s entre las posiciones 0 y res-1 }

#Por ejemplo, dadas
#s = [-1, 1, 1, 5, -7, 1, 3]
#n = 2
#elem = 1
#se debería devolver res = 2

def ind_nesima_aparicion (s: list[int],n: int, elem: int) -> int:
    apariciones:int=0

    for i in range (len(s)): #i= 0 1 2 3 4 5 6 xq len(s)=7
        if s[i] == elem:
            apariciones+=1
            if apariciones == n:
                return i
    
    return -1


seq = []
n = 3
elem = 707

#print (ind_nesima_aparicion(seq,n,elem))

#otra forma con while
def ind_nesima_aparicion_bis (s: list[int],n: int, elem: int) -> int:
    i:int=0
    apariciones:int=0

    while i < len(s):
         if s[i] == elem:
            apariciones+=1
            if apariciones == n:
                return i
    i+=1
    
    return -1

#print (ind_nesima_aparicion(seq,n,elem))

def mezclar (s1: list[int], s2: list[int]) -> list[int]:
    res:list[int] = []

    for i in range (len (s1)):
        res.append (s1[i])
        res.append (s2[i])

    return res

s1 = [1]
s2 = [4]


#print (mezclar (s1,s2))

def frecuencia_posiciones_por_caballo(caballos: list[str], carreras: dict[str,list[str]]) -> dict[str.list[int]]:
    res:dict[str.list[int]]={}

    for resultados in carreras.values():
        for nombre in caballos:
            if nombre not in res.keys():
                res[nombre] = posiciones_carreras (carreras, nombre)

def posiciones_carreras (carreritas: dict[str,list[str]], nombre_esp:str):
    res=[]
    contador:int=0
    for resultados in carreritas.values():
        for i in range (len(carreritas.values())):
            if resultados[i] == nombre_esp:
                contador+=1