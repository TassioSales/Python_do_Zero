nome = input("digite seu nome ?")
idade = input("digite sua idade ?")
cidade = input("Onde voce mora ?")

print(f'O {nome} tem {idade} anos e mora em {cidade}')
print('O ' + nome + ' tem ' + str(idade) + ' anos e mora em ' + cidade)
print('O {} tem {} anos e mora em {}'.format(nome, idade, cidade))