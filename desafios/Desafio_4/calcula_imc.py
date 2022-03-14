# MENOR QUE 18,5     MAGREZA
# ENTRE 18,5 E 24,9  NORMAL
# 25,0 E 29,9        SOBREPESO
# ENTRE  30,0 E 39,9 OBESIDADE
# MAIOR QUE 40,0     OBESIDADE GRAVE


class Imc:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura

    def cal_imc(self):
        imc = self.peso / (self.altura * self.altura)
        return imc

    def resultado(self, imc):
        print(f'Seu peso e de {self.peso}')
        print(f'Sua altura e de {self.altura}')
        print(f'Seu IMC: {imc:.2f}')
        if imc < 18.5:
            print('SITUATION: MAGREZA')
        elif 18.5 <= imc <= 24.9:
            print('SITUATION: NORMAL')
        elif 25.0 <= imc <= 29.9:
            print('SITUATION: SOBREPESO')
        elif 30.0 <= imc <= 39.9:
            print('SITUATION: OBESIDADE')
        else:
            print('SITUATION: OBESIDADE GRAVE')
