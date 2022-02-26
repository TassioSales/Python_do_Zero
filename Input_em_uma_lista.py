frutas = []
while True:
    fruta = input('Digite o nome da fruta: ').capitalize().strip()
    if fruta == 'Sair':
        break
    frutas.append(fruta)

print(frutas)
