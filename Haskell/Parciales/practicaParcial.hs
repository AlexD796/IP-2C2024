{-- GUIA REPASO PARCIAL PROBLEMA SISTEMA DE STOCK--}

{--EJ 1--}

generarStock :: [String] -> [(String, Int)]
generarStock [] = []
generarStock (x:xs)  = (x, contarStockEspecifico x (x:xs)): generarStock (quitarTodos x xs)

contarStockEspecifico :: String -> [String] -> Int
contarStockEspecifico l [] = 0
contarStockEspecifico producto (l:ls)
    | producto == l = 1 + contarStockEspecifico producto ls
    | otherwise = 0 + contarStockEspecifico producto ls

quitarTodos:: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos e (x:xs) | e == x = quitarTodos e xs
                     | otherwise = x : quitarTodos e xs

{--EJ 2--}

stockDeProducto :: [(String, Int)] -> String -> Int
stockDeProducto ((prod, cantidad): stocks) prodEspecifico
    | prod == prodEspecifico = cantidad
    | prod /= prodEspecifico && pertenece prodEspecifico ((prod, cantidad): stocks) == True = stockDeProducto stocks prodEspecifico 
    | otherwise = 0

pertenece :: String -> [(String, Int)] -> Bool
pertenece _ [] = False
pertenece productoEspecifico ((prod, cantidad): stocks) = productoEspecifico == prod || pertenece productoEspecifico stocks

{--EJ 3--}

dineroEnStock :: [(String, Int)] -> [(String, Float)] -> Float
dineroEnStock [(p1,c)] lp = fromIntegral c *  precioDelProducto lp p1
dineroEnStock ((p1,c):sts) lp = fromIntegral((stockDeProducto ((p1,c):sts) p1)) * (precioDelProducto lp p1) + dineroEnStock sts lp

precioDelProducto :: [(String, Float)] -> String -> Float
precioDelProducto ((p1,pr):prs) pEsp 
    | p1 == pEsp = pr
    | p1 /= pEsp = precioDelProducto prs pEsp

{--EJ 4--}

aplicarOferta :: [(String, Int)] ->[(String, Float)] ->[(String,Float)]
aplicarOferta [st] (p:ps) 
    | snd st > 10 = [(fst st, (precioDelProducto (p:ps) (fst st)* 0.80))]
    | otherwise = [(fst st, (precioDelProducto (p:ps) (fst st)))]
aplicarOferta (st:sts) (p:ps) 
    | snd st > 10 = (fst st, (precioDelProducto (p:ps) (fst st)* 0.80)) :  aplicarOferta sts (p:ps) 
    | otherwise = (fst st, (precioDelProducto (p:ps) (fst st))) : aplicarOferta sts (p:ps) 

{--PROBLEMA PERFECTOS AMIGOS--}

{--EJ 5--}

type Fila = [Int]
type Tablero = [Fila]
type Posicion = (Int, Int)
type Camino = [Posicion]

maximo :: Tablero -> Int
maximo (t1:[]) = maximoFila t1
maximo (t1:t2:ts)
    | maximoFila t1 >= maximoFila t2 = maximo (t1:ts)
    | maximoFila t1 <= maximoFila t2 = maximo (t2:ts)

maximoFila :: Fila -> Int
maximoFila (n:[]) = n
maximoFila (n:ns) 
    | n >= head ns = maximoFila (n:tail ns)
    | n <= head ns = maximoFila (head ns:tail ns)

{--EJ 6--}

masRepetido :: Tablero -> Int
masRepetido t = masRepetidoAux (aplanarTablero t) (aplanarTablero t) 

masRepetidoAux ::  Fila -> Fila -> Int
masRepetidoAux [a] ys = a
masRepetidoAux (a:b:cs) ys
    | apariciones a ys >= apariciones b ys = masRepetidoAux (a:cs) ys
    | otherwise = masRepetidoAux (b:cs) ys

--numeroMasRepetido :: Fila -> Int
--numeroMasRepetido (n:[]) = n
--numeroMasRepetido (n:ns)
 --   | apariciones n (n:ns) >= apariciones (head ns) (n:tail ns) = numeroMasRepetido (n:tail ns)
   -- | apariciones n (n:ns) <= apariciones (head ns) (n:tail ns) = numeroMasRepetido (ns)

aplanarTablero :: Tablero -> Fila
aplanarTablero [] = []
aplanarTablero ([]:t) = aplanarTablero t
aplanarTablero ((x:xs):t) = x : aplanarTablero (xs:t)

