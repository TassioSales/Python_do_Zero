class Funcionario:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

    def imprimeDados(self):
        print(f'Seu nome e {self.nome} {self.sobrenome}')
        print(f'Voce nasceu em {self.data_nascimento}')


usuario1 = Funcionario("Tassio", "Sales", "02/04/1990")
usuario2 = Funcionario("Lucian", "Jesus", "25/05/2002")

usuario1.imprimeDados()
usuario2.imprimeDados()


