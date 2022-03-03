frutas1 = ["abacate", 'banana', 'morango', 'kiwi', 'abacaxi']
frutas2 = []

for fruta in frutas1:
    if "b" in fruta:
        frutas2.append(fruta)

frutas3 = [fruta for fruta in frutas1 if "b" in fruta]

print(frutas2)
print(frutas3)