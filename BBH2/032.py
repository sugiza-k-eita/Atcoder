import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = II()

def Eratosthenes(N):
    N += 1
    is_prime_list = [True] * N
    m = int(N ** 0.5) + 1
    for i in range(3, m, 2):
        if is_prime_list[i]:
            is_prime_list[i * i :: 2 * i]=[False] * ((N - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, N, 2) if is_prime_list[i]]

A = Eratosthenes(N)
print(A)

