from collections import Counter
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N,K = MI()

ns = LI()

ruiseki = [0 for i in range(N)]
ruiseki[0] = ns[0]
for i in range(1,N):
    ruiseki[i] = ruiseki[i-1]+ns[i]
C = Counter()
C[0] += 1
ans = 0
for x in ruiseki:
    y = x - K  # x - y = K より、y = x - K である連続部分列が今まで何回出てきたかが知りたいものです
    ans += C[y]
    C[x] += 1

print(ans)
