# Calculo de  IMC - Indice de massa corporal

"""
Qual e sua altura em cm
qual e o seu peso em kg
"""
# MENOR QUE 18,5     MAGREZA
# ENTRE 18,5 E 24,9  NORMAL
# 25,0 E 29,9        SOBREPESO
# ENTRE  30,0 E 39,9 OBESIDADE
# MAIOR QUE 40,0     OBESIDADE GRAVE

from calcula_imc import Imc

try:
    peso = input('Digite seu peso: ')
    altura = input("Digite sua altura: ")
    peso = float(peso)
    altura = float(altura)
    pessoa = Imc(peso, altura)
except:
    pass
else:
    pessoa.resultado(pessoa.cal_imc())
