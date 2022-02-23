def boasvindas(nome = 'Sem Nome', produto = "Produtos", quantidade=0):
    print(f'Bem vindo {nome}')
    print(f'Temos {quantidade} {produto} em estoque ')


boasvindas('Tassio', 'Cama')
print()
boasvindas('Marcos', 'Mesa', 10)
print()
boasvindas()