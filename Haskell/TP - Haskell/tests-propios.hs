import Test.HUnit
import Data.List
import Solucion

runCatedraTests = runTestTT allTests

allTests = test [
    "vuelosValidos" ~: testsEjvuelosValidos,
    "ciudadesConectadas" ~: testsEjciudadesConectadas,
    "modernizarFlota" ~: testsEjmodernizarFlota,
    "ciudadMasConectada" ~: testsEjciudadMasConectada,
    "sePuedeLlegar" ~: testsEjsePuedeLlegar,
    "duracionDelCaminoMasRapido" ~: testsEjduracionDelCaminoMasRapido,
    "puedoVolverAOrigen" ~: testsEjpuedoVolverAOrigen
    
    ]

testsEjvuelosValidos = test [
    "vuelos válido con un vuelo" ~: vuelosValidos [("BsAs", "Rosario", 5.0)] ~?= True,
    "vuelos válido con 3 vuelos distintos" ~: vuelosValidos [("BsAs","Barcelona",3.0),("Corrientes","Dubai",4.0),("Ezeiza","Formosa",3.0)] ~?= True,
    "vuelos válido con varios vuelos y 1 de duracion 0" ~: vuelosValidos [("BsAs","Barcelona",3.0),("Corrientes","Dubai",4.0),("BsAs","Dubai",0)] ~?= False,
    "vuelos válido con un vuelo de duracion 0" ~: vuelosValidos [("BsAs","Dubai",0)] ~?= False,
    "vuelos válido con vuelos repetidos en lugar 1 y 2" ~: vuelosValidos [("BsAs","Barcelona",3.0),("BsAs","Barcelona",4.0),("Dubai","Formosa",3.0)] ~?= False,
    "vuelos válido con vuelos repetidos en lugar 2 y 3" ~: vuelosValidos [("BsAs","Barcelona",3.0),("Corrientes","Dubai",4.0),("Corrientes","Dubai",3.0)] ~?= False,
    "vuelos válido con vuelos repetidos en lugar 1 y 3" ~: vuelosValidos [("BsAs","Barcelona",3.0),("Corrientes","Dubai",4.0),("BsAs","Barcelona",3.0)] ~?= False,
    "vuelos válido con solamente 2 vuelos repetidos" ~: vuelosValidos [("BsAs", "Rosario", 5.0),("BsAs", "Rosario", 5.0)] ~?= False,
    "vuelos válido con lista vacía" ~: vuelosValidos [] ~?= False

    ]

testsEjciudadesConectadas = test [
    "ciudad conectada con un solo vuelo" ~: ciudadesConectadas [("BsAs", "Rosario", 5.0)] "Rosario" ~?= ["BsAs"],
    "ciudad conectada con 2 conexiones" ~: expectPermutacion (ciudadesConectadas [("BsAs", "Rosario", 5.0), ("Rosario", "La Plata", 4.3)] "Rosario") ["La Plata","BsAs"],
    "ninguna ciudad conectada" ~: ciudadesConectadas [("BsAs", "Rosario", 5.0), ("Rosario", "BsAs", 4), ("La Plata", "BsAs", 4), ("Rosario", "La Plata", 4.3)] "Cordoba" ~?= [],
    "solo 1 ciudad conectada y todo el resto no" ~: ciudadesConectadas [("La Plata", "BsAs", 4), ("BsAs", "Rosario", 5.0), ("Yapeyu", "Antartida", 4), ("Bariloche", "BsAs", 4)] "Rosario" ~?= ["BsAs"],
    "solo 2 ciudades conectada y todo el resto no" ~: expectPermutacion (ciudadesConectadas [("La Plata", "BsAs", 4), ("BsAs", "Rosario", 5.0), ("Rosario", "Antartida", 4), ("Bariloche", "BsAs", 4)] "Rosario") ["Antartida", "BsAs"]

    ]

testsEjmodernizarFlota = test [
    "flota modernizada con un vuelo" ~: expectlistProximity (sacarFloats(modernizarFlota [("BsAs", "Rosario", 10.0)])) [9.0],
    "flota modernizada con 2 vuelos" ~: expectlistProximity (sacarFloats(modernizarFlota [("BsAs", "Rosario", 5.27),("BsAs", "Cordoba", 9.33333)])) [4.743, 8.399997],
    "flota modernizada con 3 vuelos" ~: expectlistProximity (sacarFloats(modernizarFlota [("BsAs", "Cordoba", 9.5), ("BsAs", "Rosario", 2.3), ("La Plata", "Cordoba", 5.1)])) [8.55, 2.07, 4.59]

    ]

