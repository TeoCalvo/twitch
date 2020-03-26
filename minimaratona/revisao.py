# String
frase = 'Olá mundo!'
print(frase) # exibindo uma string

# Inteiros
a = 10
b = 20
c = a + b
print(c)    

idade = 27
altura = 1.82

coeficiente = idade / altura
print(coeficiente)


# Float

# print, input
nome = input('Qual o nome da sua mãe:')
quant_letras = len(nome)
print('O nome da sua mãe tem ', quant_letras, ' letras' , sep='')

# Listas
listagem = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Quantidade de elementos
quant = len(listagem)
print('A lista tem', quant , 'elementos')

# Soma de todos os elementos
soma = sum(listagem)
print('A soma de todos os elementos é:' , soma)

maior = max(listagem)
print('O elemento de maior valor é:', maior)

media = soma / quant
print('A média dos elementos é:', media)

# Diconários

dicionario = {'nome':'Natália',
                'idade':29 ,
                'sexo':'Feminino',
                'cidade_natal':'Guararapes',
                'cidade_atual': 'São Paulo'}

letras_cid_natal = len(dicionario['cidade_natal'])
print('A cidade natal tem ', letras_cid_natal, 'letras')

letras_nome = len(dicionario['nome'])
print('O seu nome tem ', letras_nome , 'letras')

dicionario['peso'] = 50.1

print(dicionario)