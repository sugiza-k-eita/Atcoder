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


N, M = map(int, input().split())
A = list(map(int, input().split()))
maxA = max(max(A), M)


is_prime = [True] * (maxA + 1)
is_prime[0] = False
is_prime[1] = False
# is_primeは素数かそうじゃないか
k = [True]*(maxA+1)
# 今回の条件を満たすk
# 最初はすべて満たす
primes = []
# Aの各要素の素因数を格納する


# 条件その1
# Aの中に含まれるkはFalse
for a in A:
    k[a] = False
# 条件2
# Aの中に含まれる各要素の素因数を持たない
# A = [6,15]だったら、2,3,5は不適
for p in range(2, maxA + 1):
    if not is_prime[p]:
        continue
    # Falseだったらpは不適
    # 0,1とAの要素は不適
    for i in range(p*2, maxA + 1, p):
        is_prime[i] = False
        # iがAの各要素の素因数に含まれる場合はFalse
        # ex) p=3だとたら、i = 6,9,12・・・でA=[6]の場合
        # だめだから
        # 要するにiがAの要素になる場合、そのpはAの(素)因数となる
        k[p] = k[p] and k[i]
    if not k[p]:
        # k[p]がFalse、つまりpがAの素因数を持つとき
        primes.append(p)
        # primesに格納
        # primesはAの各要素の素因数
        # primesに含まれる数(とその定数倍)は×

# 条件3 Aの要素に含まれる素因数の定数倍は×
# 4,12は2を因数にもつため、不適
for p in primes:
    for j in range(p*2, M+1, p):
        k[j] = k[j] and k[p]

ans = [1]

for i in range(2, M+1):
    if k[i] == True:
        ans.append(i)
print(len(ans))
for i in ans:
    print(i)
