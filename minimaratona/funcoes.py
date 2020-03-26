lista = [1,2,1,2,3,4,4,54,6,67,6,43,5]
quant = len(lista)
soma = sum(lista)
media_1 = soma / quant

lista_2 = [1,2,2,2,2,3,3,4,5,66,7,7,8,9]
quant_2 = len(lista_2)
soma_2 = sum(lista_2)
media_2 = soma_2 / quant_2

def media( x ):
    quant = len(x)
    soma = sum(x)
    resultado = soma / quant
    return resultado

media(lista_2)

def troca_nome( nome, sobrenome ):
    resultado = sobrenome + ', ' + nome[0] 
    return resultado

troca_nome('Maria','Ataide')



def consumo(litros, quilometragem ) :
    resultado = quilometragem / litros
    return resultado

def razao_preco(p_alcool , p_gasolina):
    resultado = p_alcool / p_gasolina
    return resultado

def razao_consumo( c_alcool, c_gasolina ):
    resultado = c_alcool / c_gasolina
    return resultado

def melhor_combustivel( litros_alcool, km_alcool, litros_gas, km_gas, p_alcool, p_gas  ):
    rend_alcool = consumo(litros_alcool, km_alcool)
    rend_gas = consumo(litros_gas, km_gas)
    razao_p = razao_preco(p_alcool, p_gas)
    razao_c = razao_consumo(rend_alcool, rend_gas)
    if razao_c > razao_p :
        return 'alcool'
    else : 
        return 'gasolina'


melhor_combustivel(50, 650, 30, 650, 3.69, 4.96)