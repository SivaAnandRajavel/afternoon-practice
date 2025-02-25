import itertools


def prime_numbers():
    yield 2  # start no
    prime_cache = [2]  # cache user to catch all thew prime nos
    for n in itertools.count(3, 2):
        is_prime = True
        for p in prime_cache:
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            prime_cache.append(n)
            yield n


for p in prime_numbers():
    print(p)
    if p > 30:
        break
