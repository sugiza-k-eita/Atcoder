import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N,K = MI()
ns = LI()
"""
二人零和有限確定完全情報ゲーム(千日手などのループがない)では
「自分の手番のあと、相手がかてる状況で盤面を回さない」というのが
勝つための条件(負けないための条件)
探索方法は勝ち負けがすでに決まっている局面をもとにして
現地店からその局面に遷移できるかを考える

"""
"残りの碁石の数が0の状態で相手に手番を回したら勝ち"
dp = [0] * (K + 1)
for i in range(1, K + 1):
  for j in range(N):
    if i - ns[j] >= 0 and dp[i - ns[j]] == 0:
      dp[i] = 1

if dp[K]:
  print('First')
else:
  print('Second')

