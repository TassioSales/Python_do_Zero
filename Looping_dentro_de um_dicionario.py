aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovacao': True}

for x in aluno.items():
    print(x[0], ':', x[1])

print()

for keys, values in aluno.items():
    print(keys, ':',  values)
