from calcula_pintura import Pintar_parede
while True:
    try:
        altura = float(input('Digite a altura da sua parede: '))
        largura = float(input("Digite a largura da sua parede: "))
        redimento = float(input('Digite o redimento da sua tinta: '))
        parede = Pintar_parede(largura, altura, redimento)
        area = parede.calculaArea()
        qtd_latas = parede.calculaQtdTinta(area)
    except ValueError as V:
        print(V.__class__)
        print('Valor digitado incorreto')
        continue
    else:
        print(f"Sua parede tem {area} m² e voce ira gasta {qtd_latas} latas de tinta")
        break
