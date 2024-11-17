import random
from queue import Queue as Cola
from queue import LifoQueue as Pila
p = Pila ()
c = Cola ()

#EJERCICIO 1
def gestion_notas(notas_estudiante_materia: list[tuple[str, str, int]]) -> dict[str, list[tuple[str,int]]]:
   # [(a, mate, 5)(a, bio, 6)(b, cine, 9)] -> {a : [(mate, 5), (bio, 6)], b : [(cine, 9)], c}
   res: dict[str, list[tuple[str,int]]] = {}
   aux: list [tuple[str,int]] = []

   for tripla in notas_estudiante_materia:
       
       if tripla[0] not in res.keys():
           listaTupla:list[tuple[str,int]] = [(tripla[1], tripla[2])]
           res[tripla[0]] = listaTupla

       elif tripla[0] in res.keys():
           listaTuplaDos:list[tuple[str,int]] = res.pop(tripla[0])
           listaTuplaDos.append ((tripla[1], tripla[2]))
           res[tripla[0]] = listaTuplaDos

       

   return res

alumnosNotas={("a", "mate", 5),("a", "bio", 6),("b", "cine", 9), ("c", "cunt", 7),("c", "kuka", 10)}
#print (gestion_notas (alumnosNotas))

#EJERCICIO 2
#[5434, 42, 811, 3139] --> 5 (los dígitos pares son 4, 4, 4, 2, y 8).
def cantidad_digitos_pares(numeros: list[int]) -> int:
    aux = []
    contador:int=0

    for n in numeros: #n= 5434
        num_str:str = str(n) # num_str= "5434"
        
        for digito in num_str: #digito= 5,4,3,4
            aux.append (digito) #AUX=["5","4","3"...]

    for i in aux:
        if int(i) % 2 == 0: #vuelvo cada elemento de la lista de str, a !!int!! individualmente
            contador+=1

    return contador

#print (cantidad_digitos_pares ([54344, 5, 11, 3139]))

#EJERCICIO 3
def reordenar_cola_primero_pesados (paquetes:Cola[tuple[str,int]], umbral:int) -> Cola[str,int]:
    res:Cola[tuple[str,int]] = Cola ()
    cola_umbral_menor:Cola[tuple[str,int]] = Cola ()
    cola_umbral_mayor:Cola[tuple[str,int]] = Cola ()
    paquetes_copia:list[tuple[str,int]] = []

    while not paquetes.empty():
        tupla:tuple[str,int] = paquetes.get()
        paquetes_copia.append(tupla)
        
    for elem in paquetes_copia: #paquetes_copia no se vacía
        if elem[1] <= umbral:
            cola_umbral_menor.put (elem)
        if elem[1] > umbral:
            cola_umbral_mayor.put (elem)

    while not cola_umbral_mayor.empty():
        res.put(cola_umbral_mayor.get())

    while not cola_umbral_menor.empty():
        res.put(cola_umbral_menor.get())

    for x in paquetes_copia: #restauré variable original ya que me está recorriendo la copia de paquetes (que está en el orden de la cola original (izq principio, derecha final))
        paquetes.put(x)

    return res 

def mostrar_cola(c: Cola[int]) -> None: 
    caux: Cola[int] = Cola()

    while not c.empty():
        elem: int = c.get()
        caux.put(elem)
        print(elem)
    print("-----")

    while not caux.empty():
        c.put(caux.get())


c = Cola ()
c.put(("e", 5)) #principio
c.put(("d", 1))
c.put(("c", 7))
c.put(("b", 5))
c.put(("a", 12)) #final

#print (mostrar_cola (reordenar_cola_primero_pesados(c, 5)))

# ("c", 7) principio
# ("a", 12)
# ("e", 5)
# ("d", 1)
# ("b", 5) final


#EJERCICIO 4

matriz = [[2,3,4,6],[5,3,1,7],[4,55,12,7]] #--> false xq min(c1)=2,min(c2)=3,min(c3)=1 
#matriz_columnas -> [[2,5,4],[3,3,55],[4,1,12],[6,7,7]]

def matriz_pseudo_ordenada (matriz:list[list[int]]) -> bool:
    matriz_columnas:list[list[int]] = []

    for fila in matriz: #fila= [2,3,4,6]
        longitudFila = len(fila)

        for i in range(0, longitudFila, 1): #longitud = 4 range= 0 1 2 3
            matriz_columnas.append(columna(matriz, i)) #hago matriz_columnas

    for i in range(len(matriz_columnas)-1): #i= 0 1 2 
        listaMin:list[int]= buscarMin (matriz_columnas) #--> [2,3,1,6]
       
        if listaMin[i] < listaMin [i+1]: #veo si la res de buscarMin está ordenda menor a mayor
            return True
        else:
            return False

def buscarMin (matriz_columnas:list[list[int]]) -> list[int]:
#matriz_columnas = [[2,5,4],[3,3,55],[4,1,12],[6,7,7]] --> [2,3,1,6]
    res:list[int]=[]

    for fila in matriz_columnas: #fila=[2,5,4]   
        res.append(minimo(fila))
    
    return res

def minimo (s:list[int])->int:
    min:int= maximo (s)
    for i in s:
        if i < min:
         min= i
    return min

def maximo (s:list[int])->int:
    max:int=0
    for i in s:
        if i > max:
            max=i
    return max

def columna (s:list[list[int]], e:int) -> list[int]:
    #[[2,3,4,6],[5,3,1,7]] 3 ->[6,7] 
    res:list[int] = []
    for fila in s:
        res.append(fila[e])
    
    return res

#print (minimo ([2,5,4]))
#print (buscarMin ([[2,5,4],[3,3,55],[4,1,12],[6,7,1]]))
#print (matriz_pseudo_ordenada (([[2,5,4],[3,3,55],[4,3,12],[6,7,9]])))

