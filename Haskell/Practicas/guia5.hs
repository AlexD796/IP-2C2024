longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

ultimo :: [t] -> t
ultimo [x] = x
ultimo (x:xs) = ultimo xs

principio :: [t] -> [t]
principio (x:[]) = []
principio (x:xs) = x : principio xs

intercambiar :: Int -> Int -> [Int]
intercambiar a b = [b,a]

reverso :: [t] -> [t]
reverso [] = []
reverso xs = ultimo xs : reverso (principio xs)

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece e (x:xs) = e == x || pertenece e (xs)

todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales [x] = True
todosIguales (x:xs) = x == head xs && todosIguales xs

todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos [x] = True
todosDistintos (x:xs) 
    | pertenece x xs = False
    | otherwise = todosDistintos xs

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos [x] = False
hayRepetidos (x:xs) 
    | pertenece x xs = True
    | otherwise = hayRepetidos xs

quitar :: (Eq t) => t -> [t] -> [t]
quitar e [] = []
quitar e (x:xs) 
    | e == x = xs
    | otherwise = x : quitar e xs 

quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos e [] = []
quitarTodos e (x:xs) 
    | e == x = quitarTodos e xs
    | otherwise = x : quitarTodos e (xs)

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos [x] = [x]
eliminarRepetidos (x:xs)
    | x == head xs = eliminarRepetidos xs
    |otherwise = x : eliminarRepetidos xs

mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos [] [] = True
mismosElementos as bs = estaContenida as bs && estaContenida bs as

estaContenida :: (Eq y) => [y] -> [y] -> Bool
estaContenida [] [] = True
estaContenida [] bs = True
estaContenida bs [] = False
estaContenida (a:as) bs = pertenece a bs && estaContenida as bs

capicua :: (Eq t) => [t] -> Bool
capicua xs = xs == reverso xs

maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x:y:xs) 
    | x >= y = maximo (x:xs) --descarta el y que sabemos que es menor que el elemento x
    | otherwise = maximo (y:xs) --descarta el x que sabemos que es menor que el elemento y

sumarN :: Integer -> [Integer] -> [Integer]
sumarN 0 xs= xs 
sumarN e [] = []
sumarN e (x:xs) = (e + x) : sumarN e (xs)

sumarElPrimero :: [Integer] -> [Integer] 
sumarElPrimero (x:xs) = (x + x) : sumarN x xs

sumarElUltimo :: [Integer] -> [Integer] 
sumarElUltimo (x:xs) = (x + ultimo xs) : sumarN (ultimo xs) xs

pares :: [Integer] -> [Integer] 
pares [] = []
pares (x:xs) 
    | mod x 2 == 0 = x : pares xs
    | mod x 2 == 1 = pares xs

multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN e [] = []
multiplosDeN e (x:xs) = (e*x) : multiplosDeN e xs


ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar l = ordenar (quitar (maximo l) l) ++ [maximo l]

sacarEspacios :: [Char] -> [Char]
sacarEspacios [] = []
sacarEspacios [x] = [x]
sacarEspacios (x:y:xs) 
    | x == y && x == ' ' = sacarEspacios (y:xs)
    | otherwise = x : sacarEspacios (y:xs)

contarPalabras :: [Char] -> Integer
contarPalabras [] = 0
contarPalabras xs = contarEspacios (listaSinEspaciosReal xs) + 1 

listaSinEspaciosReal :: [Char] -> [Char]
listaSinEspaciosReal xs = (sacarEspaciosAdelante (sacarEspaciosAtras (sacarEspacios xs)))

sacarEspaciosAdelante :: [Char] -> [Char]
sacarEspaciosAdelante [] = []
sacarEspaciosAdelante [x] = [x]
sacarEspaciosAdelante (x:xs) 
    | x == ' ' = sacarEspaciosAdelante xs
    | otherwise = (x: xs)

sacarEspaciosAtras :: [Char] -> [Char]
sacarEspaciosAtras [] = []
sacarEspaciosAtras [x] = [x]
sacarEspaciosAtras (x:xs) 
    | ultimo (x:xs) == ' ' = sacarEspaciosAtras (principio (x:xs))
    | otherwise = (x:xs)

