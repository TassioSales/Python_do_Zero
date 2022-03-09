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

from ponto_do_steak import temp_da_carne

while True:
    try:
        temperatura = input("Digite a Temperatura da carne: ")
        temperatura = int(temperatura)
        ponto_da_carne = temp_da_carne(temperatura)
        print(ponto_da_carne.analisa_ponto())
        break
    except ValueError as V:
        print(V.__class__)
        print('Digite apenas nomeros')
        continue
    except Exception as E:
        print(E.__class__)
        print("Erro para ser indentificado")
        continue
