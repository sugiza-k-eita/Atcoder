N, K = map(int, input().split())


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


ans = 0

K_prime = list_primes(N)
for i in K_prime:
    if i >= K:
        ans += 1
print(ans)
