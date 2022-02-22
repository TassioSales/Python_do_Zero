valor = int(input("Digite o valor do seu produto: "))

while valor > 20:
    valor = valor + (valor * 10 / 100)
    print(f'O valor final do seu produto sera de R$ {float(valor)}')
    break
