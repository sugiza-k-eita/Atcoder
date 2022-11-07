import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
import copy
N = II()
P = LI()

for i in range(N-1,-1,-1):
    if P[i] < P[i-1]:
        ans = P[:i-1]
        flg = P[i-1:]
        break

aa = copy.copy(flg)
aa.sort()
# s
ind = aa.index(flg[0])
head = [aa[ind-1]]
aa.pop(ind-1)
aa.sort(reverse=True)
ans1 = head + aa
final_ans  = ans+ans1
print(*final_ans, sep=" ")

