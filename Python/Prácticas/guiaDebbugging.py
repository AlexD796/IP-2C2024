#EJERCICIO 1 >>> estaba mal asignado el esMenor = "False" y el return era otra cosa

def esta_ordenado_asc(v):
    i = 0
    longitud = len(v)
    esMenor = True
    while i <= longitud -2 and esMenor:
        esMenor = v[i] <= v[i + 1]
        i += 1
    return esMenor
        
def esta_ordenado_desc(v):
    longitud = len(v)
    i = 0
    esMayor = True
    while i <= longitud - 2 and esMayor:
        esMayor = v[i] >= v[i + 1]
        i += 1
    return i == longitud - 1
