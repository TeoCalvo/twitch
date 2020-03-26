'''Um Posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes.
Escreva um algoritmo para ler o tipo de combustível abastecido
(codificado da seguinte forma: 1.Álcool 2.Gasolina 3.Diesel 4.Fim).
Caso o usuário informe um código inválido (fora da faixa de 1 a 4) deve ser solicitado um novo código
(até que seja válido). O programa será encerrado quando o código informado for o número 4.

Entrada
A entrada contém apenas valores inteiros e positivos.

Saída
Deve ser escrito a mensagem: "MUITO OBRIGADO"
e a quantidade de clientes que abasteceram cada tipo de combustível, conforme exemplo.'''

n_alcool = 0
n_gas = 0
n_diesel = 0

opcao = 0
while opcao != 4:
    opcao = int(input("Entre com uma opção entre 1 a 4: "))
    if opcao == 1:
        n_alcool += 1
    elif opcao == 2:
        n_gas += 1
    elif opcao == 3:
        n_diesel += 1

print("Muito obrigado")
print("Alcool:", n_alcool)
print("Gasolina:", n_gas)
print("Diesel:", n_diesel)