contarEspacios :: [Char] -> Integer
contarEspacios [] = 0
contarEspacios (x:xs) 
    | x == ' ' = 1 + contarEspacios xs
    | otherwise = contarEspacios xs

primeraPalabra :: [Char] -> [Char]
primeraPalabra [] = []
primeraPalabra (x:xs) 
    | x == ' ' = []
    | otherwise = x : primeraPalabra xs

sacarPrimeraPalabra :: [Char] -> [Char]
sacarPrimeraPalabra [] = []
sacarPrimeraPalabra (x:xs)
    | x == ' ' = xs
    | otherwise = sacarPrimeraPalabra xs

palabras :: [Char] -> [[Char]]
palabras [] = []
palabras ps = primeraPalabra ps : palabras (sacarPrimeraPalabra (listaSinEspaciosReal ps))

palabraMasLargaAuxiliar :: [Char] -> [Char]
palabraMasLargaAuxiliar xs 
    | sacarPrimeraPalabra xs == [] = primeraPalabra xs
    | longitud (primeraPalabra xs) > longitud (palabraMasLargaAuxiliar(sacarPrimeraPalabra xs)) = primeraPalabra xs --cuando me encuentra la palabra mas larga me corta la recursion
    | otherwise = palabraMasLargaAuxiliar (sacarPrimeraPalabra xs) --sigue recursion buscando palabra mas grande

palabraMasLarga :: [Char] -> [Char]
palabraMasLarga xs = palabraMasLargaAuxiliar (listaSinEspaciosReal xs)

type Texto = [Char]
type Nombre = Texto
type Telefono = Texto
type Contacto = (Nombre, Telefono)
type ContactosTel = [Contacto]

enLosContactos :: Nombre -> ContactosTel -> Bool
enLosContactos _ [] = False
enLosContactos nombre ((nombreContacto,_): contactos) 
    | nombre == nombreContacto = True
    | otherwise = enLosContactos nombre contactos

agregarContacto :: Contacto -> ContactosTel -> ContactosTel
agregarContacto contacto [] = [contacto]
agregarContacto (nombre,telefono) ((cNombre,cTelefono):contactos) | nombre == cNombre = (nombre,telefono) : contactos
                                                                  | otherwise = (cNombre,cTelefono) : agregarContacto (nombre,telefono) contactos 
    -- como ya existia el contacto, lo reescribe
    -- mediante recursion me fijo esta en lo que queda, de ser asi lo reescribe por el caso base

elNombre :: Contacto -> Nombre
elNombre (nombre, telefono) = nombre

elTelefono :: Contacto -> Nombre
elTelefono (nombre, telefono) = telefono

eliminarContacto :: Nombre -> ContactosTel -> ContactosTel
eliminarContacto _ [] = []
eliminarContacto nombre ((otroNombre, otroTelefono): contactos)
    | nombre == otroNombre = contactos
    | otherwise = (otroNombre, otroTelefono) : eliminarContacto nombre contactos

type Identificacion = Integer
type Ubicacion = Texto
type Estado = (Disponibilidad, Ubicacion)
type Locker = (Identificacion, Estado)
type MapaDeLockers = [Locker]
type Disponibilidad = Bool

existeElLocker :: Identificacion -> MapaDeLockers -> Bool
existeElLocker id [] = False
existeElLocker id ((id2,(disp,ubi)): lockers)
    | id == id2 = True
    | otherwise = existeElLocker id lockers

ubicacionDelLocker :: Identificacion -> MapaDeLockers -> Ubicacion
ubicacionDelLocker id ((id2,(disp,ubi)): lockers)
    | id == id2 = ubi
    | otherwise = ubicacionDelLocker id (lockers)

estaDisponibleElLocker :: Identificacion -> MapaDeLockers -> Bool
estaDisponibleElLocker id ((id2,(disp,ubi)): lockers) 
    | existeElLocker id ((id2,(disp,ubi)): lockers) && disp == True = True
    | existeElLocker id ((id2,(disp,ubi)): lockers) && disp == False = False

ocuparLocker :: Identificacion -> MapaDeLockers -> MapaDeLockers
ocuparLocker id ((id2,(disp,ubi)): lockers) 
    | id == id2 && disp == False = ((id2,(disp,ubi)): lockers) 
    | otherwise = ocuparLocker id (lockers)