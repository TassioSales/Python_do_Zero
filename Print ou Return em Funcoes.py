def cliente1(nome):
    print(f'Olá {nome}'),


def cliente2(nome):
    return f'Ola {nome}'


cliente1("Tassio")
print(cliente2('Jose'))

x = cliente1('Venancio')
y = cliente2('Matheus')

print(x)
print(y)
