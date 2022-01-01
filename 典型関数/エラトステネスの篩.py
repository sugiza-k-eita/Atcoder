# その数までにある素数を列挙
def Eratosthenes(N):
    N += 1
    is_prime_list = [True] * N
    m = int(N ** 0.5) + 1
    for i in range(3, m, 2):
        if is_prime_list[i]:
            is_prime_list[i * i :: 2 * i]=[False] * ((N - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, N, 2) if is_prime_list[i]]
#下記もその数までにある素数を列挙しているが、遅い
"""
def list_primes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False

    for p in range(0, limit + 1):
        if not is_prime[p]:
            continue
        primes.append(p)
        for i in range(p*p, limit + 1, p):
            is_prime[i] = False
    return primes
"""

# 0 から　N番目の数それぞれが何種類の素因数を持っているか判別する
def list_primes(limit, *k):
    have_K_primes = [0]*(limit+1)
    # k種類の素因数をもつか返す
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False

    for p in range(0, limit + 1):
        if not is_prime[p]:  # Falseだったら
            continue
        # Trueだったら↓
        for i in range(p, limit + 1, p):
            is_prime[i] = False
            have_K_primes[i] += 1

    return have_K_primes