testsEjciudadMasConectada = test [
    "ciudad mas conectada con 2 vuelos" ~: ciudadMasConectada [("BsAs", "Rosario", 10.0), ("Rosario", "Córdoba", 7.0)] ~?= "Rosario",
    "ciudad mas conectada con 3 vuelos" ~: ciudadMasConectada [("BsAs", "Rosario", 10.0), ("Rosario", "Córdoba", 7.0),("BsAs", "Rosario", 10.0)] ~?= "Rosario",
    "ciudad mas conectada con 3 vuelos y solo 2 conexiones" ~: ciudadMasConectada [("Antartida", "Bariloche", 10.0), ("BsAs", "Rosario", 10.0), ("Rosario", "Córdoba", 7.0)] ~?= "Rosario",
    "ciudad mas conectada con 3 vuelos y 2 posibilidades" ~: expectAny (ciudadMasConectada [("BsAs", "Rosario", 10.0), ("Yapeyu","Chaco", 5.2), ("Rosario", "BsAs", 7.0)]) ["BsAs", "Rosario"],
    "ciudad mas conectada unico vuelo" ~: expectAny (ciudadMasConectada [("Chaco", "Mendoza", 10.0)]) ["Mendoza", "Chaco"],
    "ciudad mas conectada con 2 vuelos sin conexiones" ~: expectAny (ciudadMasConectada [("BsAs","Rosario", 10.0), ("Chaco", "Mendoza", 10.0)]) ["BsAs", "Rosario", "Mendoza", "Chaco"]

    ]

testsEjsePuedeLlegar = test [
    "se puede llegar caso verdadero con una escala" ~: sePuedeLlegar [("BsAs", "Rosario", 5.0), ("Rosario", "Córdoba", 5.0), ("Córdoba", "BsAs", 8.0)] "BsAs" "Córdoba" ~?= True,
    "se puede llegar caso falso 3 vuelos" ~: sePuedeLlegar [("BsAs", "Rosario", 5.0), ("Rosario", "Cordoba", 5.0), ("BsAs", "Cordoba", 8.0)] "Cordoba" "BsAs" ~?= False,
    "se puede llegar caso falso con varias escalas" ~: sePuedeLlegar [("Antartida", "Rosario", 5.0), ("Rosario", "Córdoba", 5.0), ("Córdoba", "BsAs", 8.0)] "Antartida" "BsAs" ~?= False,
    "se puede llegar caso verdadero con unico vuelo" ~: sePuedeLlegar [("Antartida", "Rosario", 5.0)] "Antartida" "Rosario" ~?= True,
    "se puede llegar caso falso con unico vuelo" ~: sePuedeLlegar [("Antartida", "Rosario", 5.0)] "Yapeyu" "Rosario" ~?= False
    
    ]

testsEjduracionDelCaminoMasRapido = test [
    "duración del camino más rápido con 3 vuelos y una escala" ~: duracionDelCaminoMasRapido [("BsAs", "Rosario", 5.0), ("Rosario", "Córdoba", 5.0), ("Córdoba", "BsAs", 8.0)] "BsAs" "Córdoba" ~?= 10.0,
    "duracion del camino mas rapido con 5 vuelos y 2 posibilidades ambas con 2 escalas" ~: duracionDelCaminoMasRapido [("BsAs", "Rosario", 2.703), ("Rosario", "Cordoba", 1.888), ("Cordoba", "BsAs", 8.0),("BsAs","Antartida", 4.0),("Antartida","Cordoba", 3.0)] "BsAs" "Cordoba" ~?= 4.591,
    "duración del camino más rápido con 4 vuelos y 2 posibilidades con un vuelo directo" ~: duracionDelCaminoMasRapido [("BsAs", "Rosario", 5.0), ("Rosario", "Cordoba", 5.0), ("Cordoba", "BsAs", 8.0),("BsAs","Cordoba",9.0)] "BsAs" "Cordoba" ~?= 9.0,
    "duración del camino más rápido con 5 vuelos y 2 posibilidades misma duracion ambas" ~:  duracionDelCaminoMasRapido [("Cordoba", "BsAs", 8.0), ("Antartida","Cordoba",5.0), ("BsAs", "Rosario", 5.0), ("Rosario", "Cordoba", 5.0),("BsAs","Antartida",5.0)] "BsAs" "Cordoba" ~?= 10.0,
    "duración del camino más rápido con solamente 1 vuelo" ~: duracionDelCaminoMasRapido [("Corrientes", "Rosario", 5.0)] "Corrientes" "Rosario" ~?= 5.0,
    "duración del camino más rápido con 2 vuelos y solo 1 posible" ~: duracionDelCaminoMasRapido [("Corrientes", "Rosario", 5.0), ("Antartida", "BsAs", 8.0)] "Antartida" "BsAs" ~?= 8.0

    ]

