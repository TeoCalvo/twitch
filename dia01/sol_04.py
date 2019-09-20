#Crie um programa que receba um número natural de 1 a 12
#retorne o mês correspondente.

meses = {
    1:'janeiro',
    2:'fevereiro',
    3:'março',
    4:'abril',
    5:'maio',
    6:'junho',
    7:'julho',
    8:'agosto',
    9:'setembro',
    10:'outubro',
    11:'novembro',
    12:'dezembro'
}

numero_mes = input()
if numero_mes.isdigit() and 1 <= int(numero_mes) <= 12:
    print( meses[int(numero_mes)] )
else:
    print("Entre com um mês válido!")