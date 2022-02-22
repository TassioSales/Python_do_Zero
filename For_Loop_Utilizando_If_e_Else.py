'''for i in range(0, 100):
    if i % 2 == 0:
        print(f"{i} - PAR")
    else:
        print(f"{i} - IMPAR")'''

compra_confirmada = True
dados_compra = "Compra no valor de R$ 12,50 e entrega confirmada"
for i in range(3):
    if compra_confirmada:
        print(dados_compra)
        print("Detalhes enviados para seu email")
        break
else:
    print("Compra nao confirmada")
