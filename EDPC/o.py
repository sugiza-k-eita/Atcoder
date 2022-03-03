import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

"""
bitDP
bitDPというテクニックを使う問題ね。
bitDPというのは、集合を数に変換して状態(=添字)として持つようなDPのことよ。
例えば{0,2,3}という集合は2**0+2**2+2**3=13という数に変換して、
「数iが集合に属しているか」と「i bit目が1か」を対応させる

dp[i][S]=(男性はi人目までで、既にペアになった女性の集合がSであるような場合の数)
としてDPするわ。

少し考えると「既にペアになった女性の集合がS」なら
「bitpopcount(S)人目までをチェックした」ってことになるから、iを状態として持つ必要は無い
"""

MOD = 10**9+7
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
#dp[i][S]:= i番目の男性まで決めて、集合Sの女性の選び方を決めた時の場合の数
dp = [[0] * (2**N) for _ in range(N+1)]
dp[0][0] = 1
for i in range(1,N+1):
    for s in range(1<<N):
        #1をNビットだけ左シフト
        #2**N倍される
        if dp[i][s] == 0:
            #配る側が0の時、0を配っても意味がないから
            continue
        for j in range(N):
            if (s>>j)&1:
                #すでに配られている場合は
                continue
            if A[i][j] == 0:
                #相性が悪い場合は
                continue
            dp[i][s|(1<<j)] += dp[i-1][s]
            dp[i][s|(1<<j)] %= MOD
            
print(dp[N][-1])
