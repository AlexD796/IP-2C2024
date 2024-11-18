{-EJ 1-}

{-EJ 2-}
{-si es PRIMO la cantidad de factores primos de ese número-}

esAtractivo :: Integer -> Bool
esAtractivo 1 = False
esAtractivo n = esPrimo (cantidadDivisoresPrimos n)

cantidadDivisoresPrimos :: Integer -> Integer
cantidadDivisoresPrimos n = contarDivisoresPrimosDesde 2 n 

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

{-
similAnagrama :: String -> String -> Bool
similAnagrama l1 l2 = similAnagramaAux1 l1 l2

similAnagramaAux1 :: String -> String -> String
similAnagramaAux1 l1 l2 = similAnagramaAux ((sacarBlancos (l1)) (sacarBlancos (l2)))

similAnagramaAux :: String -> String -> Bool
similAnagramaAux [] [] = True
similAnagramaAux _ [] = False
similAnagramaAux [] _ = False
similAnagramaAux (x:xs) (y:ys)
    | cantApariciones x (x:xs) == cantApariciones x (y:ys) = similAnagramaAux (quitarTodos x (x:xs)) (quitarTodos x (y:ys)) 
    | otherwise = False

sacarBlancos :: String -> String
sacarBlancos (x:[])
    | x == ' ' = []
    | otherwise = [x]
sacarBlancos (x:xs)
    | x == ' ' = sacarBlancos xs
    | otherwise = x : sacarBlancos xs

cantApariciones :: Char -> String -> Int
cantApariciones _ [] = 0
cantApariciones e (x:xs)
    | e == x = 1 + cantApariciones e (xs)
    | otherwise = cantApariciones e (xs)

quitarTodos :: Char -> String -> String
quitarTodos e [] = []
quitarTodos e (x:xs)
    | e == x = quitarTodos e xs
    | e /= x = x : quitarTodos e xs 
    -}