testsEjpuedoVolverAOrigen = test [
    "puedo volver a origen caso verdadero con 3 vuelos y una escala" ~: puedoVolverAOrigen [("BsAs", "Rosario", 5.0), ("Rosario", "Córdoba", 5.0), ("Córdoba", "BsAs", 8.0)] "BsAs" ~?= True,
    "puedo volver a origen caso verdadero con 2 vuelos y una escala" ~: puedoVolverAOrigen [("Cordoba", "Yapeyu", 8.0), ("Yapeyu", "Cordoba", 5.0)] "Yapeyu" ~?= True,
    "puedo volver a origen caso falso con 3 vuelos imposible volver" ~: puedoVolverAOrigen [("BsAs", "Rosario", 5.0), ("Rosario", "Cordoba", 5.0), ("La Plata", "BsAs", 8.0)] "BsAs" ~?= False,
    "puedo volver a origen caso verdadero con 4 vuelos y 2 posibilidades 1 valida" ~: puedoVolverAOrigen [("Rosario","La Plata",5.0),("BsAs", "Rosario", 5.0),("Rosario", "Cordoba", 5.0), ("Cordoba", "BsAs", 8.0)]  "BsAs" ~?= True,
    "puedo volver a origen caso verdadero con 4 vuelos y 3 escalas" ~: puedoVolverAOrigen [("Rosario", "Cordoba", 5.0), ("BsAs", "Rosario", 5.0), ("Santiago del Estero", "BsAs", 8.0), ("Cordoba", "Santiago del Estero", 5.0)] "BsAs" ~?= True,
    "puedo volver a origen caso falso con 2 vuelos imposible volver" ~: puedoVolverAOrigen [("Rosario", "Chile", 5.0), ("La Plata", "BsAs", 8.0)] "BsAs" ~?= False,
    "puedo volver a origen caso falso lista de vuelos no contiene ciudad" ~: puedoVolverAOrigen [("Rosario", "Chile", 5.0), ("La Plata", "BsAs", 8.0)] "Chaco" ~?= False

    ]


-- Funciones Extras

sacarFloats :: [(String, String, Float)] -> [Float]
sacarFloats [] = []
sacarFloats ((origen,destino,duracion):vs) = duracion : sacarFloats vs

margenFloat = 0.00001

expectAny :: (Foldable t, Eq a, Show a, Show (t a)) => a -> t a -> Test
expectAny actual expected = elem actual expected ~? ("expected any of: " ++ show expected ++ "\n but got: " ++ show actual)

expectlistProximity:: [Float] -> [Float] -> Test
expectlistProximity actual expected = esParecidoLista actual expected ~? ("expected list: " ++ show expected ++ "\nbut got: " ++ show actual)

esParecidoLista :: [Float] -> [Float] -> Bool
esParecidoLista actual expected = (length actual) == (length expected) && (esParecidoUnaAUno actual expected)

esParecidoUnaAUno :: [Float] -> [Float] -> Bool
esParecidoUnaAUno [] [] = True
esParecidoUnaAUno (x:xs) (y:ys) = (aproximado x y) && (esParecidoUnaAUno xs ys)

aproximado :: Float -> Float -> Bool
aproximado x y = abs (x - y) < margenFloat

expectAnyTuplaAprox :: (Char, Float) -> [(Char, Float)] -> Test
expectAnyTuplaAprox actual expected = elemAproxTupla actual expected ~? ("expected any of: " ++ show expected ++ "\nbut got: " ++ show actual)

elemAproxTupla :: (Char, Float) -> [(Char, Float)] -> Bool
elemAproxTupla _ [] = False
elemAproxTupla (ac,af) ((bc,bf):bs) = sonAprox || (elemAproxTupla (ac,af) bs)
    where sonAprox = (ac == bc) && (aproximado af bf)

expectPermutacion :: (Ord a, Show a) => [a] -> [a] -> Test
expectPermutacion actual expected = esPermutacion actual expected ~? ("expected list: " ++ show expected ++ "\nbut got: " ++ show actual)

esPermutacion :: Ord a => [a] -> [a] -> Bool
esPermutacion a b = (length a == length b) && (sort a == sort b)
