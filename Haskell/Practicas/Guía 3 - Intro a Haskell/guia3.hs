-------EJERCICIO 1-------

f :: Integer -> Integer 
f n | n == 1 = 8
    | n == 4 = 131
    | n == 16 = 16
    | otherwise = false ? --no hace falta, no me lo pide

g :: Integer -> Integer
g n | n == 8 = 16
    | n == 16 = 4
    | n == 131 = 1

h :: Integer -> Integer
h n = f (g n)

k :: Integer -> Integer
k n = g (h n)

también se puede hacer:

f 1 = 8
f 4 = 131
f 16 = 16

------EJERCICIO 2-------

absoluto :: Num a => a -> a
absoluto a = abs a

maximo :: Integer -> Integer -> Integer -> Integer
maximo x y z | x >= y && x >= z = x
             | y >= z && x >= x = y
             | otherwise = z 

algunoEs0::Float -> Float-> Bool
algunoEs0 0 _ = True
algunoEs0 _ 0 = True
algunoEs0 _ _ = False

algunoEs0Bis::Float->Float->Bool
algunoEs0Bis x y = x==0 || y== 0

ambosSon0 :: Float -> Float -> Bool
ambosSon0 0 0 = True
ambosSon0 _ _ = False

ambosSon0Bis :: Float -> Float -> Bool
ambosSon0Bis x y = x == 0 && y == 0

mismoIntervalo :: Float -> Float -> Bool
mismoIntervalo x y | x <= 3 && y <= 3 = True
                   | x > 3 && y <= 7 = True
                   | x > 7 && y > 7 = True
                   | otherwise = False

sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos x y z | x /= y && x /= z && y /= z = x + y + z
                    | x == y && x /= z && y /=z = z
                    | y == z && x /= z && y /=x = x 
                    | x == z && x /= y && y /=z = y 
                    | otherwise = 0

--mas facil y eficiente--
sumaDistintos x y z | x == y && y == z = 0
                    | x == y = z
                    | y == z = x
                    | otherwise = a+b+c

esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe a b = mod a b == 0 

digitoUnidades :: Integer -> Integer
digitoUnidades n = mod (abs n) 10 

-- PREGUNTAR POR EL ABS QUE FUNCIONA EN INTEGER
--funciona en neg por el absoluto

digitoDecenas x = digitoUnidades (div x 10)

------EJERCICIO 3-------

estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados a b | mod a b ==0 = True
                      | otherwise = False

-- nunca lo hubiera pensado asi che

------EJERCICIO 4-------

productoInterno :: (Float, Float) -> (Float, Float) -> Float
productoInterno (a,b) (c,d) = a*c+b*d  

todoMenor :: (Float, Float) -> (Float, Float) -> Bool
todoMenor x y | ((fst x) < (fst y)) && ((snd x) < (snd y)) = True
              | otherwise = False

-- o mejor

todoMenor (a,b) (c,d) |a < c && b < d 
                       | otherwise = False

-- o mejor aun

todoMenor (a,b) (c,d) = a < c && b < d 


distanciaPuntos :: (Float, Float) -> (Float, Float) -> Float
distanciaPuntos (a,b) (c,d) = sqrt ((c-a)^2 + (d-b)^2)

sumaTerna :: (Float, Float, Float) -> Float
sumaTerna (a, b, c) = a + b + c
!!!!! PREGUNTAR !!!!! 


posPrimerPar: dada una terna de enteros, devuelve la posici´on del primer n´umero par si es que hay alguno, y devuelve
4 si son todos impares

posPrimerPar :: (Int, Int, Int) -> Int 
posPrimerPar (a,b,c) 
    | mod a 2 == 0 = 1
    | mod b 2 == 0 = 2
    | mod c 2 == 0 = 3
    | (mod a 2 == 1) && (mod b 2 == 1) && (mod c 2 == 1) = 4

!!!!! por qué no / diferencia en este caso entre && y || !!!!!!
-- son enteros asi que contempé todos los casos

posPrimerPar :: (Int, Int, Int) -> Int 
posPrimerPar (a,b,c) = (mod a 2 == 0 = 1) || (mod b 2 == 0 = 2) || (mod c 2 == 0 = 3) ||  MAL

-- no está dentro de haskell poner dos veces una misma linea un "="

sumarSoloMultiplos::(Int,Int,Int)->Int->Int
sumarSoloMultiplos (a,b,c) d | mod a d == 0 && mod b d == 0 && mod c d == 0 = a+b+c
                             | mod a d == 0 && mod b d == 0 && mod c d /= 0 = a+b
                             | mod a d == 0 && mod b d /= 0 && mod c d == 0 = a+c
                             | mod a d /= 0 && mod b d == 0 && mod c d == 0 = b+c
                             | mod a d == 0 && mod b d /= 0 && mod c d /= 0 = a
                             | mod a d /= 0 && mod b d == 0 && mod c d /= 0 = b
                             | mod a d /= 0 && mod b d /= 0 && mod c d == 0 = c
                             | otherwise = 0

todoMenor :: Punto2D -> Punto2D -> Bool
type Punto2D = (Float, Float)
todoMenor (a,b) (c,d) = a < c && b < d 

invertir :: (a,b) -> (b,a)
invertir (a,b) = (b,a)

------EJERCICIO 5-------

todosMenores :: (Int -> Int -> Int) -> Bool
todosMenores (a,b,c) = f (a) > g (a) && f (b) > g (b) && f (c) > g (c)

f :: Int -> Int
f n | n <= 7 = n^2
    | n > 7 = 2*n - 1

g :: Int -> Int
g n | mod n 2 == 0 = div n 2
    | mod n 2 == 1 = 3*n + 1

POR QUÉ NO ME FUNCIONA

------EJERCICIO 6-------


------EJERCICIO 7-------

absoluto x | x >= 0 = x
           | x <= 0 = -x

distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (p0,p1,p2) (q0,q1,q2) = absoluto (p0-q0) + absoluto (p1-q1) + absoluto (p2 - q2)

------EJERCICIO 8-------

comparar :: Int -> Int -> Int
comparar a b 
    |sumaUltimosDigitos (a) < sumaUltimosDigitos (b) = 1
    |sumaUltimosDigitos (a) > sumaUltimosDigitos (b) = -1
    |otherwise = 0

sumaUltimosDigitos :: Int -> Int
sumaUltimosDigitos x = unidad x + decena x

unidad :: Int -> Int
unidad x = mod (absoluto x) 10

decena :: Int -> Int
decena x = unidad (div x 10)

------EJERCICIO 9-------

a) problema f1 (n: R) : R {
    requiere: True
    asegura: res= 1 <-> n=0
    asegura: res= 0 <-> n /=0
}

b) problema f2 (n:R) : R {
    requiere: n = 1 o n = -1
    asegura: res= 15 <-> n= 1
    asegura: res=-15 <-> n=-1
}

c) problema f3 (n:R) : R {
    requiere: True
    asegura: res= 7 <-> n <= 9
    asegura: res= 5 <-> n > 9
}

d) problema f4 (a: R, b: R) : R {
    requiere: True
    asegura: res= (a+b) / 2

e) problema f5 (n: R x R) : R {
    requiere: True
    asegura: res= (n0+n1) / 2
}

f) problema f6 (a: R, b: Z) : Bool
    requiere: True
    asegura: res= a <-> [a]=b