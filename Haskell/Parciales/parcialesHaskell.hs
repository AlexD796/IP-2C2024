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

--EJERCICIO 3--

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


