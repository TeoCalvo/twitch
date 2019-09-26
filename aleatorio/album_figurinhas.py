import random
from tqdm import tqdm
import numpy as np

def complete_album(N, n):
    album = set( range(1,641) )
    count = 0
    while len(album) > 0:
        album -= set(random.choices( range(1,641), k=5 ))
        count += 1

    return count

albuns = [ complete_album( 640, 5 ) for i in tqdm(range(10000))  ]

print("Média:", np.mean( albuns ) )
print("Desvio Padrão:", np.std( albuns ) )
ic_sup = np.round( np.mean( albuns ) + 1.96 * np.std( albuns ) / np.sqrt( len(albuns) ) , 2)
ic_inf = np.round( np.mean( albuns ) - 1.96 * np.std( albuns ) / np.sqrt( len(albuns) ), 2)

print("Intervalos de confiança: [{} ; {}]".format( ic_inf, ic_sup )  )
