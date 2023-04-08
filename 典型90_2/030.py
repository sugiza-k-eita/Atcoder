import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def list_primes(limit, k=1):# k種類の素因数をもつか返す
    have_K_primes = [0]*(limit+1)
    is_prime = [True] * (limit + 1)#素数かどうかを判別するリスト
    is_prime[0] = False#0は素数じゃないから、False
    is_prime[1] = False#1は素数じゃないから、False
    #手順1,2
    for p in range(0, limit + 1):
        if not is_prime[p]:  # Falseつまり、素数じゃなければ
            continue
        # 素数であれば
        for i in range(p, limit + 1, p):#その素数の倍数は
            is_prime[i] = False#素数ではないので、
            have_K_primes[i] += 1#その数は、pという素数を因数に持つ
    #手順3
    ans = []
    for j in range(limit+1):
        if have_K_primes[j] >= k:
            ans.append(j)
    
    return ans

N,K = MI()
ans = list_primes(N,K)
print(len(ans))

"""
今回、制約がN< 10^7です。
そのため、大体O(N)になるようにアルゴリズムを組む必要があります。
計算時間の目安については、こちらの記事がものすごくわかりやすくまとまっているのでご参照ください
https://qiita.com/drken/items/872ebc3a2b5caaa4a0d0

今回で求められることは大きく分けて3つあります。
1 2-Nまでの素因数分解
2 1で素因数分解された
3
"""