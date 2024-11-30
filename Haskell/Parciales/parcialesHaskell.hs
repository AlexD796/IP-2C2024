{-- PARCIAL MATERIAS--}
--EJ 1
aproboMasDenMaterias :: [(String,[Int])] -> String -> Int -> Bool
aproboMasDenMaterias [] _ _ = False
aproboMasDenMaterias ((nombre,notas):registros) alumno i
    | (alumno == nombre) && (finalesAprobados notas) > i = True
    | (alumno == nombre) && (finalesAprobados notas) < i = False
    | otherwise = aproboMasDenMaterias registros alumno i

finalesAprobados :: [Int] -> Int
finalesAprobados [] = 0
finalesAprobados (x:xs)
    | x >= 4 = 1 + finalesAprobados xs
    | otherwise = 0 + finalesAprobados xs 

--EJ 2
buenosAlumnos :: [(String,[Int])] -> [String]
buenosAlumnos [(nombre,notas)]
    | aplazos notas == True = []
    | promedioNotas notas < 8.000 = []
    | (promedioNotas notas >= 8.000) && (aplazos notas == False) = [nombre] 
buenosAlumnos ((nombre,notas):registros)
    | aplazos notas == True = buenosAlumnos registros
    | promedioNotas notas < 8.000 = buenosAlumnos registros
    | (promedioNotas notas >= 8.000) && (aplazos notas == False) = nombre : buenosAlumnos registros

promedioNotas :: [Int] -> Float
promedioNotas lista = dividir (sumatoria lista) (longitud lista)

sumatoria :: [Int] -> Int
sumatoria [] = 0
sumatoria lista = head lista + sumatoria (tail lista)

longitud :: [Int] -> Int
longitud [] = 0
longitud lista = 1 + longitud (tail lista)

dividir :: Int -> Int -> Float
dividir a b = fromIntegral a / fromIntegral b

aplazos :: [Int] -> Bool
aplazos [] = False
aplazos (x:xs) 
    | x >= 4 = aplazos xs
    | x < 4 = True

--EJ 3
mejorPromedio :: [(String,[Int])] -> String
mejorPromedio ((nom1,not1):(nom2,not2):[])
    | promedioNotas not1 >= promedioNotas not2 = nom1
    | promedioNotas not1 <= promedioNotas not2 = nom2
mejorPromedio ((nom1,not1):(nom2,not2):registros)
    | promedioNotas not1 >= promedioNotas not2 = mejorPromedio ((nom1,not1):registros)
    | promedioNotas not1 <= promedioNotas not2 = mejorPromedio ((nom2,not2):registros)


--EJ 4
seGraduoConHonores :: [(String,[Int])] -> Int -> String -> Bool
seGraduoConHonores registros cMaterias nEsp 
    | aproboMasDenMaterias registros nEsp (cMaterias-1) == False = False
    | pertenece nEsp (buenosAlumnos registros) == False = False
    | (promedioNotasAux registros nEsp) - (promedioNotasAux (registros) (mejorPromedio registros)) >= 1 = False
    | otherwise = True

promedioNotasAux :: [(String,[Int])] -> String -> Float
promedioNotasAux ((nom1,not1):registros) nEsp 
    | nom1 == nEsp = promedioNotas not1 
    | otherwise = promedioNotasAux registros nEsp

--diferenciaPromedios :: Float -> Float -> Float
--diferenciaPromedios a b = a - b 

pertenece :: String -> [String] -> Bool
pertenece _ [] = False
pertenece e (x:xs) 
    | e == x = True
    | otherwise = pertenece e xs 

{-- PARCIAL FUTBOL--}

--EJ 1 
atajaronSuplentes :: [(String, String)] -> [Int] -> Int -> Int
atajaronSuplentes listaEq golesEsp totalGoles = totalGoles - sumatoria (golesEsp)

--sumatoria :: [Int] -> Int
--sumatoria [] = 0
--sumatoria (x:xs) = x + sumatoria xs

