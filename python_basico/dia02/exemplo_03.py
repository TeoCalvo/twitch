# programa para calcular a área de um círculo

from math import pi # Importando apenas o pi

raio = input("Entre com o raio do seu circulo em centimetros:") # Recebe valor de raio do usuário (string)
raio = float( raio ) # Converte string para float

area = pi * (raio ** 2) # Calcula a área do circulo com a fórmula da área
area = round( area, 2 ) # Arredonda a nossa area

print("A área é igual a:", area) # Exibe a área calculada e arredondada

