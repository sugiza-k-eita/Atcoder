"""
二人零和有限確定完全情報ゲームはdpでとける

解法
dp[i] = 山がiこの状態の時、先手が勝つか？

山が0個の時、先手負ける
山が1このとき、nsに1があれば勝てる
"""
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N,K = MI()
ns = LI()
#Trueのときはfirstがかつ
dp = [False]*(K+1)
dp[0] = False
for i in range(1,K+1):
    for j in range(N):
        if i -ns[j] <0:
            continue
        if dp[i-ns[j]] == True:
            dp[i] = False
        else:
            dp[i] = True
            break
# print(dp)
if dp[-1] == False:
    print("Second")
else:
    print("First")

