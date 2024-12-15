{-PARIAL TEMA MAÑANA CUATRI 2C 2024-}
{-EJ 1-}

{-EJ 2-}
{-si es PRIMO la cantidad de factores primos de ese número-}

esAtractivo :: Integer -> Bool
esAtractivo 1 = False
esAtractivo n = esPrimo (cantidadDivisoresPrimos n)

cantidadDivisoresPrimos :: Integer -> Integer
cantidadDivisoresPrimos n = contarDivisoresPrimosDesde 2 n 
--hay una amnera mucho mas eficiente........
contarDivisoresPrimosDesde :: Integer -> Integer -> Integer
contarDivisoresPrimosDesde d n | d == n && esPrimo d = 1 -- CB : luego de dividir a el n por los factores primos que encontramos -> si factor == n entonces sumamos un ultimo divisor
                              -- | d == n && not (esPrimo d) = 0 --cuando llega hasta acá? CREO INNECESARIO xq nunca d va a ser compuesto y ser igual a n porque lo estamos dividiendo solamente pro sus factores primos a n
                               | (esPrimo d) && loDivide = 1 + contarDivisoresPrimosDesde d (div n d) -- si d es primo y lo divide es factor -> luego recursiono con el numero dividido ese divisor
                               | otherwise = contarDivisoresPrimosDesde (d+1) n -- si n es diferente a d, d es primo y no divide entonces sigo buscando factor primo
                               where loDivide = mod n d == 0

esPrimo :: Integer -> Bool
esPrimo 1 = False
esPrimo n = menorDivisor n == n

menorDivisor :: Integer -> Integer
menorDivisor n = menorDivisorDesde 2 n

menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde desde n 
    | mod n desde == 0 = desde
    | otherwise = menorDivisorDesde (desde+1) n


---aca solo con esto ya cuenta la cant de divisores, faltaria fijarse que es primo
cantFactores :: Integer -> Integer
cantFactores 1 = 0
cantFactores n = cantFactoresAux 2 n

cantFactoresAux :: Integer -> Integer -> Integer
cantFactoresAux d n 
    | d == n = 1
    | mod n d == 0 = 1 + cantFactoresAux d (div n d)
    | mod n d /= 0 = cantFactoresAux (d+1) (n)

{-EJ 3-}
--"abc " yes --"gijj lopq" yes --"kaka" no --en haskell las palabras son list[char] por eso funcionan como listas
palabraOrdenada :: String -> Bool
palabraOrdenada [] = True
palabraOrdenada (x:[]) = True
palabraOrdenada (x:xs) 
    | x == ' ' = palabraOrdenada (xs)
    | x /= ' ' && head xs == ' ' = palabraOrdenada (x:tail xs)
    | x <= head xs = palabraOrdenada (xs)
    | otherwise = False

{-EJ 4-}
--Debe haber misma cantidad de apariciones en ambos Strings de todos los elementos no blancos. Además, no deben ser iguales
--" abcccc" "cc a b cc" true, "bcbc" "c c c b" false

similAnagrama :: String -> String -> Bool
similAnagrama l1 l2 = mismaCantidadDeNoBlancos l1 l1 l2 && mismaCantidadDeNoBlancos l2 l1 l2 && l1 /= l2

-- El primer parametro indica que caracteres resta chequear. Los otros dos param son los strings originales
mismaCantidadDeNoBlancos :: String -> String -> String -> Bool
mismaCantidadDeNoBlancos [] _ _ = True
mismaCantidadDeNoBlancos (x:xs) l1 l2 
    | x == ' ' = mismaCantidadDeNoBlancos xs l1 l2 
    | x /= ' '  && mismaCantidad = mismaCantidadDeNoBlancos xs l1 l2  -- o directamente otherwise = mismaCantidad && mismaCantidadDeNoBlancos xs l1 l2 
    | otherwise = False
        where mismaCantidad = cantAp x l1 == cantAp x l2 --si esto es false directamente la res es false

cantAp :: Char -> String -> Int
cantAp _ [] = 0
cantAp e (x:xs)
    | e == x = 1 + cantAp e (xs)
    | otherwise = cantAp e (xs)


---------------------------------------------------------------------------------------------------------------------
{-PARIAL TEMA TARDE CUATRI 2C 2024-}

{-EJ 1, esto es re poco eficiente pero bueno funciona¿?-}

maxMovilN :: [Integer] -> Integer -> Integer
maxMovilN (x:xs) 1 = ultimo xs
maxMovilN (x:xs) n 
    | longitud (x:xs) == n = maximo (x:xs)
    | otherwise = maximo (maxMovilAux (x:xs) n)

maxMovilAux :: [Integer] -> Integer -> [Integer]
maxMovilAux (x:xs) 1 = (x:xs)
maxMovilAux (x:xs) n = maxMovilAux (xs) (n-1)

maximo :: [Integer] -> Integer
maximo (x:[]) = x
maximo (x:xs) 
    | x < head xs = maximo (xs)
    | otherwise = maximo (x:tail xs)

ultimo :: [Integer] -> Integer
ultimo (x:[]) = x
ultimo (x:xs) = ultimo (xs)

longitud :: [Integer] -> Integer
longitud (x:[]) = 1
longitud (x:xs) = 1 + longitud (xs)

{-EJ 2-}

promedioPrimo :: Integer -> Float
promedioPrimo n = promedio (factorizacion 2 n)

factorizacion :: Integer -> Integer -> [Integer]
factorizacion i n
    | n == 1 = []
    | mod n i == 0 = i : factorizacion (i) (div n i)
    | mod n i /= 0 = factorizacion (i + 1) (n)

promedio :: [Integer] -> Float
promedio n = fromIntegral (sumaFactores (n)) / fromIntegral (longitud n)

sumaFactores :: [Integer] -> Integer
sumaFactores (x:[]) = x
sumaFactores (x:xs) = x + sumaFactores xs

{-EJ 3-}

letrasIguales :: String -> Integer
letrasIguales (l:[]) = 0
letrasIguales (l:ls) = letrasIgualesAux (l:ls) (l:ls)

letrasIgualesAux :: String -> String -> Integer
letrasIgualesAux _ [] = 0
letrasIgualesAux [] _ = 0
letrasIgualesAux (p:ps) l
    | cantApa p l > 1 = 1 + letrasIgualesAux (ps) (sacarLetra p l)
    | otherwise = letrasIgualesAux (ps) (sacarLetra p l)

cantApa :: Char -> String -> Integer
cantApa x [] = 0
cantApa x (y:ys) 
    | x == ' ' = 0
    | x == y = 1 + cantApa x ys
    | x /= y = cantApa x ys

sacarLetra :: Char -> String -> String
sacarLetra x [] = []
sacarLetra x (y:ys)
    | x == y = sacarLetra x ys
    | x /= y = y : sacarLetra x ys

{-EJ 3-}

