{--ELECCIONES PRESIDENCIALES--}

{-EJ 1-}

votosEnBlanco :: [(String,String)] -> [Int] -> Int -> Int
votosEnBlanco listaCand listaVotos totalVotos = totalVotos - sumatoria listaVotos

sumatoria :: [Int] -> Int
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

{-EJ 2-}

{--formulasValidas :: [(String,String)] -> Bool
formulasValidas [] = False
formulasValidas lc 
    | (hayDuplaComponentesIguales lc == True) = False
    | (hayAlgunaRepeticion lc == True) = False
    | otherwise = True

hayDuplaComponentesIguales :: [(String,String)] -> Bool
hayDuplaComponentesIguales [] = True
hayDuplaComponentesIguales (l:ls)
    | fst l == snd l = True
    | otherwise = hayDuplaComponentesIguales ls

hayAlgunaRepeticionRecursion :: [(String, String)] -> Bool
hayAlgunaRepeticionRecursion [] = True
hayAlgunaRepeticionRecursion [x] = False
hayAlgunaRepeticionRecursion ((x,y):xys)
    | (hayAlgunaRepeticionEspecifica (x,y) xys == True) = True
    | (hayAlgunaRepeticionEspecifica (x,y) xys == False) = False


hayAlgunaRepeticionEspecifica :: (String, String) -> [(String, String)] -> Bool --se fija si la dupla existe en toda la lista en cualquier orden
hayAlgunaRepeticionEspecifica (x,y) [] = False
hayAlgunaRepeticionEspecifica (x,y) (l:ls)
    | (x == fst l || x == snd l) && (y == fst l || y == snd l) = True
    | otherwise = hayAlgunaRepeticionEspecifica (x,y) ls
    --}

{-EJ 2-}

formulasValidas :: [(String,String)] -> Bool
formulasValidas [] = True
formulasValidas ((l1,l2):ls)  
    | l1==l2 = False
    | (perteneceAtupla l1 ls == True) = False
    | (perteneceAtupla l2 ls == True) = False
    | otherwise = formulasValidas ls

perteneceAtupla :: String -> [(String,String)] -> Bool
perteneceAtupla e [] = False
perteneceAtupla e ((a,b):xs)
    | e == a = True
    | e == b = True
    | otherwise = perteneceAtupla e xs

{-EJ 3-}

porcentajeDeVotos :: String -> [(String, String)] -> [Int] -> Float
porcentajeDeVotos presi ((x,y):xs) (c:cs)
    | presi == x = division c (sumatoria (c:cs))
    | otherwise = division (encontrarVotosPresi presi ((x,y):xs) (c:cs)) (sumatoria (c:cs))

encontrarVotosPresi :: String -> [(String, String)] -> [Int] -> Int
encontrarVotosPresi presi ((x,y):xs) (c:cs)
    | presi == x = c
    | otherwise = encontrarVotosPresi presi xs cs

division :: Int -> Int -> Float
division a b = fromIntegral a / fromIntegral b

{-EJ 4-}

proximoPresidente :: [(String, String)] -> [Int] -> String
proximoPresidente ((x,y):xs) (c:cs)
    | c == devolverMayorVoto (c:cs) = x
    | otherwise = proximoPresidente xs cs

devolverMayorVoto :: [Int] -> Int
devolverMayorVoto [a] = a
devolverMayorVoto (a:b:as) 
    | a > b = devolverMayorVoto (a:as) 
    | otherwise = devolverMayorVoto (b:as)
aplanarConEspacios :: [[Char]] -> [Char]
aplanarConEspacios [] = []
aplanarConEspacios (xs:[]) = xs ++ []
aplanarConEspacios (xs:xss) = (xs++" ") ++ aplanarConEspacios xss
