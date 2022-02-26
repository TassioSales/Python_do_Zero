aluno = {'nome': 'Ana', 'idade': 16, 'Nota_Final': 'A', 'aprovação': True}
print(aluno)

aluno['nome'] = 'Jose'

print(aluno)

aluno.update({'nome':'João', 'Nota_Final':'B'})
print(aluno)

aluno.update({'Endereco': 'Rua dos bobos'})
print(aluno)
print(aluno.get('sobrenome', 'Não existe'))

del aluno['idade']
print(aluno)