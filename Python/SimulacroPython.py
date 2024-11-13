# Ejercicio 1
def gestion_notas(notas_estudiante_materia: list[tuple[str, str, int]]) -> dict[str, list[tuple[str,int]]]:
   # [(a, mate, 5)(a, bio, 6)(b, cine, 9)] -> {a : [(mate, 5), (bio, 6)], b : [(cine, 9)]}
   #res={}
   res: dict[str, list[tuple[str,int]]] = {}
   aux: list [tuple[str,int]] = []

   for tupla in notas_estudiante_materia:
        if tupla[0] not in res.keys():
       #aux.append ((tupla[1], tupla[2]))
            tuplaAux= (tupla[1], tupla[2])
            res[tupla[0]] = aux.append(list(tuplaAux))
        else: #if tupla [0] in res.keys():
            tuplaAux2= (tupla[1], tupla[2])
            estacional:tuple[str, int] = res.pop (tupla [0]) #
            aux.append (list(estacional)) #aux esta funcionado como una tupla
            res[tupla[0]] = aux
      
     # if tupla[0] in res.keys():
       # res[tupla[0]] = (tupla[1], tupla[2])
        #res[tupla[0]].append ((tupla[1], tupla[2]))
       # for materia, nota in notas_estudiante_materia.values():

   return res

alumnosNotas={("a", "mate", 5),("a", "bio", 6),("b", "cine", 9)}
print (gestion_notas (alumnosNotas))

# Ejercicio 2
#[5434, 42, 811, 3139] --> 5 (los dígitos pares son 4, 4, 4, 2, y 8).
def cantidad_digitos_pares(numeros: list[int]) -> int:
    contador:int=0
    aux:list[int]=[]

    for n in numeros:
        #aux = (n) 
    
        for i in range (0, len(aux), 1):
        
         if n[i] % 2 == 0 :
             contador += 1

    return contador

def longitud (numero: int) -> int:
   contador:int=0
   str(numero)
   #for i in range (len )


veamos = [5434, 42, 811, 3139]
#print (cantidad_digitos_pares (veamos))
