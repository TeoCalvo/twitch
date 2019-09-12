# Exemplos de listas

minha_lista = [] # lista vazia

# Lista de téo
teo_1 = ["Téo", "Calvo", 27, 1.80, 65, "Nah" ]
teo_1.append( "Kira" )
teo_1[0] = "Teodoro" # Troca apelido para nome
teo_1[1:4]

# Lista de numeros

numeros = [1,2,3,4,5,6,7,8,9,10,11, "ultimo numero"]
numeros[ len(numeros) - 1 ]

sum( numeros[0:-1] )
numeros_2 = numeros[:]

numeros_2.remove( "ultimo numero" )

numeros_2