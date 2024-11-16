                --------GUIA 2--------

duplicar :: Integer -> Integer
duplicar n = 2 * n

--enteroMasCercano :: Float -> Integer
--enteroMasCercano n = ??

--raizCuadrada :: Integer -> Float
--raizCuadrada n = sqrt n

maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 a b c 
    | a >= b &&  a >= c = a
    | b >= a && b >= c = b
    | otherwise = c

sumaSinRepetidos :: Integer -> Integer -> Integer -> Integer
sumaSinRepetidos x y z 
    | x == y && y == z && x == z = 0
    | x == y = z
    | x == z = y
    | y == z = x
    | otherwise = x + y + z

digitoUnidades :: Integer -> Integer
digitoUnidades a = mod a 10

digitoDecenas :: Integer -> Integer
digitoDecenas a = mod (div a 10) 10

todoMenor :: (Float, Float) -> (Float, Float) -> Bool
todoMenor (x,y) (z,w) = x < z && y < w

ordenar :: (Ord t) => [t] -> [t]
ordenar [] = []
ordenar l = ordenar (quitar (maximo l) l) ++ [maximo l]

maximo :: (Ord t) => [t] -> t
maximo (x:[]) = x 
maximo (x:xs) 
    | x >= head xs = maximo (x:tail xs)
    | otherwise = maximo (head xs: tail xs) 

quitar :: (Eq t) => t -> [t] -> [t] --con Integer tambien funciona
quitar a [] = []
quitar a (x:xs) 
    | a == x = xs
    | otherwise= x : quitar a xs

duplicarTodos :: [Integer] -> [Integer]
duplicarTodos (x:[]) = [2*x]
duplicarTodos (x:xs) = 2*x : duplicarTodos xs

            --------GUIA 3--------
absoluto :: Integer -> Integer
absoluto x 
    | x >= 0 = x
    | otherwise = -x

algunoEs0 :: Float -> Float -> Bool
algunoEs0 _ 0 = True
algunoEs0 0 _ = True
algunoEs0 _ _ = False

algunoEs0Bis :: Float -> Float -> Bool
algunoEs0Bis x y = x == 0 || y == 0 

ambosSon0 :: Float -> Float -> Bool
ambosSon0 x y = x == 0 && y == 0

mismoIntervalo :: Float -> Float -> Bool
mismoIntervalo x y = (x <= 3 && y <= 3) || (x > 3 && x <= 7) && (y > 3 && y <= 7) || x>7 && y > 7

esMultiploDe :: Int -> Int -> Bool
esMultiploDe x y = mod x y == 0 

estanRelacionados :: Integer ->Integer ->Bool
estanRelacionados a b | mod a b ==0 = True
                      | otherwise = False

distanciaPuntos :: Float -> Float -> Float
distanciaPuntos x y = sqrt(x**2 + y**2)

sumarSoloMultiplos :: (Int, Int, Int) -> Int -> Int
sumarSoloMultiplos (a,b,c) e 
    | mod a e /= 0 && mod b e /= 0 && mod c e /= 0 = 0
    | mod a e /= 0 && mod b e /= 0 && mod c e == 0 = c
    | mod a e /= 0 && mod b e == 0 && mod c e /= 0 = b
    | mod a e == 0 && mod b e /= 0 && mod c e /= 0 = a
    | mod a e == 0 && mod b e == 0 && mod c e /= 0 = a+b
    | mod a e == 0 && mod b e /= 0 && mod c e == 0 = a+c
    | mod a e /= 0 && mod b e == 0 && mod c e == 0 = b+c
    | otherwise = a+b+c

posPrimerPar :: (Int,Int,Int) -> Int
posPrimerPar (a,b,c) 
    | (mod a 2 == 0) = a
    | (mod b 2 == 0) = b
    | (mod c 2 == 0) = c
    | otherwise = 4

crearPar :: a -> b -> (a, b)
crearPar x y = (x,y)

type Anio = Integer
type EsBisiesto = Bool

bisiesto :: Anio -> EsBisiesto
bisiesto x 
    | mod x 4 /=0 = False
    | (mod x 100 == 0) && (mod x 400 /= 0) = False
    | otherwise = True 

            --------GUIA 3-------

fib :: Integer -> Integer
fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-2) 

parteEntera :: Float -> Integer
parteEntera 0 = 0
parteEntera n | n >= 0 && n < 1 = 0
parteEntera n = 1 + parteEntera (n-1)

