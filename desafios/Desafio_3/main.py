"""
criar um programa que gera 3 listas de acordo com a necessidade abaixo
lista1 = Funcionario que tem carro e trabalham a noite
lista2 = Funcionario que tem carro e trabalham durante o dia
lista3 = Funcionario que nao tem carro.
"""

funcionarios = ['Ana', 'Marcos', "Alice", 'Pedro', 'Sophia', 'Bruno', "Melissa"]
turno_dia = ['Ana', 'Marcos', "Alice", "Melissa"]
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = {"Marcos", 'Alice', "Bruno", 'Melissa'}

#Lista1

Lista1 = set(tem_carro.intersection(turno_noite))
print(Lista1)

Lista2 = set(tem_carro.intersection(turno_dia))
print(Lista2)

Lista3 = set(funcionarios).difference(tem_carro)
print(Lista3)