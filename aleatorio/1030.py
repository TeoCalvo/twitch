qt_casos = int(input())

result = []
for q in range(qt_casos):
    n, m =[int(i) for i in input().split(" ")]

    homens = list(range(1,n+1))
    indices = list( range(1,m+1) ) * 10000

    i = 0
    rodadas = []
    while len(homens) > 1:
        rodadas.extend(homens.copy())
        while True:
            try:
                if indices[i] == m:
                    homens.remove(rodadas[i])
                i+=1
            except IndexError:
                break
    
    result.append( homens[-1] )

for i in range(1, qt_casos+1 ):
    print("Case {}:".format(i), result[i-1])