--EJ 2
equiposValidos :: [(String, String)] -> Bool
equiposValidos [] = True
equiposValidos ((eq,arq):eqs)
    | eq == arq = False
    | (hayRepeticion eq eqs == True) || (hayRepeticion arq eqs == True) = False
    | (hayRepeticion eq eqs == False) && (hayRepeticion arq eqs == False) = equiposValidos eqs

hayRepeticion :: String -> [(String, String)] -> Bool
hayRepeticion a [] = False
hayRepeticion a ((x,y):xys)
    | (a == x || a == y) = True
    | otherwise = hayRepeticion a xys

--EJ 3
porcentajeDeGoles :: String -> [(String, String)] -> [Int] -> Float
porcentajeDeGoles a ((x,y):xys) golesEsp
    | (a == y) = dividir (head golesEsp) (sumatoria golesEsp)
    | otherwise = dividir (encontarGoles a xys (tail golesEsp)) (sumatoria golesEsp)

encontarGoles:: String -> [(String, String)] -> [Int] -> Int
encontarGoles a ((x,y):xys) (i:is)
    | a == y = i 
    | otherwise = encontarGoles a xys is

-- dividir :: Int -> Int -> Float
-- dividir a b = fromIntegral a / fromIntegral b

--EJ 4
vallaMenosVencida :: [(String, String)] -> [Int] -> String
vallaMenosVencida arq goles = sacarNombre (duplaMenosGoles arq goles)
    where sacarNombre (x,y) = x

duplaMenosGoles :: [(String,String)] -> [Int] -> (String,Int)
duplaMenosGoles ((x,y):[]) (i:[]) = (y,i)
duplaMenosGoles ((x,y):xys) (i:is)
    | i <= head is = duplaMenosGoles ((x,y):tail xys) (i:tail is)
    | i > head is = duplaMenosGoles xys is


---------------------------------------------------------------------------------------------------------------------
{-- PARCIAL MATERIAS AGAIN--}

--EJERCICIO 1--

aproboMasDeNMaterias :: [(String, [Integer])] -> String -> Integer -> Bool
aproboMasDeNMaterias [] _ _ = False
aproboMasDeNMaterias (x:xs) nombre i
    | fst x == nombre && fijarseNotas (x) >= i = True
    | fst x == nombre && fijarseNotas (x) < i = False
    | otherwise = aproboMasDeNMaterias xs nombre i

fijarseNotas :: (String, [Integer]) -> Integer
fijarseNotas (nombre, []) = 0
fijarseNotas (nombre,(n1:ns)) 
    | n1 >= 4 = 1 + fijarseNotas (nombre,ns)
    | n1 < 4 = fijarseNotas (nombre,ns)

--EJERCICIO 2--

buenosAlumnos_bis :: [(String, [Integer])] -> [String]
buenosAlumnos_bis [] = []
buenosAlumnos_bis (x:xs)
    | promedio (x) >= 8.00 && aplazos_bis (x) == False = fst (x) : buenosAlumnos_bis (xs)
    | otherwise = buenosAlumnos_bis (xs)

aplazos_bis :: (String, [Integer]) -> Bool
aplazos_bis (nombre,[]) = False
aplazos_bis (nombre, (n:ns))
    | n >= 4 = aplazos_bis (nombre,ns)
    | otherwise = True

promedio :: (String, [Integer]) -> Float
promedio (nombre, notas) = (fromIntegral(suma_total (notas)) / fromIntegral(longitud_bis (notas)))

suma_total :: [Integer] -> Integer
suma_total [] = 0
suma_total (x:xs) = x + suma_total xs

longitud_bis :: [Integer] -> Integer
longitud_bis [] = 0
longitud_bis (x:xs) = 1 + longitud_bis (xs)

--EJERCICIO 3--

mejorPromedio_bis :: [(String, [Integer])] -> String
mejorPromedio_bis (x:[]) = fst x
mejorPromedio_bis (x:xs)
    | promedio (x) < promedio (head (xs)) = mejorPromedio_bis (xs)
    | otherwise = mejorPromedio_bis (x:tail xs)

--EJERCICIO 4--

