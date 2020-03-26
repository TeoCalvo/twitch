salario = float(input('Digite seu salario: R$'))

faixas = [ [0, 2000],
           [2000.01, 3000 ],
           [3000.01, 4500],
           [4500.01, 1000000]  ]

pesos = [0, 0.08, 0.18, 0.28]

def calc_imposto( salario, faixas, pesos ):
    valores = []
    for i in faixas:
        if salario < i[-1] - i[0]:
            valores.append(salario)
        else:
            valores.append( i[-1] - i[0] )
        salario -= (i[-1] - i[0])
        if salario <= 0 :
            break
        
    imposto_faixas = []
    for i in range( len(valores) ):
        imposto_faixas.append( valores[i] * pesos[i] )
    return sum( imposto_faixas )
        

calc_imposto(3002.00, faixas, pesos)




'''de 0 a 2000 -> isento
de 2000.01 a 3000 -> 8%
de 3000.01 a 4500 -> 18%
acima de 4500.01 -> 28%'''

