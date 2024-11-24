from queue import Queue as Cola
from queue import LifoQueue as Pila
p = Pila ()
c = Cola ()

##########################################################
####PARCIAL 1 ------- EJERCICIO 4: TRABAJADOR PREMIADO ###
##########################################################

"""1) Alerta Enfermedades Infecciosas (3 puntos)

Necesitamos detectar la aparición de posibles epidemias. Para esto contamos con un lista de enfermedades infecciosas y los registros de atención por guardia dados por una lista expedientes. Cada expediente es una tupla con ID paciente y enfermedad que motivó la atención. Debemos devolver un diccionario cuya clave son las enfermedades infecciosas y su valor es la proporción de pacientes que se atendieron por esa enfermedad. En este diccionario deben aparecer solo aquellas enfermedades infecciosas cuya proporción supere cierto umbral.

problema alarma_epidemiologica (registros: seq⟨ZxString⟩, infecciosas: seq⟨String⟩, umbral: R) : dict⟨String,R⟩ {
  requiere: {0 < umbral < 1}
  asegura: {claves de res pertenecen a infecciosas}
  asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de pacientes que se atendieron por esa enfermedad sobre el total de registros es mayor o igual al umbral, entonces res[enfermedad] = porcentaje}
  asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de e pacientes que se atendieron por esa enfermedad sobre el total de registros es menor que el umbral, entonces enfermedad no aparece en res}
}
"""
#r= [(1, "a"),(2, "b"),(3, "b"),(4, "a"),(5, "c"),(8, "c"),(9, "a"),(10, "d"),(29, "a")]
#in = ["a", "d"]
#u = 0.42
#-> 4/9=0.44 cumple -> dict = {"a", 0.44}

def umbral_especifico (registros: list[tuple[int,str]], e:str):
    total_pacientes:int = len(registros)

    return apariciones (registros, e) / total_pacientes

def apariciones (reg: list[tuple[int,str]], e:str):
    res:int=0

    for tupla in reg:
        if tupla[1] == e:
            res +=1

    return res

def pertenece (e:str, inf:list[str]):
    for elem in inf:
        if elem == e:
            return True
        
    return False

def alarma_epidemiologica (registros: list[tuple[int,str]], infecciosas:list[str], umbral: float) -> dict[str,float]:
    res:dict[str,float] = {}

    for elem in registros: #podes iterar en enfermedades infecciosas
        if (elem[1] not in res.keys()) and (pertenece (elem[1], infecciosas)) and (umbral_especifico (registros, elem[1]) >= umbral):
            res [elem[1]] = umbral_especifico (registros, elem[1])

    return res 


#r= [(1, "a"),(2, "b"),(3, "b"),(4, "a"),(5, "c"),(8, "c"),(9, "a"),(10, "d"),(29, "a")]
#inf = ["a", "d", "b"]
#u = 0.01
#print (alarma_epidemiologica (r, inf,u))

"""
2) Orden de atención (1 punto)

Desde el Hospital Fernandez nos pidieron solucionar una serie de problemas relacionados con la información que maneja sobre los pacientes y el personal de salud. En primer lugar debemos resolver en qué orden se deben atender los pacientes que llegan a la guardia. En enfermería, hay una primera instancia que clasifica en dos colas a los pacientes: una urgente y otra postergable (esto se llama hacer triage). A partir de dichas colas que contienen la identificación del paciente, se pide devolver una nueva cola según la siguiente especificación.

problema orden_de_atencion ( in urgentes: cola⟨Z⟩, in postergables: cola⟨Z⟩) : cola⟨Z⟩ {
  requiere: {no hay elementos repetidos en urgentes}
  requiere: {no hay elementos repetidos en postergables}
  requiere: {la intersección entre postergables y urgentes es vacía}
  requiere: {|postergables| = |urgentes|}
  asegura: {no hay repetidos en res }
  asegura: {res es permutación de la concatenación de urgentes y postergables}
  asegura: {Si urgentes no es vacía, en tope de res hay un elemento de urgentes}
  asegura: {En res no hay dos seguidos de urgentes}
  asegura: {En res no hay dos seguidos de postergables}
  asegura: {Para todo c1 y c2 de tipo "urgente" pertenecientes a urgentes si c1 aparece antes que c2 en urgentes entonces c1 aparece antes que c2 en res}
  asegura: {Para todo c1 y c2 de tipo "postergable" pertenecientes a postergables si c1 aparece antes que c2 en postergables entonces c1 aparece antes que c2 en res}
  """