--[("a", [8,8,8,8]),("b",[10,9,8,9]),("c", [10,10,10,3,10]),("d",[10,9,8,9,10])] "d" 5
-- aprobo mas de 4 materias && es un buen alumno && promedio < del mejor promedio (él) --> true

--[("a", [8,8,8,8]),("b",[10,9,8,9]),("c", [10,10,10,3,10]),("d",[10,9,8,9,10])] "d" 7
-- No aprobo 6 materias -> false

--[("a", [8,8,8,8]),("b",[10,9,8,9]),("c", [10,10,10,3,10]),("d",[10,9,8,9,10])] "a" 3
-- materias yes && buen alumno && ESTA A 1 ESTRICTO DE D -> False


--[("a", [8,8,8,8]),("b",[10,9,8,9]),("c", [10,10,10,3,10]),("d",[10,9,8,9,10])] "c" 3
-- materias yes && NOOOO buen alumno && ESTA A menos de 1 ESTRICTO DE D -> false

seGraduoConHonores_bis :: [(String, [Integer])] -> Integer -> String -> Bool
seGraduoConHonores_bis (r:rs) i n =(aproboMasDeNMaterias (r:rs) (n) (i-1)) && pertenece_bis (buenosAlumnos_bis (r:rs)) (n) && ((auxiliar (r:rs) - promedio (r)) < 1) 

auxiliar :: [(String, [Integer])] -> Float --lo mismo q mejor promedio pero me devuelve el promedio al final en vez del nombre
auxiliar (x:[]) = promedio x
auxiliar (x:xs)
    | promedio (x) < promedio (head (xs)) = auxiliar (xs)
    | otherwise = auxiliar (x:tail xs)

pertenece_bis :: [String] -> String -> Bool
pertenece_bis [] i = False
pertenece_bis (x:xs) i 
    | x == i = True
    | otherwise = pertenece_bis xs i

---------------------------------------------------------------------------------------------------------------------
{-- RECUPERATORIO SOPA DE LETRAS AGAIN--}

--EJERCICIO 1--

type Fila = [Integer]
type Tablero = [Fila]
type Posicion = (Integer,Integer)
type Camino = [Posicion]

maximo :: Tablero -> Integer
maximo (x:[]) = maximoAux (x)
maximo (x:xs)
    | maximoAux x < maximoAux (head xs) = maximo (xs)
    | otherwise = maximo (x:tail xs)

maximoAux :: Fila -> Integer
maximoAux (x:[]) = x
maximoAux (x:xs)
    | x < head xs = maximoAux xs
    | otherwise = maximoAux (x:tail xs)

--EJERCICIO 2--

masRepetido :: Tablero -> Integer
masRepetido l = masRepetidoAux (concatenar (l)) l

masRepetidoAux :: Fila -> Tablero -> Integer
masRepetidoAux (x:[]) l = x
masRepetidoAux (x:xs) l
    | cantAp (x) l < cantAp (head xs) l = masRepetidoAux (xs) l
    | otherwise = masRepetidoAux (x:tail xs) l

concatenar :: Tablero -> Fila
concatenar (x:[]) = x
concatenar (x:xs) = x ++ concatenar xs

cantAp :: Integer -> Tablero -> Integer
cantAp i [] = 0
cantAp (i) (x:xs) = cantApAux i x + cantAp i xs

cantApAux :: Integer -> Fila -> Integer
cantApAux i [] = 0
cantApAux i (x:xs)
    | i == x = 1 + cantApAux i xs
    | otherwise = cantApAux i xs 

--EJERCICIO 3--

valoresDecamino :: Tablero -> Camino -> Fila
valoresDecamino tablero [] = []
valoresDecamino tablero ((f,c):ps) = buscarNumero tablero (f,c) : valoresDecamino (tablero) (ps)

buscarNumero:: Tablero -> Posicion -> Integer
buscarNumero tablero (f,c) = enesimoDigito (encontrarFila tablero f) c

