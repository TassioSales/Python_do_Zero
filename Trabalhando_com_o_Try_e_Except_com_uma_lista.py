try:
    letras = ['a', 'b', 'c', 'd']
    print(letras[4])
except IndexError as I:
    print(I.__class__)
    print("O index que voce esta pedindo não existe")