esDivisible :: Integer -> Integer -> Bool
esDivisible a b = mod b a == 0

--sumaImpares 3 ; 1+3+5 ⇝ 9
sumaImpares :: Integer -> Integer
sumaImpares 1 = 1
sumaImpares n = sumaImpares (n-1) + (2*n-1)

factorial :: Integer -> Integer
factorial 0 = 1
factorial n = factorial (n-1) * n

medioFact :: Int -> Int
medioFact 0 = 1
medioFact 1 = 1
medioFact n = n * medioFact (n-2)

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n 
    | n < 10 = True
    | otherwise = mod n 10 == mod (div n 10) 10 && todosDigitosIguales (div n 10)

--olvidate que me aprenda algo de todo esto
cantidadDigitos :: Int -> Int
cantidadDigitos n 
    | n < 10 = 1
    | otherwise = 1 + cantidadDigitos (div n 10)

iesimoDigito :: Int -> Int -> Int
iesimoDigito n 1 =  div n (10 ^ ((cantidadDigitos n)-1))
iesimoDigito n i = iesimoDigito ( mod n (10 ^ ((cantidadDigitos n)-1))) (i-1)

capicua :: Int -> Bool
capicua n 
    | n < 10 = True
    | otherwise = (ultimo n == primero n) && capicua (sacarBordes n)
        where ultimo n = iesimoDigito n (cantidadDigitos n)
              primero n = iesimoDigito n 1
              sacarBordes n = div (mod n (10 ^ (cantidadDigitos n - 1))) 10

--1231 = 1 +2 3+ 1
sumaDigitos :: Integer ->Integer
sumaDigitos n 
    | n < 10 = n
    | otherwise = mod n 10 + sumaDigitos (div n 10)

eAprox :: Integer ->Float
eAprox 0 = 1
eAprox n = eAprox (n-1) + (1 / fromIntegral (factorial n))

raizDe2Aprox :: Integer -> Float
raizDe2Aprox 1 = 1
raizDe2Aprox n = aux (n)- 1

aux :: Integer -> Float
aux 1 = 2
aux n = 2 + (1 / aux (n-1))

menorDivisor :: Integer ->Integer
menorDivisor 1 = 1
menorDivisor n = menorDivisorDesde 2 n

menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde e n
    | mod n e == 0 = e
    | mod n e /= 0 = menorDivisorDesde (e+1) n

esPrimo :: Integer ->Bool
esPrimo 1 = False
esPrimo n = menorDivisor n == n

sonCoprimos :: Integer ->Integer ->Bool 
sonCoprimos 1 _ = True
sonCoprimos _ 1 = True
sonCoprimos x y 
    | x == y = False
    | (mod x y == 00 ) || (mod y x == 00 )= False
    | menorDivisor x == menorDivisor y = False 
    | menorDivisor x /= menorDivisor y = True 

-- pn es el minimo numero natural MAYOR A pn-1 que sea primo
nEsimoPrimo :: Integer ->Integer
nEsimoPrimo 1 = 2
nEsimoPrimo n = minimoPrimoDesde (nEsimoPrimo (n-1) + 1)

minimoPrimoDesde :: Integer -> Integer
minimoPrimoDesde n 
    | esPrimo (n) = n
    | otherwise = minimoPrimoDesde (n+1)

--10? -> True xq [2+3+5]
--11? -> False xq [2+3+5]= 10 y [2+3+5+7]=17
esSumaInicialDePrimosDesde :: Integer -> Integer -> Bool
esSumaInicialDePrimosDesde n i
    | n < 0 = False
    | n == 0 = True
    | otherwise = esSumaInicialDePrimosDesde (n - nEsimoPrimo i) (i+1)

esSumaInicialDePrimos :: Integer -> Bool
esSumaInicialDePrimos n = esSumaInicialDePrimosDesde n 1

--nunca en mi vida se me hubiera ocurrido esto: le va restado el nEsimo 
--primo desde nEsimo1= 2 a la supuesta suma los primos, y si llega a 0 es que es y si se pasa es que no

esFibonacci :: Integer -> Bool
esFibonacci n = esFibonacciDesde 1 n

esFibonacciDesde :: Integer -> Integer -> Bool
esFibonacciDesde desde n 
    | fib (desde) == n = True
    | fib (desde) > n = False
    | otherwise = esFibonacciDesde (desde+1) n

--EJERCICIO 18 Y 20