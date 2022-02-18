# Criar uma frase adicionar strigs no final
# O Tássio Tem 32 anos de idade e mara em Brasili:

nome = "Tássio"
idade = 32
cidade = "Brasilia"

print(f'O {nome} tem {idade} anos e mora em {cidade}')
print('O ' + nome + ' tem ' + str(idade) + ' anos e mora em ' + cidade)
print('O {} tem {} anos e mora em {}'.format(nome, idade, cidade))