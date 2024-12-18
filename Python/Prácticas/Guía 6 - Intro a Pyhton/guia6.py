import math

#EJERCICIO 1
def imprimir_hola_mundo () -> None: 
    print ('Hola Mundo')
#imprimir_hola_mundo ()

def imprimir_un_verso() -> None:
    print ("¿Qué importan ya tus ideales\n ¿Qué importa tu canción?\n La grasa de las capitales\n Cubre tu corazón\n")

def raizDe2 () -> int:
    return round (math.sqrt (2), 4)
#print (raizDe2 ())

def factorial_de_dos () -> int:
    return math.factorial (2)

#print (factorial_de_dos ())

def perimetro() -> float:
    res: float = 2* math.pi
    return res
#print(perimetro ())

#EJERCICIO 2

def imprimir_saludo (nombre: str) -> None:
    print ("Hola "+ nombre)
#imprimir_saludo ("lauti")

def raiz_cuadrada_de(numero: int) -> float:
    return math.sqrt (numero)
#print (raiz_cuadrada_de(17))

def lala (numero:int) -> int:
    return math.factorial (numero - 0.50)

#print (lala (7.50)) no funciona por el tipado fuerte 

def fahrenheit_a_celsius (temp: float) -> float:
    return round (((temp-32) * 5 / 9), 5) #me pinto redondear 5 decimales

#print( fahrenheit_a_celsius (345))

def imprimir_dos_veces(estribillo: str) -> None:
    print (estribillo*2)

#imprimir_dos_veces ("gente loca")

def problema_es_multiplo_de (n:int, m:int) -> bool:
    return n % m == 0 
# resto: int = n % m
# if: resto == 0
    #return True
#else: NO PRACTICO
    #return False
#print (problema_es_multiplo_de (4,8))

def es_par(numero:int) -> bool:
    return problema_es_multiplo_de (numero, 2) 

#print (es_par (8))

def cantidad_de_pizzas(comensales:int, min:int) -> int:
    return math.ceil (comensales * min / 8)

# 8 com 2 min -> 16 porciones / 8 -> 2 pizzas
# 5 comensales 3 min -> 15 porciones / 8 -> 1.875... -> 2 pizzas
# 31 comensales 4 min -> 124 / 8 -> 15.5... -> 16 pizzas

#EJERCICIO 3

def alguno_es_0(n1:float, n2:float) -> bool: 
    return n1==0 or n2==0

def ambos_son_0(n1:float, n2:float) -> bool:
    return n1==0 and n2==0

#print (ambos_son_0 (0,0.3))

def es_nombre_largo (nombre:str) -> bool:
    return  3 <=len (nombre)<= 8

#print (es_nombre_largo ("Lu")) #False
#print (es_nombre_largo ("Joni")) #True
#print (es_nombre_largo ("Guadalupe")) #False

def es_bisiesto(año:int) -> bool:
    return (año%400==0) or ((año%4==0) and (not(año%100==0)))
 
#def es_bisiesto(año:int)->bool: look at the !
  # return (año%4==0) and ((año%100!=0) or (año%400==0))

#print (es_bisiesto (400)) #TRUE
#print (es_bisiesto (40)) #TRUE
#print (es_bisiesto (32)) #TRUE
#print (es_bisiesto (440)) #TRUE
#print (es_bisiesto (1)) #FALSE
#print (es_bisiesto (900)) #FALSE

#EJERCICIO 4
#altura en m, devuelve kg
def peso_pino (altura_pino: int) -> int:
    if altura_pino <= 3:
        return altura_pino *300
    else:
        return 900 + (altura_pino - 3)*200

def es_peso_util (peso:int) -> bool:
    return 400 <= peso <= 1000

def sirve_pino (altura:int) -> bool:
    return es_peso_util (peso_pino (altura))

#print (sirve_pino (3.5))

#EJERCICIO 5

def devolver_el_doble_si_es_par (numero:int) -> int:
    if numero%2 == 0:
        return numero *2
    else:
        return numero

#print (devolver_el_doble_si_es_par (-3))
def devolver_valor_si_es_par_sino_el_que_sigue (n:int) -> int:
    if n%2 == 0:
         return n 
    else:
        return n + 1

