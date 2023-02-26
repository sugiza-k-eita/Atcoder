import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
A = LI()
A.sort()

ruiseki = [A[0]]

for i in range(1,N):
    new = ruiseki[-1]+A[i]
    ruiseki.append(new)

cnt = 0
for i in range(N-1):
    if ruiseki[i]*2 >= A[i+1]:
        cnt += 1
    else:
        cnt = 0

print(cnt+1)

"""
今回、自分の2倍までの個体なら捕食することができます。
そのため、モンスターを小さい順に並べたとき
i番目の個体がi+1番目の個体を捕食できるかは、
0からi番目の個体の和の2倍とi+1番目の個体の大小によって決まります。
もし大きければ、i番目の個体の大きさは0からi+1までの和となり、次にi+2を捕食できるか検討し、
もし小さければ、i番目までの全ての個体は最終個体になりえないことがわかります。

このように現地点までの累積和と次の地点のモンスターの大きさを比べることで最終個体になり得るかを検討していきます



累積和を用いて解く
"""