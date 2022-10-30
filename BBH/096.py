import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

H,W = MI()
box = []
flg = [[-1] * W for i in range(H)]
for i in range(H):
    A = LI()
    box.append(A)
    
    for j in range(W):
        if A[j]%2 == 0:
            flg[i][j] = 1
ans = []
move = [[0,1],[1,0]]
for i in range(H-1):
    for j in range(W):
        if flg[i][j] == 1:
            continue
        else:
            flg[i+1][j] *= -1
            ans.append([i+1,j+1,i+2,j+1])

for j in range(W-1):
    if flg[-1][j] == 1:
        continue
    else:
        flg[-1][j+1] *=-1
        ans.append([H,j+1,H,j+2])


print(len(ans))
for x in ans:
    print(*x,sep=" ")

"""
偶数枚のコインが置かれたマスの数を最大化するのが目的だが、
どういう場合が最大化と言えるかを考える。

今回、与えられたコインの合計枚数が偶数のときは、すべてのマスを偶数にでき、
与えられたコインの合計枚数が奇数のときは、1つのマスのみ奇数枚のコインとなる

です。今回、コインの枚数はあまり重要ではなく、そのマスが奇数か偶数かが大事
今回、計算量に余裕があるので、dfsやbfsではなく、すべてのマスを全探索して答えを求めていきます。

POINT
全探索するときは、端から端


手順
左上のマスから、そのマスのコインが偶数枚か奇数枚かを見る
偶数のときはなにもせず
奇数のときは、下のマスに一枚コインを移動し、そのマスのコイン枚数を偶数枚にする
そうすると、一番下の行以外は、すべてのマスが偶数になる


最後に一番下の行について、左から順に偶数か奇数かをみる
偶数のときはなにもせず
奇数のときは、右のマスに一枚コインを移動し、そのマスのコイン枚数を偶数枚にする
そうすると、コインの合計が奇数のときは、H行目W列目のみ奇数になり、それ以外は偶数になる

Q なぜ移動方向が下方向か右方向なの？(上や左になぜいかないのか？)
→一度見たマスにコインを移動してしまうと、もう一度コインの枚数を見ないといけないから
POINT
全探索のときは、一度見たマスには二度と干渉しない

"""