from queue import Queue as Cola
from queue import LifoQueue as Pila
p = Pila ()
c = Cola ()

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
print (nivel_de_ocupacion(info))

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

def empleados_del_mes(horas:dict[int, list[int,int]]) -> list[int]:
    aux: list[tuple[int,int]] = []
    res: list[int] = []

    for v, lista in horas.items():
        aux.append ((v,(suma_total (lista))))

    res = encontrar_maximos(aux)

    return res

def encontrar_maximos (l:list[tuple[int,int]]) -> list[int]:
    res:list[int]
    max:int=-1

    for i in range (len(l)-1):
        if l[i] > l[i+1]:
             max = l[i]
    
    l.pop(max)

    if pertenece
          


def suma_total (s:list[int]) -> int:
    res:int=0

    for n in s:
        res+=n

    return res

    