def devolver_valor_v2 (n:int) -> int:
    if n%2 == 0:
        return n 
    if n%2 == 1:
        return n + 1

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(n:int) -> int:
    if n%3==0:
        return 2*n
    elif n%9==0:
        return 3*n
    else:
        return n 

def devolver_v2(n:int) -> int:
    if n%3==0 and  n%9!=0:
        return 2*n
    if (n%3==0 and n%9==0):
        return 3*n
    if (n%3!=0 and n%9!=0):
        return n 

#print (devolver_v2 (18))

def lindo_nombre(n:str) -> None:
    if len(n) >= 5:
        print ("Tu nombre tiene muchas letras")
    else:
        print ("Tu nombre tiene menos de 5 caracteres")

#lindo_nombre ("lala")

def elRango(numero:int) -> None:
        if numero <=5:
            print ("Menor a 5")
        elif 10<= numero <= 20:
            print ("Entre 10 y 20")
        elif numero >= 20:
            print ("Mayor a 20")

#elRango (16)

def vacas_o_laburo (sexo:chr, edad:int):
    if (0<=edad<= 18) or (sexo =="M" and edad>=65) or (sexo=="F" and edad>=60):
        print ("Andá de vacaciones")
    else:
        print ("Te toca trabajar")

#vacas_o_laburo ("A", 65)

#EJERCICIO 6 y 7
def imprimir_del_1_al_10 ():
    inicio:int=1
    fin:int=10
    paso:int=1
    while inicio <= fin:
        print (inicio)
        inicio += paso

def imprimir_1_10_for ():
    for n in range(1,11,1):
        print (n)

def imprimir_pares ():
    inicio: int = 10
    fin: int = 40
    paso: int = 1

    while inicio <= fin:
       if inicio % 2 == 0:
           print (inicio)
       inicio += paso

def imprimir_pares_for ():
        for n in range (10,41,1):
            if n % 2 == 0:
                print (n)

def imprimir_eco ():
    inicio:int=1
    fin:int=10
    while inicio <= fin:
        print ("eco")
        inicio = 1 + inicio

def imprimir_eco_for ():
    for n in range(1,11,1):
        print ("eco")

def despegar (n:int):
    while (n >= 0):
        print (n)
        n -=1
    print ("Despegue!!")

def despegar_for (n:int):
    for i in range (n, 0, -1):
        print (i) 
    print ("Despegue!!!")

def viaje_en_el_tiempo (partida: int, llegada:int):
    while partida > llegada :
        partida -=1
        print ("Viajó un año al pasado, estamos en el año:"+str(partida))

def viaje_en_el_tiempo_for (partida: int, llegada:int):
    for i in range (partida, llegada,-1):
         partida -=1
         print ("Viajó un año al pasado, estamos en el año:" +str(partida))

def viaje_en_el_tiempo_aristoteles (partida: int, llegada:int):
    while partida >= -364 :
        partida-=20
        print ("Viajó 20 años al pasado, estamos en el año:"+str(partida))
  #  if partida < -384: #tambien se podria usar break mepa (no se como me salio esto)
#print ("Viajó 20 años al pasado, estamos en el año:"+str(partida)) 


def viaje_en_el_tiempo_aristoteles_for (partida: int, llegada:int):
    for i in range(partida,-365,-20):
        partida -= 20 #de nuevo, ni idea como lo hice pero salio capaz con un break seria mas facil de entender
        print ("Viajó 20 años al pasado, estamos en el año:"+str(partida))

#EJERCICIO 8

def ej_1 (x:int, y:int) -> int:
    x = x + y
    return x



def ej_2 (x:int,y:int) -> int:
    z = x + y
    y = z * 2
    return y 

def ej_3 () -> None:
    x = 5
    y = 7
    x = "hora"
    y = x*2
    return y

def ej_4 ():
    x = False
    return not (x)

def ej_5 ():
    x = False
    x = not (x)
    return  not (x)

def ej_6 ():
    x = True
    y = False
    res= x and y 
    x = res and x
    return not x

#print (ej_6 ())

#EJERCICIO 9

def rt(x: int, g: int) -> int:
    g = g + 1
    return x + g

g: int = 0
def ro(x: int) -> int:
    global g
    g = g + 1
    return x + g

#ro (1)