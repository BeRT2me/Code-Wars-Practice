def num_primorial(n):
    p_hash = 2
    thing = gen_primes()
    primes = [next(thing) for x in range(n)]
    for prime in primes[1:]:
        p_hash *= prime
    return p_hash


def gen_primes():  # http://code.activestate.com/recipes/117119/
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1