while True:
    try:
        valor = float(input('digite o valor do seu produto: '))
        print(valor)
        break
    except ValueError as v:
        print(v.__class__)
        print("Digite apenas numeros e não letras")
        continue

print('Mais codigo abaixo')