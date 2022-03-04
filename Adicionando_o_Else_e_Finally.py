while True:
    try:
        valor = float(input('digite o valor do seu produto: '))
        print(valor)
    except ValueError as v:
        print(v.__class__)
        print("Digite apenas numeros e não letras")
        continue
    # else:
    #     print("Usuario digitou um valor correto")
    #     resultado = valor * 2
    #     print(resultado)
    #     break
    finally:
        print('Codigo oK')
