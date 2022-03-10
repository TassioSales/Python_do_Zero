"""
Criar um programa que dependendo do temperatura (em celcius do steak) ele retorna o ponto de cozimento em portugues.
o usuario devera fornecer a temperatura:

Temperaturas - Cozimento
120º F ou 48º C - Rare(Selada)
130º F ou 54º C - Mediun rare (Ao ponto para mal passada)
140º F ou 60º C - Mediun (Ao ponto)
150º F ou 65º C - Mediun well (Ao ponto para o bem passada)
160º F ou 71º C - Well done (Bem passada)
"""


class temp_da_carne:
    def __init__(self, temperatura):
        self.temperatura = temperatura

    def analisa_ponto(self):

        if self.temperatura < 48:
            return 'Sua carne esta: Rare (Selada)'

        elif 48 < self.temperatura < 54:
            return 'Mediun rare (Ao ponto para mal passada)'

        elif 54 < self.temperatura <= 60:
            return 'Mediun (Ao ponto)'

        elif 60 < self.temperatura <= 65:
            return 'Mediun well (Ao ponto para o bem passada'

        elif 65 < self.temperatura <= 71:
            return 'Well done (Bem passada)'
        else:
            return 'Carne passou do ponto desejado'
