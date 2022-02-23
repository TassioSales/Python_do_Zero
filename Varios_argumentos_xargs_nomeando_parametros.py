def agencia(**carro):
    return carro


carro1 = agencia(marca='Gol', cor="Branca", motor=1.0, placa='ABCD1234')
carro2 = agencia(marca='Gol', cor="Preto", motor=1.2, placa='ABCD5678')
carro3 = agencia(marca='Gol', cor="Cinza", motor=1.4, placa='ABCD9101')
carro4 = agencia(marca='Gol', cor="Marron", motor=1.6, placa='ABCD1213')

print(carro1)
print(carro2)
print(carro3)
print(carro4)

lista = [carro1, carro2, carro3, carro4]
for i in lista:
    print(i['cor'])