def mostrar_cola (c:Cola[int]):
    contenedor:Cola[int]=Cola ()

    while not c.empty():
        elem = c.get()
        print (elem)
        contenedor.put(elem)

    while not contenedor.empty():
        c.put(contenedor.get())


def orden_de_atencion (urgentes: Cola[int], postergables: Cola[int]) -> Cola[int]:
    res:Cola[int]=Cola()
    c_urg:list[int] = []
    c_pos:list[int] = []

    while not (urgentes.empty() and postergables.empty()): #pongo lo de las colas en dos listas
        c_urg.append(urgentes.get()) 
        c_pos.append(postergables.get()) 

    for i in range (len(c_urg)): #pongo en la cola final lo que me pide con un for porque los datos están en listas
        res.put(c_urg[i])
        res.put(c_pos[i])

    for i in range (len(c_urg)): #restauro variables in de urgentes y postergables!
        urgentes.put(c_urg[i])
        postergables.put(c_pos[i])

    return res

#c1 = Cola()
#c1.put(8) #principio
#c1.put(10)
#c1.put(11)
#c1.put(2)
#c1.put(9) #final

#c2 = Cola()
#c2.put(15) #principio
#c2.put(3)
#c2.put(1)
#c2.put(99)
#c2.put(43) #final

#mostrar_cola (orden_de_atencion (c1,c2))

"""
3) Camas ocupadas en el hospital (2 puntos)
Queremos saber qué porcentaje de ocupación de camas hay en el hospital. El hospital se representa por una matriz en donde las filas son los pisos, y las columnas son las camas. Los valores de la matriz son booleanos que indican si la cama está ocupada o no. Si el valor es verdadero (True) indica que la cama está ocupada. Se nos pide programar en Python una función que devuelve una secuencia de enteros, indicando la proporción de camas ocupadas en cada piso.

problema nivel_de_ocupacion(camas_por_piso:seq⟨seq⟨Bool⟩⟩) : seq⟨R⟩ {
  requiere: {Todos los pisos tienen la misma cantidad de camas.}
  requiere: {Hay por lo menos 1 piso en el hospital.}
  requiere: {Hay por lo menos una cama por piso.}
  asegura: {|res| = |camas|}
  asegura: {Para todo 0<= i < |res| se cumple que res[i] es igual a la cantidad de camas ocupadas del piso i dividido el total de camas del piso i)}
}
"""

def nivel_de_ocupacion(camas_por_piso:list[list[bool]]) -> list[float]:
    res:list[bool] = []
    contador:int=0

    for piso in camas_por_piso:
        for cama in piso:
            if cama == True:
                contador +=1
        res.append(contador /len(piso))
        contador=0

    return res

info = [True,False], [False,False], [True,True],[True,False]
#print (nivel_de_ocupacion(info))

"""
4) Quiénes trabajaron más? (2 puntos)
Dado un diccionario con la cantidad de horas trabajadas por empleado, en donde la clave es el ID del empleado y el valor es una lista de las horas trabajadas por día, queremos saber quienes trabajaron más para darles un premio. Se deberá buscar la o las claves para la cual se tiene el máximo valor de cantidad total de horas, y devolverlas en una lista.

problema empleados_del_mes(horas:dicc⟨Z,seq⟨Z⟩⟩) : seq⟨Z⟩ {
  requiere: {No hay valores en horas que sean listas vacías}
  asegura: {Si ID pertence a res entonces ID pertence a las claves de horas}
  asegura: {Si ID pertenece a res, la suma de sus valores de horas es el máximo de la suma de elementos de horas de todos los otros IDs}
  asegura: {Para todo ID de claves de horas, si la suma de sus valores es el máximo de la suma de elementos de horas de los otros IDs, entonces ID pertences a res}
}
"""

#h2 = {"111": [1, 2, 3], "222": [2, 3, 4], "333": [4,5,6], "444": [4,5,6]}
def empleados_del_mes(horas:dict[int, list[int,int]]) -> list[int]:
    lista_horas:list[tuple[int,list[int]]] = list(horas.items()) #lista tuplas con clave y valor
    empleado_horas_totales:dict[int,int] = {}
    lista_horas_totales:list[tuple[str,int]] = []
    res:list[int] = []

    for c, v in lista_horas:
        suma:int=0
        for numero in v:
            suma += numero

        empleado_horas_totales [c] = suma #hago dicc con id : suma total de las horas
        lista_horas_totales.append (suma) #hago lista con sumas totales de diferentes empleados

    max_horas_trabajadas = maximo (lista_horas_totales) #busco maximo de la lista de sumas totales de horas
    
    for c, v in empleado_horas_totales.items(): # si hay más de un empleado con la misma cant de horas lo pone en la lista res
            if v == max_horas_trabajadas:
                res.append (c)

    return res

