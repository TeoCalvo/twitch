import random

correto = random.randint( 1, 6 )
tentativa = 1

while tentativa <= 3:

    num = int( input("Entre com um valor: ") )
    
    if num == correto:
        print("Você acertou! Gênio! Você é um campeão!")
        break

    elif num > correto:
        print("Número muito alto! Tente um valor menor.")

    else:
        print("Número muito baixo! Tente um valor maior.")
    tentativa += 1

if tentativa == 4:
    print("Acabou para você!")