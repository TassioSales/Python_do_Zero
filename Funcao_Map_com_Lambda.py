lista1 = [1, 2, 3, 4]

lista2 = map(lambda x: x * 2, lista1)

lista2 = list(lista2)

print(list(lista2))

print(list(map(lambda x: x ** 2, lista1)))

print(list(map(lambda x: x ** 4, lista2)))