def maximo (s:list[int]):
    res:int = 0

    for dig in s:
        if dig > res:
            res = dig
    
    return res
    
"""
h1 = {"111": [1, 2, 3], "222": [2, 3, 4], "333": [4,5,6]}
print(empleados_del_mes(h1)) #["333"]
h2 = {"111": [1, 2, 3], "222": [2, 3, 4], "333": [4,5,6], "444": [4,5,6]}
print(empleados_del_mes(h2)) #["333","444"]
h2 = {"111": [1, 2, 3], "222": [2, 3, 4], "333": [4,5,6], "444": [4,5,6]}
print(empleados_del_mes(h2)) #["333","444"]
h3 = {"111": [1, 2, 3], "444": [6,7,8], "222": [2, 3, 4], "333": [4,5,6]}
print(empleados_del_mes(h3)) #["444"]
h4 = {"111": [1, 2, 3], "444": [6,7,8], "222": [8,9,10], "333": [4,5,6], "444": [8,9,10], "555": [6,7,8]}
print(empleados_del_mes(h4)) #["222","444"] o ["444","222"] (en los asegura no se habla del orden)
"""


#############################################################################
####  PARCIAL 2 ------- EJERCICIO 3  - RACHA MAS LARGA & TIEMPO MAS LARGO ###
#############################################################################

def promedio_de_salidas (registro: dict[str, list[int]]) -> dict[str, tuple[int,float]]:
    res:dict[str, tuple[int,float]] = {}

    for nombre, tiempos in registro.items():
        contador:int = 0
        suma:int = 0

        for numero in tiempos:
            if 0 < numero < 61:
                contador +=1
                suma += numero
        
        if contador !=0:
          res [nombre] = (contador, (suma / contador))

        else:
          res [nombre] = (0,0.0)

    return res

#dicc = {"a": [2,45,34,16,61,0,61,55], "b": [44,12,61,0,23,23,55], "c": [44,22,1,1,45,2], "d": [0,61]} #{"a": (5, 30.4), "b": (5,31,4), "c": (6,19.1667)}
#print (promedio_de_salidas (dicc))

def tiempo_mas_rapido (tiempos_salas: list [int]) -> int:
    res:int = -1
    min:int=61
    i:int=0

    while i < len (tiempos_salas):
        if (min > tiempos_salas[i]) and (0 < tiempos_salas [i] < 61):
          min = tiempos_salas [i]
          res:int= i 
        i+=1
    else:
        i+=1

    return res

#l = [8,61,9,9,7,61,0,44]
#print (tiempo_mas_rapido (l))

def racha_mas_larga (tiempos: list[int])-> tuple[int,int]:
    racha:int=0
    mayor_racha:int=0
    index:int=0

    for i in range (len(tiempos)):
        if 0 < tiempos[i] < 61:
            racha+=1
        else:
            racha=0

        if racha > mayor_racha:
           mayor_racha = racha
           index = i - mayor_racha + 1

    return (index, index + mayor_racha - 1)

#s = [8,61,23,45,53,61,8,0] # -> (2,4)
#print (racha_mas_larga (s))
#q = [45,53,3,61,8,0,45,60,1,73,9] #-> (0,2)
#print (racha_mas_larga (q))
#p = [8,61,23,0] #-> (0,0)
#print (racha_mas_larga (p))

def escape_en_solitario (amigos_por_salas: list[list[int]]) -> list[int]:
    res:list[int]=[]
    i:int = -1

    for sala in amigos_por_salas:
      if cumple_condicion (sala):
          i+=1
          res.append(i)
      else:
          i+=1

    return res

def cumple_condicion (s: list[int]) -> bool:
    return (s[0]== 0) and (s[1]==0) and (s[2]!= 0) and (s[3]==0)

    

#t = [[2,3,6,9],[0,0,0,0],[0,0,3,0],[0,0,61,0],[2,11,9,0],[0,0,4,1],[0,0,4,0]] # [2,3,6]
#d = [[2,3,6,9],[0,0,0,0]] # []
#print (escape_en_solitario (d))


