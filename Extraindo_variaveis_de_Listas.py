produtos = ["Arros", "Feijão", 'Laranja', 'banana']

item1 = produtos[0]
item2 = produtos[1]
item3 = produtos[2]
item4 = produtos[3]

print(item1)
print(item2)
print(item3)
print(item4)
print()

item5, item6, item7, item8 = produtos

print(item5)
print(item6)
print(item7)
print(item8)
print()

produtos1 = ["Arros", "Feijão", 'Laranja', 'banana', 1, 2, 3, 4, 5, 6]

item10, item11, item12, *outros = produtos1

print(item10)
print(item11)
print(item12)
print(outros)
