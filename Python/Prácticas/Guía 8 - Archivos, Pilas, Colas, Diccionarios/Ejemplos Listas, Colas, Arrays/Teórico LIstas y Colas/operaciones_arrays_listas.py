# Importar módulo array
import array

# Declarar lista con valores numéricos
lista1 = [1, 0, 1, 0, 1, 1, 0, 0]

# Declarar 'array1' de tipo 'char sin signo' con datos de 'lista1'
array1 = array.array('B', lista1)

print("Buffer info: " + str(array1.buffer_info()))
print("Buffer info: " + str(lista1.buffer_info()))



