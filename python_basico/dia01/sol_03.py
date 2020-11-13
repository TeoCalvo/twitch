#Crie um algoritmo para ler um valor em R$ (Reais),
#ler a cotação do dólar e fazer a conversão.

valor_reais = float(input())
cotacao_dolar = float(input())
valor_dolar = valor_reais / cotacao_dolar
print( "U${valor:.2f}".format(valor=valor_dolar))