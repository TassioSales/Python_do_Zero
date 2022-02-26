from array import array

letras = ['a', 'b', 'c', 'd', 'e']
numero_int = [10, 20, 30, 40]
numeros_float = [1.23, 1.4, 2.1, 2.2, 2.3, 1.]

print(letras)
print(numero_int)
print(numeros_float)
print()

letras = array('u', ['a', 'b', 'c', 'd', 'e'])
numero_int = array('i', [10, 20, 30, 40])
numeros_float = array('f', [1.23, 1.4, 2.1, 2.2, 2.3, 1])
print(letras)
print(numero_int)
print(numeros_float)
