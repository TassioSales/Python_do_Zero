from datetime import datetime


class Funcionario:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.ano = None
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.ano_nascimento = int(data_nascimento[6:])

    def idade_funcionario(self):
        ano_atual = datetime.now().year
        idade = int(ano_atual - self.ano_nascimento)
        return idade

    def imprimeDados(self):
        idade = Funcionario.idade_funcionario(self)
        print(f'Seu nome e {self.nome} {self.sobrenome}')
        print(f'Voce nasceu em {self.data_nascimento}')
        print(f"E tem {idade}")

    def imprimeNome(self):
        return f'O nome do cliente e {self.nome} {self.sobrenome}'


usuario1 = Funcionario("Tassio", "Sales", "02/04/1990")
usuario2 = Funcionario("Lucian", "Jesus", "25/05/2002")

usuario1.imprimeDados()
print()
usuario2.imprimeDados()

print()

print(usuario1.imprimeNome())
print(usuario2.imprimeNome())
print(Funcionario.imprimeNome(usuario1))
print(Funcionario.imprimeNome(usuario2))
