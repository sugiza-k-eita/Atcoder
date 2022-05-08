#https://atcoder.jp/contests/abc124/tasks/abc124_d
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
from collections import deque

N,K = MI()
s = S()

#ランレングス変換する
def rle(s):
    tmp, count, ans = s[0], 1, []
    for i in range(1,len(s)):
        if tmp == s[i]:
            count += 1
        else:
            ans.append([int(tmp),count])
            tmp = s[i]
            count = 1
    ans.append([int(tmp),count])
    return ans

a = rle(s)
print(len(a))

#dequeに変換して取り出しやすくする
q = deque()
for i in range(len(a)):
    c,n = a[i][0],a[i][1]
    q.append((c, n))
print(q)