lista1 = [10, 20, 30, 40, 50]
lista2 = [10, 20, 30, 60, 70]

num1 = set(lista1)
num2 = set(lista2)

print(lista1)
print(num1)

print(lista2)
print(num2)

print(num1 | num2)  # Union
print(num1 - num2)  # Diference
print(num1 ^ num2)  # Symetric Difference
print(num1 & num2)  # and
print(len(num1))
print(len(num2))