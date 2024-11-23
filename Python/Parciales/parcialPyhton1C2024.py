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

#mostrar_cola (c1)

def orden_de_atencion (urgentes: Cola[int], postergables: Cola[int]) -> Cola[int]:
    res:Cola[int]=Cola()
    c_urg:list[int] = []
    c_pos:list[int] = []

    while not (urgentes.empty() and postergables.empty()):
        elem:int= urgentes.get()
        c_urg.append(elem) and res.put(elem)

        elem2 = postergables.get()
        c_pos.append(elem2) and res.put(elem2) 

    while not (c_urg.empty() and c_pos.empty()):
        urgentes.put(c_urg.get())
        postergables.put(c_pos.get())

    return res

c1 = Cola()
c1.put(8) #principio
c1.put(10)
c1.put(11)
c1.put(2)
c1.put(9) #final

c2 = Cola()
c2.put(15) #principio
c2.put(3)
c2.put(1)
c2.put(99)
c2.put(43) #final

mostrar_cola (orden_de_atencion (c1,c2))