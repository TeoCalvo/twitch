# Escreva um programa que recebe 2 valores do usuário
# Armazene os dois valores em variáveis distintas( Ex A e B)
# Troque o valor de A para B e de B para A e exiba novamente

A = input("Entre com o valor de A: ")
B = input("Entre com o valor de B: ")

A, B = B, A

print("A =",A, "\nB =",B)