apariciones :: Int -> Fila -> Int
apariciones e [] = 0
apariciones e (x:xs)
    | e == x = 1 + apariciones e xs
    | otherwise = 0 + apariciones e xs
 
{--EJ 7--}

valoresDeCamino :: Tablero -> Camino -> [Int]
valoresDeCamino _ [] = []
valoresDeCamino tablero ((x,y):zs) = encontrarNumero tablero [(x,y)] ++ valoresDeCamino tablero zs

encontrarNumero :: Tablero -> Camino -> [Int]
encontrarNumero tablero [(x,y)] = [iesimoDigito y (iesimoDigito x tablero)]

iesimoDigito :: Int -> [t] -> t
iesimoDigito 1 tablero = head tablero
iesimoDigito n tablero = iesimoDigito (n-1) (tail tablero)


{-- encontrarFila :: Posicion -> Tablero -> Fila
encontrarFila (x,y) (f1:f2:fs)
    | (x == 1) || (esPar x == True) = f1
    | (x == 2) || (esPar x == False)= f2
    | otherwise = encontrarFila (x,y) fs
        
encontrarNumeroAux :: Posicion -> Fila -> Int
encontrarNumeroAux (x,y) (n1:n2:ns)
    | esPar y == False = n1
    | esPar y == True = n2
    | otherwise = encontrarNumeroAux (x,y) ns

esPar :: Int -> Bool
esPar x 
    | mod x 2 == 0 = True
    | otherwise= False
--}

{--EJ 8 esta mal !!! pide otra cosa eh--}

esCaminoFibo :: [Int] -> Int -> Bool
esCaminoFibo [] e = True
esCaminoFibo (x:xs) e
    | f (e) == x = esCaminoFibo xs (e+1)
    | otherwise = False


f :: Int -> Int
f(0) = 0
f(1) = 1
f(n) = f(n-1) + f(n-2)


{--PROBLEMA PERFECTOS AMIGOS--}

{--EJ 9--}

divisoresPropios :: Int -> [Int]
divisoresPropios 1 = [1]
divisoresPropios n = divisoresDesde n 1

divisoresDesde :: Int -> Int -> [Int]
divisoresDesde n desde 
    | n == desde = []
    | mod n desde == 0 = desde : divisoresDesde n (desde+1)
    | mod n desde /= 0 = divisoresDesde n (desde+1)

{--EJ 10--}

sonAmigos :: Int -> Int -> Bool
sonAmigos n1 n2 = (sumatoria (divisoresPropios n1) == n2) && (sumatoria (divisoresPropios n2) == n1)

sumatoria :: [Int] -> Int
sumatoria [n] = n
sumatoria (n:ns) = n + sumatoria ns

{--EJ 11--}

--losPrimerosNPerfectos :: Int -> [Int]
--losPrimerosNPerfectos 1 = [6]
--losPrimerosNPerfectos nP 
 --   | (sumatoria (divisoresPropios nP) == nP) = 1 : losPrimerosNPerfectos

losPrimerosNPerfectos :: Int -> [Int]
losPrimerosNPerfectos 1 = [6]
losPrimerosNPerfectos n = losPrimerosNPerfectos (n-1) ++ [proxPerfecto (nEsimoPerfecto (n-1))]

nEsimoPerfecto :: Int -> Int
nEsimoPerfecto 1 = 6
nEsimoPerfecto n = proxPerfecto (nEsimoPerfecto (n-1))
 
proxPerfecto :: Int -> Int
proxPerfecto 1 = 6
proxPerfecto n 
    | esPerfecto (n+1) == True = (n+1)
    | otherwise = proxPerfecto (n+1)

esPerfecto :: Int -> Bool
esPerfecto 1 = False
esPerfecto x 
    | (sumatoria (divisoresPropios x) == x) = True
    | otherwise = False

{--EJ 12--}

listaDeAmigos :: [Int] ->[(Int,Int)]
listaDeAmigos [x] = []
listaDeAmigos (x:xs) = buscarAmigos x xs ++ listaDeAmigos xs

buscarAmigos::Int -> [Int] -> [(Int,Int)]
buscarAmigos a [] = []
buscarAmigos a (x:xs)   
    | a == x = buscarAmigos a xs
    | sonAmigos a x = (a,x): buscarAmigos a xs
    | otherwise = buscarAmigos a xs
