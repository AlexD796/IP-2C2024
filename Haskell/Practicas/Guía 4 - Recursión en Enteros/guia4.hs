-----------------EJ 1-----------------------
fibonacci:: Integer ->Integer
fibonacci n 
    | n == 0 = 0
    | n == 1 = 1
    | otherwise = fibonacci (n-1) + fibonacci (n-2)

fib2 :: Integer ->Integer
fib2 0 = 1
fib2 1 = 1
fib n = fib(n-1) + fib(n-2)

-----------------EJ 2------------------------
parteEntera :: Float -> Integer
parteEntera 0 = 0 --innecesario--
parteEntera n | n >= 0 && n <= 1 = 0
parteEntera n = 1 + parteEntera (n-1)

parteEntera :: Float -> Integer
parteEntera 0 = 0
parteEntera n = 1 + parteEntera (n-1)

-- parteEntera 2.3
-- 1  + parteEntera (1.3)
-- 1  + 1  + parteEntera (0.3 - 1)
-- 1  + 1  + parteEntera (-0.3 - 1)

--------> MAL

-----------------EJ 3------------------------
esDivisible :: Integer -> Integer -> Bool
esDivisible a b 
    | (a-b) < 0 = False
    | (a-b) == 0 = True
    | otherwise = esDivisible (a-b) b 

-----------------EJ 4------------------------
sumaImpares :: Integer -> Integer
sumaImpares 0 = 0
sumaImpares n = sumaImpares (n-1) + (2*n - 1)

-----------------EJ 5------------------------
medioFact :: Integer -> Integer
medioFact 0 = 1
medioFact 1 = 1
medioFact n = n * medioFact (n-2)

-----------------EJ 6------------------------

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | n < 10 = True
todosDigitosIguales n | otherwise = ultimo n == ultimo (div n 10) && todosDigitosIguales (div n 10)
    where ultimo n = mod n 10

-----------------EJ 7------------------------
cantDigitos :: Int -> Int
cantDigitos n | n < 10 = 1
cantDigitos n | otherwise = cantDigitos (div n 10) + 1

iEsimoDigito :: Int -> Int -> Int
iEsimoDigito n 1 = div n (10 ^ ((cantidadDigitos n)-1))
iEsimoDigito n i = iEsimoDigito sacarPrimero (i-1)
    where sacarPrimero = mod n (10 ^ ((cantidadDigitos n)-1))

-----------------EJ 8------------------------
sumaDig :: Int -> Int
sumaDig n | n < 10 = n
          | otherwise = sumaDig (div n 10) + (mod n 10)

-----------------EJ 9------------------------
capicua :: Int -> Bool
capicua n 
    | n < 10 = True
    | otherwise = (ultimo n == primero n) && capicua (sacarBordes n)
        where ultimo n = iesimoDigito n (cantDigitos n)
              primero n = iesimoDigito n 1
              sacarBordes n = div (mod n (10 ^ (cantDigitos n - 1))) 10


-----------------EJ 10------------------------
f1::Integer -> Integer
f1 0=1
f1 n=2^n + f1 (n-1)

f2 :: Integer -> Float -> Float
f2 1 q = q
f2 n q = q^n + f2 (n-1) q

-----------------EJ 11------------------------
eAprox :: Integer -> Integer
eAprox n 
    | n == 1 = 2
    | otherwise = 1 / (factorial n) + eAprox (n - 1)

factorial :: Integer -> Integer
factorial n | n == 0 = 1
            | n > 0 = n * factorial (n-1)
????
-----------------EJ 12------------------------
raiz2Aprox :: Int -> Float
raiz2Aprox n 
    | n == 1 = 1
    | otherwise = recursion n - 1

recursion :: Int -> Float
recursion n 
    | n == 1 = 2
    | otherwise = 2 + (1 / recursion (n-1))

-----------------EJ 13------------------------
sumatoriaSimple:: Integer -> Integer -> Integer
sumatoriaSimple _ 0 = 0
sumatoriaSimple n j  = I^j + sumatoriaSimple I (j-1)

