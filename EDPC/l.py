import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

# N = II()
# ns = LI()

"""
自分は大きな数字を取りつつ、相手には小さい数字を取らせたい
ミニマックス法
player1(自分)は勝ちを最大化しplayer2(相手)はplayer1の勝ちを最小化する

方針
N*Nのdpを作成 (縦をl,横をrとする)
l = 区間の始まりの場所
r = 区間の終わり
w = 区間の幅

区間の幅と始点の位置で二次元dp

dp[i][i]は
"""

N = II()
A = LI()
#dp[l][r] := 半開半閉区間[l, r)からゲームを始めた時に最適行動をした場合のX-Y
dp = [[0] * (N+1) for _ in range(N+1)]
for w in range(1, N+1):
    #wを設定　幅が0のときは区間がないので0のまま
    for l in range(N+1-w):
        r = l+w
        dp[l][r] = max(-dp[l+1][r] + A[l], -dp[l][r-1] + A[r-1])
        #l-rまでの区間で
for xx in dp:
    print(xx)
