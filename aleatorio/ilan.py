num = list(range(1,1000))
from tqdm import tqdm
condicoes = [False, False]

for c in tqdm( num[2:] ):
    for b in num[ : num.index(c)]:
        for a in num[ : num.index(b)]:
            condicoes[0] = a**2 + b**2 == c**2
            condicoes[1] = a + b + c == 1000
            if sum(condicoes) == 2:
                print(a,b,c )
                break
        if sum(condicoes) == 2:
                break
    if sum(condicoes) == 2:
        break
    
print(a,b,c)