def par_impar(num) :
    resto = num % 2
    if resto == 0:
       return 'par'
    else :
       return 'impar'

numero_1 = int(input('Digite um numero '))
numero_2 = int(input('Digite um numero '))
print('O primeiro numero é ', par_impar(numero_1))
print('O segundo numero é ', par_impar(numero_2))

def exibe_nome(nome):
    print(nome)

def retorna_nome(nome):
    return nome

nome = exibe_nome("Teodoro")
type( nome )

