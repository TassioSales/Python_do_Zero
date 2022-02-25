cor = input("Digite a cor desejada: ").capitalize()
cores = ['Amarelo', 'Verde', 'Azul', 'Vermelho']

if cor in cores:
    print(f"Sim temos {cor} em estoque.")
else:
    print(f'Não temos {cor} em estoque."')