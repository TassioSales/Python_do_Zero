# o Marcos silva e um excelente programador


nome = "Marcos"
sobrenome = "Silva"
profissao = "Programador"

texto = " O" + nome +" "+ sobrenome + " e um excelente " + ' [' + profissao + '] '

texto2 = f'O {nome} {sobrenome} e um excelente [{profissao}]'
texto3 = 'O {} {} e um excelente [{}]'.format(nome, sobrenome, profissao)


print(texto)
print(texto2)
print(texto3)