#############################################################################
####  PARCIAL 3 ------- EJERCICIO                                         ###
#############################################################################

# 1) Fila en ExactaBank (1 puntos)
# En el banco ExactaBank los clientes hacen cola para ser atendidos por un representante. Los clientes son representados por
# las tuplas (nombre, tipo afiliado) donde la pimera componente es el nombre y el tipo afiliado puede ser "comun" o "vip".
# Se nos pide implementar una función en python que dada una cola de clientes del banco, devuelva una nueva cola con los
# mismos clientes pero en donde los clientes vip están primero que los clientes comunes manteniendo el orden original de los 
# clientes vips y los comunes entre sí.

def reordenar_cola_priorizando_vips(filaClientes: Cola[tuple[str,str]])-> Cola[str]:
    c_comun:list[tuple[str,str]] = []
    c_vip: list[tuple[str,str]] = []
    res :Cola[tuple[str,str]] = Cola ()
    contenedor: Cola[tuple[str,str]] = Cola ()

    while not filaClientes.empty(): #pongo en 2 listas diferentes a los clientes vip y comunes
        elem = filaClientes.get()   #y todos los elem en otra lista

        if elem[1] == "comun":
            c_comun.append (elem)
            contenedor.put (elem)
        else:
            c_vip.append (elem)
            contenedor.put (elem)

    while not (contenedor.empty()): #recupero variable in
        filaClientes.put (contenedor.get())

    for i in range (len (c_vip)): #pongo en la cola res lo que me piden
        res.put (c_vip[i][0])

    for i in range (len(c_comun)):
        res.put (c_comun[i][0])

    return res


def mostrar_cola (c:Cola[str]):
    contenedor:Cola[str]=Cola()

    while not c.empty():
        elem = c.get()
        print (elem)
        contenedor.put(elem)

    while not contenedor.empty():
        c.put(contenedor.get())

#h = Cola ()
#h.put (("h", "vip"))
#h.put (("a", "comun")) #principio
#h.put (("b", "vip"))
#h.put (("c", "comun"))
#h.put (("d", "vip")) 
#h.put (("j", "comun"))
#h.put (("k", "comun")) #final

#mostrar_cola (reordenar_cola_priorizando_vips (h))



#j = [1,2]
#j.pop ()
#print (j)

def torneo_de_gallinas(estrategias: dict[str,str]) -> dict[str,int]:
    jugadores:list[str] = list(estrategias.keys())
    aux:list[tuple[str,str]] = []
    res: dict[str,list[int]] = {}
    p1:int
    p2:int

    for j in range (len(jugadores)-1): #j= 0,1,2,
        for i in range (len(jugadores)-1): #i= 0,1,2
                indice:int = (len(jugadores)-1) #indice = 3
                aux.append((jugadores [indice], jugadores [i])) #aux = (d,a)(d,b)(d,c) -> aux=(d,a)(d,b)(d,c)(c,a)(c,b)(b,a)
        jugadores.pop()

    for player in estrategias.keys(): #hago diccionario res con mis jugadores y todos en 0 puntos
        res [player] = 0

    for dupla in aux:
        j1 = estrategias [(dupla[0])] #j1= desvia o no
        j2 = estrategias [dupla[1]] #j2= adesvia o no


        if j1 == "desvia" and j2 == "no desvia":
            p1 = res.pop((dupla[0]))
            p1 -= 15
            res [dupla[0]] = p1

            p2 = res.pop(dupla[1])    
            p2 +=  10
            res [dupla[1]] = p2
        
        if j2 == "desvia" and j1 == "no desvia":
            p2 = res.pop(dupla[1])
            p2 -= 15
            res [dupla[1]] = p2

            p1 = res.pop(dupla[0])    
            p1 +=  10
            res [dupla[0]] = p1

        if j1 == "no desvia" and j2 == "no desvia":
            p1 = res.pop(dupla[0])
            p1 -= 5
            res [dupla[0]] = p1

            p2 = res.pop(dupla[1])    
            p2 -= 5
            res [dupla[1]] = p2

        if j1 == "desvia" and j2 == "desvia":
            p1 = res.pop(dupla[0])
            p1 -= 10
            res [dupla[0]] = p1

            p2 = res.pop(dupla[1])    
            p2 -= 10
            res [dupla[1]] = p2

    return res



#dic = {"a" : "desvia", "b" : "no desvia", "c" : "no desvia", "d": "desvia"}
#print(torneo_de_gallinas (dic))