"""
    Criar um programa que calcula a quantidade de tinta necessaria para pintar uma parede.
    O usuario devera fornecer as segunintes informações: Rendimento, Largura e altura
    O programa deve mostra a seguinte informação na tela: Vc necessita de X lata de tinta
"""


class Pintar_parede:
    def __init__(self, largura, altura, redimento):
        self.largura = largura
        self.altura = altura
        self.redimento = redimento

    def calculaArea(self):
        area = self.altura * self.largura
        return area

    def calculaQtdTinta(self, area):
        tinta = area / self.redimento
        return tinta