enesimoDigito :: (Num t, Eq t) => [t] -> t -> t --es la misma funcion pero como son diferentes signaturas no me deja usarla jjj
enesimoDigito (x:xs) 1 = x
enesimoDigito (x:xs) i = enesimoDigito xs (i-1)

encontrarFila :: Tablero -> Integer -> Fila
encontrarFila (x:xs) 1 = x
encontrarFila (x:xs) i = encontrarFila xs (i-1)

--EJERCICIO 4--

esCaminoFibo :: Fila -> Integer -> Bool
esCaminoFibo (x:xs) i
    | x /= i = False
    | x == i = esCaminoFiboAux (x:xs) 0

esCaminoFiboAux :: Fila -> Integer -> Bool
esCaminoFiboAux [] _ = True
esCaminoFiboAux (x:xs) i
    | f(i) == x = esCaminoFiboAux (xs) (i+1)
    | f(i) /= x && i > x = False
    | otherwise = esCaminoFiboAux (x:xs) (i+1)

f :: Integer -> Integer
f(0) = 0
f(1) = 1
f (n) = f (n-1) + f (n-2)

---------------------------------------------------------------------------------------------------------------------
{-- PARCIAL DEMOCRACIA--}

--EJERCICIO 1--
division :: Integer -> Integer -> Float
division a b = (fromIntegral a) / (fromIntegral b)

porcentajeDeVotosAfirmativos :: [(String,String)] -> [Integer] -> Integer -> Float
porcentajeDeVotosAfirmativos formulas votos i = division (sumaTotal (votos)) i

sumaTotal :: [Integer] -> Integer
sumaTotal [] = 0
sumaTotal (x:xs) = x + sumaTotal xs

--EJERCICIO 2--

formulasInvalidas :: [(String,String)] -> Bool
formulasInvalidas [] = False
formulasInvalidas l = formulasInvalidasAux l l

formulasInvalidasAux :: [(String,String)] -> [(String,String)] -> Bool
formulasInvalidasAux [] _ = False
formulasInvalidasAux (x:xs) (y:ys) 
    | cantApariciones (fst x) (y:ys) > 1 || cantApariciones (snd x) (y:ys) > 1 = True
    | otherwise = formulasInvalidasAux xs (y:ys)

cantApariciones :: String -> [(String,String)] -> Integer
cantApariciones i [] = 0
cantApariciones i (x:xs)
    | i == fst x && i == snd x = 2 + cantApariciones i xs
    | i == fst x || i == snd x = 1 + cantApariciones i xs
    | otherwise = cantApariciones i xs

--EJERCICIO 3--

porcentajeDeVotos :: String -> [(String,String)] -> [Integer] -> Float
porcentajeDeVotos i (x:xs) votos = division (votosEspecificos i (x:xs) votos) (sumaTotal (votos))
   
votosEspecificos :: String -> [(String,String)] -> [Integer] -> Integer
votosEspecificos i (x:[]) (v:[]) = v
votosEspecificos i (x:xs) (v:vs) 
    | i == snd x = v
    | otherwise = votosEspecificos i xs vs

--EJERCICIO 4--

menosVotado :: [(String,String)] -> [Integer] -> String
menosVotado [] [] = []
menosVotado formulas votos = menosVotadoAux formulas votos (minimo votos)

menosVotadoAux :: [(String,String)] -> [Integer] -> Integer -> String
menosVotadoAux (x:[]) (v:[]) i = fst x
menosVotadoAux (x:xs) (v:vs) i 
    | i == v = fst x
    | otherwise = menosVotadoAux xs vs i

minimo :: [Integer] -> Integer
minimo (v:[]) = v
minimo (v:vs) 
    | v > head vs = minimo (vs)
    | otherwise = minimo (v:tail vs)

--o directamente....................--
menosVotado_bis :: [(String,String)] -> [Integer] -> String
menosVotado_bis [] [] = []
menosVotado_bis (x:[]) (v:[]) = fst x
menosVotado_bis (x:xs) (v:vs)
    | v > head vs = menosVotado_bis (xs) (vs)
    | otherwise = menosVotado_bis (x:tail xs) (v:tail vs)