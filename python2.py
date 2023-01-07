import time
def get_sequence_c(a, b):
    def is_prime(n):
        if n < 2:
            return False
        return get_primes(n)[n-1]

    def get_primes(n):
        primes = [True] * n
        primes[0] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i ** 2, n, i):
                    primes[j] = False
        return primes

    c = []
    b_count = {}
    for x in b:
        if x in b_count:
            b_count[x] += 1
        else:
            b_count[x] = 1
    for x in a:
        if x not in b_count or not is_prime(b_count[x]):
            c.append(x)
    return c


a = [2, 3, 9, 2, 5, 1, 3, 7, 10]
b = [2, 1, 3, 4, 3, 10, 6, 6, 1, 7, 10, 10, 10]
start_time_1 = time.perf_counter()
c = get_sequence_c(a, b)
print(c)
end_time_1 = time.perf_counter()
elapsed_time_1 = end_time_1 - start_time_1
print(elapsed_time_1)