sumatoriaDoble :: Integer -> Integer -> Integer
sumatoriaDoble 0 _ = 0
sumatoriaDoble n m = sumatoriaSimple n m + sumatoriaDoble (n-1) m 

-----------------EJ 14------------------------
sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias _ 0 _ = 0
sumaPotencias q n m = sumaPotSimple q n m + sumaPotencias q (n-1) m

sumaPotSimple :: Integer -> Integer -> Integer -> Integer
sumaPotSimple _ _ 0 = 0
sumaPotSimple q n m = q ^ (n+m) + sumaTerminoExterno q n (m-1)

-----------------EJ 15------------------------
sumaRacInt :: Integer -> Integer -> Float
sumaRacInt _ 0 = 0
sumaRacInt p q = fromIntegral p / fromIntegral q + sumaRacInt p (q-1)

sumaRac :: Integer -> Integer -> Float
sumaRac 0 _ = 0
sumaRac n m = sumaRacInt n m + sumaRac (n-1) m

-----------------EJ 16------------------------
esPrimo :: Int -> Bool
esPrimo n = n == menorDivisor == n 

menorDivisor :: Int -> Int 
menorDivisor n = menorDivisorDesde 2 n

menorDivisorDesde :: Int -> Int -> Int
menorDivisorDesde desde n 
    | mod n desde == 0 = desde
    | otherwise = menorDivisorDesde (desde + 1)

sonCoprimos :: Integer ->Integer ->Bool 
sonCoprimos 1 _ = True
sonCoprimos _ 1 = True
sonCoprimos x y 
    | (x == y) || (mod x y == 0) || (mod y x == 0) = False
    | menorDivisor x == menorDivisor y = False 
    | menorDivisor x /= menorDivisor y = True 

nEsimoPrimo::Integer->Integer
nEsimoPrimo 1 = 2
nEsimoPrimo n = siguientePrimo (nEsimoPrimo (n-1))
-- Devuelve el primo nº n, 
-- Ej: nEsimoPrimo 4 = 7, nEsimoPrimo5=11 , nEsimoPrimo 19=67

siguientePrimo::Integer->Integer
siguientePrimo n | esPrimo (n+1) = n+1
                 | otherwise = siguientePrimo (n+1)
-- Si el siguiente numero es primo, devuelve ese numero, si no, vuelve a chequear hasta tener uno primo
-- Ej: siguientePrimo 3 = 5, siguientePrimo 5=7, siguientePrimo 6=7

-----------------EJ 17------------------------
esFibonacci :: Integer -> Bool
esFibonacci n = esFibonacciDesde 1 n

esFibonacciDesde :: Integer -> Integer -> Bool
esFibonacciDesde desde n 
    | fib (desde) == n = True
    | fib (desde) > n = False
    | otherwise = esFibonacciDesde (desde+1) n

-----------------EJ 18------------------------
mayorDigitoPar :: Integer -> Integer
mayorDigitoPar n 
    | (n < 10) && (mod n 2 == 0) = n
    | (n < 10) && (mod n 2 /= 0) = -1
    | even ultimoDigito = max ultimoDigito (mayorDigitoPar div n 10)
    | otherwise = mayorDigitoPar nRecortado
        where ultimoDigito = mod n 10

-----------------EJ 19------------------------
--10? -> True xq [2+3+5]
--11? -> False xq [2+3+5]= 10 y [2+3+5+7]=17
sumaInicialDePrimos :: Integer -> Bool 
sumaInicialDePrimos n = sumaInicialDePrimosDesde 1 n

sumaInicialDePrimosDesde :: Integer -> Integer -> Bool
sumaInicialDePrimosDesde i n 
    | n == 0 = True
    | n < 0 = False
    | otherwise = sumaInicialDePrimosDesde (n - nEsimoPrimo i) (i+1)
--nunca en mi vida se me hubiera ocurrido esto: le va restado el nEsimo 
--primo desde nEsimo1= 2 a la supuesta suma los primos, y si llega a 0 es que es y si se pasa es que no