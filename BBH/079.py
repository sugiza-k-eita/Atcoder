#https://atcoder.jp/contests/abc124/tasks/abc124_d
"""
方針ランレングスする
累積わするor 尺取法で解く
"""
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
ruiseki = [0]
tmp = 0
ans = 0
for i in range(len(a)):
    num,c = a[i][0],a[i][1]
    if i == 0:
        if num == 0:
            ruiseki.append(0)
    tmp += c
    ruiseki.append(tmp)
    ans = max(ans,c)
    
    if i == len(a)-1:
        if num == 0:
            ruiseki.append(tmp)


for left in range(0,len(ruiseki),2):
    right = left + 2*K + 1
    if right >= len(ruiseki):
        break
    
    tmp_ans = ruiseki[right] -ruiseki[left]
    ans = max(ans,tmp_ans)
print(ans)
    
