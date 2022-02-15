import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

Q = II()

# その数までにある素数を列挙
def Eratosthenes(N):
    N += 1
    is_prime_list = [True] * N
    m = int(N ** 0.5) + 1
    for i in range(3, m, 2):
        if is_prime_list[i]:
            is_prime_list[i * i :: 2 * i]=[False] * ((N - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, N, 2) if is_prime_list[i]]

box = Eratosthenes(10**5)
ruiseki = [0 for i in range(10**5)]
for i in range(2,10**5):
    if i in box and (i+1)//2 in box:
        ruiseki[i] = ruiseki[i-1] + 1
    else:
        ruiseki[i] = ruiseki[i-1]

for i in range(Q):
    l,r = MI()
    print(ruiseki[r]-ruiseki[l-1])