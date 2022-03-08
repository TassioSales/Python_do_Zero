class Funcionario:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

    def imprimeDados(self):
        print(f'Seu nome e {self.nome} {self.sobrenome}')
        print(f'Voce nasceu em {self.data_nascimento}')

    def imprimeNome(self):
        return f'O nome do cliente e {self.nome} {self.sobrenome}'


usuario1 = Funcionario("Tassio", "Sales", "02/04/1990")
usuario2 = Funcionario("Lucian", "Jesus", "25/05/2002")

usuario1.imprimeDados()
usuario2.imprimeDados()

print(usuario1.imprimeNome())
print(usuario2.imprimeNome())
print(Funcionario.imprimeNome(usuario1))
print(Funcionario.imprimeNome(usuario2))