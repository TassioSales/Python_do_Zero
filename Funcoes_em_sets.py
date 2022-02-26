lista1 = [1, 2, 3, 4, 5, 6, 7]
s1 = {1, 2, 3, 4, 5, 6, 6, 7}
print(s1)
print(type(s1))

s1.add(8)
s1.update([9, 10, 11, 12])
print(s1)

s1.remove(10)
print(s1)

s1.discard(90)
print(s1)