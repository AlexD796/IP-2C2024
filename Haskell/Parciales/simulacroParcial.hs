
{--SIMULACRO PARCIAL RELACIONES--}

{--EJ 1--}

relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = False
relacionesValidas [r1] = True
relacionesValidas (r1:r2:relaciones)     
    | existeDuplasComponentesIguales (r1:r2:relaciones) == True = False
    | recursionExisteDuplaRepetida (r1:r2:relaciones) == True = False
    | otherwise = True

recursionExisteDuplaRepetida :: [(String, String)] -> Bool
recursionExisteDuplaRepetida [] = False
recursionExisteDuplaRepetida [r1] = False
recursionExisteDuplaRepetida (r1:r2:relaciones)
    | existeDuplaRepetida r1 (r2:relaciones) == True = True
    | otherwise = existeDuplaRepetida r2 (r1:relaciones) 

existeDuplasComponentesIguales :: [(String, String)] -> Bool
existeDuplasComponentesIguales [] = False
existeDuplasComponentesIguales ((nom1, nom2):relaciones)
    | nom1 == nom2 = True
    | nom1 /= nom2 = existeDuplasComponentesIguales relaciones

existeDuplaRepetida :: (String, String) -> [(String, String)] -> Bool
existeDuplaRepetida _ [] = False
existeDuplaRepetida r1 (r2:relaciones) 
    | ((fst r1 == fst r2) ||  (fst r1 == snd r2 )) && ((snd r1 == fst r2) || (snd r1 == snd r2))= True
    | otherwise = existeDuplaRepetida r1 relaciones 

{--EJ 2--}

personas :: [(String, String)] -> [String]
personas [] = []
personas [(p1,p2)] = [p1,p2]
personas ps = listaSinRepetidos (recursionDuplasAListaString ps)

recursionDuplasAListaString :: [(String, String)] -> [String]
recursionDuplasAListaString [] = []
recursionDuplasAListaString ((p1,p2):[]) = [p1,p2]
recursionDuplasAListaString (p: personas) = duplaAstring p ++ recursionDuplasAListaString personas
    where duplaAstring (n1, n2) = [n1, n2]

listaSinRepetidos :: [String] -> [String]
listaSinRepetidos [] = []
listaSinRepetidos [x] = [x] 
listaSinRepetidos (x:xs) = x: listaSinRepetidos (quitarTodos x xs)

{-} ya hecho arriba
quitarTodos :: String -> [String] -> [String]
quitarTodos e [] = []
quitarTodas e [x] = [x]
quitarTodos e (x:xs)
    | e == x = quitarTodos e xs
    | otherwise = x: quitarTodos e xs
    --}

{--EJ 3--}

amigosDe :: String -> [(String, String)] -> [String]
amigosDe _ [] = []
amigosDe persona ((r1,r2): relaciones) 
  --  | persona ((persona, r2): []) = r2
    | otherwise = devuelveAmigoDe persona (r1,r2) ++ amigosDe persona relaciones

devuelveAmigoDe :: String -> (String, String) -> [String]
devuelveAmigoDe persona (r1,r2) 
    | persona == r1 = [r2]
    | persona == r2 = [r1]
    | otherwise = []


{--EJ 4--}

{--
muy poco eficiente y ni lo terminé
personaConMasAmigos :: [(String,String)] -> String
personaConMasAmigos (r1:r2:rs) 
    | compararCantidadAmigosUnaDuplaEnLista (fst r1) r1 >= compararCantidadAmigosUnaDuplaEnLista (snd r2) r1 = personaConMasAmigos (fst r1) rs
    | otherwise = personaConMasAmigos (r2:rs)

compararCantidadAmigos :: [(String, String)] -> String

compararCantidadAmigosUnaDuplaEnLista :: String -> [(String, String)] -> Int
compararCantidadAmigosUnaDuplaEnLIsta pEspecifica [] = 0 ??
compararCantidadAmigosUnaDuplaEnLIsta pEspecifica ((p1,p2): personas)
    | cantidadAmigos pEspecifica (p1 ((p1,p2): personas)) >= cantidadAmigos pEspecifica (p2 ((p1,p2): personas)) = cantidadAmigos p1 ((p1,p2): personas)
    | cantidadAmigos pEspecifica (p1 ((p1,p2): personas)) <= cantidadAmigos pEspecifica (p2 ((p1,p2): personas)) = cantidadAmigos p2 ((p1,p2): personas)

cantidadAmigos :: String -> [(String, String)] -> Int
cantidadAmigos pEspecifica ((pEspecifica,p2):[]) = 1
cantidadAmigos pEspecifica ((p2,pEspecifica):[]) = 1
cantidadAmigos pEspecifica ((pEspecifica,p2):[]) = 1
cantidadAmigos pEspecifica ((p2,pEspecifica):[]) = 1
cantidadAmigos pEspecifica ((p1,p2): personas) 
    | cantidadAmigos (amigosDe pESpecifica ((p1,p2): personas))
--}

personaConMasAmigos :: [(String,String)] -> String
personaConMasAmigos relaciones = mayorAmiguero (personas relaciones) relaciones   

mayorAmiguero :: [String] -> [(String,String)] -> String
mayorAmiguero [x] _ = x
mayorAmiguero (x:y:xs) relaciones
    | cantidadDeAmigos x relaciones >= cantidadDeAmigos y relaciones= mayorAmiguero (x:xs) relaciones
    | otherwise = mayorAmiguero (y:xs) relaciones

cantidadDeAmigos :: String -> [(String,String)] -> Integer
cantidadDeAmigos nombre relaciones = longitud (amigosDe nombre relaciones)

longitud :: [String] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs


