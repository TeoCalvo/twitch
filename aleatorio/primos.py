from tqdm import tqdm

primes = set( range(2,2000001) )
all_numbers = list(primes)

for i in tqdm(primes):
    if i in primes:
        list_tmp = list(all_numbers)
        list_tmp = list_tmp[ list_tmp.index(i) + i : : i ]
        primes = primes - set(list_tmp)

sum(primes)
