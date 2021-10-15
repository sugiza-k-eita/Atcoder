# その数までに何個素数があるかを数える
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

# 0 から　N番目の数それぞれが何個素数を持っているか判別する


def list_primes(limit, *k):
    have_K_primes = [0]*(limit+1)
    # k個の素数を持っているやつを格納
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
