from sys import getsizeof

numeros1 = [x * 10 for x in range(20000000)]
#print(type(numeros1))
#print(numeros1)
print(getsizeof(numeros1))

print("=" * 20)

numeros2 = (x * 10 for x in range(20000000))
#print(type(numeros2))
#print(list(numeros2))
print(getsizeof(numeros2))

