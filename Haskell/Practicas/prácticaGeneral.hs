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

