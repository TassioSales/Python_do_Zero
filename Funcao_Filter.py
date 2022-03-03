valores = [10, 12, 34, 44, 57]

valores2 = [x * 2 for x in range(0, 50)]


def remover20(x):
    return x > 20


var1 = list(map(remover20, valores2))
var2 = list(map(remover20, valores))
var3 = list(filter(remover20, valores2))
var4 = list(filter(remover20, valores))
var5 = list(filter(lambda x: x > 30, valores))
var6 = list(filter(lambda x: x > 50, valores2))

print(var1)
print(var2)
print(var3)
print(var4)
print(var5)
print(var6)
