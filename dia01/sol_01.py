#Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno.
# A seguir, calcule a média do aluno, sabendo que:
#  nota A tem peso 0.2, a nota B tem peso 0.3 e a nota C tem peso 0.5.
# Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

media = 0 
for i in [0.2, 0.3, 0.5]:
    media += float( input() ) * i

print(media)