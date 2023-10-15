
from collections import Counter
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = II()
s = S()

numbox = []
for i in range(N):
    numbox.append(s[i])
numbox.sort(reverse=True)
max_val = int("".join(numbox))

f = max_val**0.5
f = f+1
f = str(f)
# print(f)
int_num ,_ = f.split(".")
int_num = int(int_num)
s_count = Counter(s)
ans = 0
# # print(s_count)
# print(int_num)
for i in range(int_num+1):
    i_i = str(i*i)

    
    squared_count = Counter(str(i_i))
    # print(squared_count,i_i)
    cnt = 0
    n_cnt = 0
    for n in ["0","1","2","3","4","5","6","7","8","9"]:
        n_cnt += 1
        if n=="0" and squared_count[n] <= s_count[n]:
            cnt += 1
        elif n != "0" and squared_count[n] == s_count[n]:
            cnt += 1
    
    if n_cnt == cnt:
        ans += 1
        # print(i_i,i,s_count,squared_count)
print(ans)

