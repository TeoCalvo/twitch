# Criar uma sequencia de 1 até 100 e armazenar em uma lista

minha_lista = [1,2,3,4,5,6,7,8] # maneira luzitana

# Funciona bem mas nao é pythonica
minha_lista = []
for i in range(1,101):
    minha_lista.append( i )

# Forma pythonica
minha_lista = [ i for i in range(1,101) ]


# Maneira 1
meus_quadrados = []
for i in range(1,101):
    meus_quadrados.append(i**2)
meus_quadrados_2 = [ i**2 for i in range(1,101) ]



import string
letras_baixas = string.ascii_lowercase
letras_altas = string.ascii_uppercase


minhas_letras = [ letras_altas[i] + letras_baixas[i] for i in range(len(letras_altas)) ]

minhas_letras = []
for i in range( len(letras_baixas) ):
    minha_str = letras_altas[i] + letras_baixas[i]
    minhas_letras.append( minha_str )


numeros = [ i for i in range(10) ]
a = numeros[0]
b = numeros[1]
c = numeros[2:]

a, b, *c, d, e = [1, 2, 3, 4, 5, 6, 7]


