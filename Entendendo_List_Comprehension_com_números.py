valores1 = []
valores2 = []

for x in range(0, 60, 10):
    valores1.append(x)

for x in range(6):
    valores2.append(x * 10)

valores3 = [valor * 10 for valor in range(6)]
valores4 = [valor for valor in range(0, 60, 10)]

print(valores1)
print(valores2)
print(valores3)
print(valores4)
