velocidade =float(input("Digite a velocidade: "))

if velocidade > 110:
    print("Voce esta acima da velocidade permitida")
    print('Por favor reduzir')
elif velocidade < 50:
    print("Voce esta abaixo da velocidade permitida")
    print("Por favor dirigir acima de 80km/h")
else:
    print("Esta dentro da velocidade permitida")
    print("Continue assim")