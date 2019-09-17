def f( x ):
    return x ** 2

def caixa_alta( txt ):
    return txt.upper()

def soma( *nums, remove=9 ):
    '''Soma uma quantidade qualquer de numeros'''
    # Altera tipo de tupla apr alista
    nums = list(nums)
    # remove da lista todas ocorrencias do valor a ser removido
    remove_from_list( lista=nums, remove=remove )
    # aplica a soma
    return sum( nums )

def media( *nums, remove=9 ):
    ''' Função para calcular a media de uma lista de numeros'''
    # Nums é do tipo tuple
    nums = list(nums)
    remove_from_list( lista=nums, remove=remove )

    # -> aqui ja nao tem mais nove
    return soma( *nums ) /  len( nums )

def remove_from_list( lista, remove=9 ):
    while remove in lista:
        lista.remove( remove )