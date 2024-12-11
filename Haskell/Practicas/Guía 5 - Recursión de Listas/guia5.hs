-----------------EJ 1------------------------
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

-----------------EJ 2------------------------
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
eliminarRepetidos [x] = [x]
eliminarRepetidos (x:xs)
    | pertenece x xs = eliminarRepetidos ((quitarTodos x xs)++[x])
    | otherwise = x : eliminarRepetidos xs

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

-----------------EJ 3------------------------
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

-----------------EJ 4------------------------
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos (x:xs) 
    | x == head xs && x == ' ' = sacarBlancosRepetidos (xs)
    | otherwise = x : sacarBlancosRepetidos (xs)

contarPalabras :: [Char] -> Integer
contarPalabras s = contarPalabrasAux (sacarBlancosRepetidos (s))

contarPalabrasAux :: [Char] -> Integer
contarPalabrasAux [] = 1
contarPalabrasAux (x:xs)
    | x == ' ' = 1 + contarPalabrasAux xs
    | otherwise = contarPalabrasAux xs

palabras :: [Char] -> [[Char]]
palabras s = palabrasAux (listaSinEspacios (s)) -- si no hago esto la primera palabra si empiexa con "" lo toma como palabra

palabrasAux :: [Char] -> [[Char]]
palabrasAux [] = []
palabrasAux s = [(primeraP s)] ++ palabras (sacarPrimeraP (s))

listaSinEspacios :: [Char] -> [Char]
listaSinEspacios s = quitarEspaciosAdelante (quitarEspaciosAtras (sacarBlancosRepetidos s))

quitarEspaciosAdelante :: [Char] -> [Char]
quitarEspaciosAdelante [] = []
quitarEspaciosAdelante (x:xs)
    | x == ' ' = quitarEspaciosAdelante xs
    | otherwise = (x:xs)

quitarEspaciosAtras :: [Char] -> [Char]
quitarEspaciosAtras [] = []
quitarEspaciosAtras (x:[]) -- necesario sino se rompe en " " etc
    | x == ' '  = [] 
    | otherwise = [x]
quitarEspaciosAtras (x:xs)
    | ultimo (x:xs) == ' ' = quitarEspaciosAtras (x:principio xs) --no se por qué si pones ultimo xs en vez de ultimo (x:xs) se indefine
    | otherwise = (x:xs)

primeraP :: [Char] -> [Char]
primeraP [] = []
primeraP (x:xs)
    | x /= ' ' = x : primeraP xs
    | otherwise = []

sacarPrimeraP :: [Char] -> [Char]
sacarPrimeraP [] = []
sacarPrimeraP (x:xs) 
    | x /= ' ' = sacarPrimeraP xs
    | otherwise = xs

palabraMasLarga :: [Char] -> [Char]
palabraMasLarga s = palabraMasLargaAux (listaSinEspacios s)

palabraMasLargaAux :: [Char] -> [Char]
palabraMasLargaAux s 
    | sacarPrimeraP s == [] = primeraP s --si hay una sola palabra es porque descarto todas las otras mas grandes y la primeraP es efectivamente la mas grande
    | longitud (primeraP xs) > longitud (palabraMasLargaAuxiliar(sacarPrimeraP s)) = primeraP s --si esto se cumple la primera palabra era la mas grande
    | otherwise = palabraMasLargaAuxiliar (sacarPrimeraP s) --sino saca la primera palabra y sigue recursionando

palabraMasLargaAuxiliar :: [Char] -> [Char]
palabraMasLargaAuxiliar xs 
    | sacarPrimeraPalabra xs == [] = primeraPalabra xs
    | longitud (primeraPalabra xs) > longitud (palabraMasLargaAuxiliar(sacarPrimeraPalabra xs)) = primeraPalabra xs --cuando me encuentra la palabra mas larga me corta la recursion
    | otherwise = palabraMasLargaAuxiliar (sacarPrimeraPalabra xs) --sigue recursion buscando palabra mas grande

palabraMasLarga :: [Char] -> [Char]
palabraMasLarga xs = palabraMasLargaAuxiliar (listaSinEspaciosReal xs)

-----------------EJ 5------------------------
sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada [] = []
sumaAcumulada [s] = [s]
sumaAcumulada (s) = sumaAcumulada (todoMenosUltimo (s)) ++ [sumaTotal (s)]

sumaTotal :: (Num t) => [t] -> t
sumaTotal (x:[]) = x
sumaTotal (x:xs) = x + sumaTotal xs

todoMenosUltimo :: (Num t) => [t] -> [t]
todoMenosUltimo [] = []
todoMenosUltimo (x:[]) = []
todoMenosUltimo (x:xs) = x : todoMenosUltimo xs

descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x:xs) = [descomponerEnPrimosDesde 2 x] ++ descomponerEnPrimos xs

descomponerEnPrimosDesde :: Integer -> Integer -> [Integer]
descomponerEnPrimosDesde e 1 = []
descomponerEnPrimosDesde e n 
    | mod n e == 0 = e : descomponerEnPrimosDesde e (div n e)
    | otherwise = descomponerEnPrimosDesde (e+1) n

-----------------EJ 6------------------------
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

-----------------EJ 7------------------------
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