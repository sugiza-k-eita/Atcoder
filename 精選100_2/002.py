import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
ans = 0
#i をj で割ってあまりがなかったら約数と言える
#N < なので、2回全探索可能

# 1 ~ Nまでのi(割られる数)を1~Nまでのj(割る数)で割って、あまりが出なかったらjはiの約数なので、cnt += 1
for i in range(1,N+1):
    cnt = 0
    for j in range(1,N+1):
        if i % j == 0:
            cnt += 1
    
    if cnt == 8 and i % 2 == 1:
        #cnt == 8　で　iが2の倍数ではないならans += 1
        ans += 1
print(ans)