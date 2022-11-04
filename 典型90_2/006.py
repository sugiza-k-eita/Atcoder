import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N,K = MI()
letter = S()

# ord('a')→97
# chr(97)→a
INF = 10**18
dp = [[INF for i in range(26)] for i in range(N+1)]
#N+1行目は、使わないけど、dp[i][j]=dp[i+1][j]とするときに必要になる

for i in range(N-1,-1,-1):#後ろからみる
    for j in range(26):#a~zの26もじについて
        dp[i][j] = dp[i+1][j]#i文字目以降でj番目のアルファベットがはじめて出てくるのは、
    dp[i][ord(letter[i]) - ord("a")] = i#i文字目がj番目のアルファベットのときのみ、= i

ans = ""
cnt = 0
now = 0
while cnt !=K:#文字列の長さはKになるまで
    for j in range(26):#辞書順最小のaから順に
        if N - dp[now][j] >= K-cnt:
            #now番目の文字にアルファベットj番目の文字を使用したとき
            # もし、N-dp[now][j](残り使える文字数) >= K-cnt(目標の文字列までの数)ならok
            ans += chr(ord('a') + j)
            #次の探索範囲は、現在使用した文字のindex+1からなので
            now = dp[now][j] + 1
            #文字列カウント+1
            cnt += 1
            break
print(ans)

"""
基本的には、Aを取っていきたい。
が、
N=3,K=2, S = zza　の場合
最初の文字にaを取ってしまうと、それ以上の文字を取ることができない。
Q何文字目まで取ることができるのか？
取った文字のカウントをcntとすると、
残り取らなきゃいけない文字列の量は、K-cntです。

N = 7, K = 3, S = atcoderの場合
cnt=0のとき
atcod (7-3=4文字目まで取ることができる)
→aを取る

cnt=1のとき
tcode (7-3+1=5文字目まで取ることができる)
→cを取る

cnt=2のとき
oder (7-3+2=6文字目まで取ることができる)
→dを取る

この例からも、N-K+cnt文字列まで取ることが可能です。

なので、実装内容は、
N*26の2次元配列を作成する
0~Nで、i文字目以降に現れるa,b・・・zの場所を記憶しておく

0~N文字目までについて、for文を回す
a~Zについて見ていき、もしaがN-K+cnt文字列目にあったら採択し、なかったらbについて見る
cnt == Kになるまで行う
"""