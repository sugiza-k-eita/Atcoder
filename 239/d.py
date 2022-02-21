from bisect import bisect, bisect_left
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

A,B,C,D = MI()

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

sosuu = Eratosthenes(B+D)
"""
青木くんの取れる範囲はD-Cの範囲
つまりその範囲に素数が含まれないような
bisectして疲れる素数を列挙
"""
takahasi_ruiseki = [0]*(B+D+1)
aoki_ruiseki = [0]*(B+D+1)
a = bisect_left(sosuu,C)
w = D -C
#選択しうる素数
used = sosuu[a:]
flg = B -A
for i in range(A,B+1):
    cnt = 0
    for j in range(C,D+1):
        tmp = i + j
        if tmp  in sosuu:
            cnt += 1
    if cnt == 0:
        print("Takahashi")
        exit()
print("Aoki")
