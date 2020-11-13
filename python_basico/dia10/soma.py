import sys

def operacao( a, *values, **kwargs ):

    result = {}

    if 'soma' in kwargs:
        result['soma'] = sum(values) + a

    if 'multiplicacao' in kwargs:
        result['multiplicacao'] = a
        for i in values:
            result['multiplicacao'] *= i

    return result

if __name__ == "__main__":
    a, b = ( int(i) for i in sys.argv[1:3] )

    print( soma(a, b) )
    print("Executei no programa da minha função")