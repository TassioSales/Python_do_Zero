cores_lista = ['amarelo', 'verde', 'azul', 'vermelho']

cores_tuple = ('amarelo', 'verde', 'azul', 'vermelho')

print(cores_lista)
print(cores_tuple)

print(type(cores_tuple))
print(type(cores_lista))

cores_lista = cores_lista * 2
print(cores_lista)

cores_tuple = cores_tuple * 2
print(cores_tuple)

cores_lista.append("Roxo")
print(cores_lista)

cores_tuple.append('Roxo')
print(cores_tuple)
