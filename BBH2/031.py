import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
A = LI()
A = [0]+A
box = [0]*(N+1)
ans = []
# print(A)
M =0
for i in range(N,0,-1):
    # print(i)
    cnt = 0
    for j in range(i,N+1,i):
        cnt += box[j]
        # print(cnt,j)
    
    if cnt%2 == A[i]:
        continue
    else:
        box[i]+= 1
        ans.append(i)
        M += 1
# print(box)
if len(ans) != 0:
    print(M)
    ans.reverse()
    print(*ans, sep=" ")
else:
    print(0)

"""
O(
N
1 +
N
2 + ... +
N
N
) 程度の計算量がかかります。これは一見 O(N2
) に見えますが、丁寧に解析すると
O(NlogN) で抑えることができます。よって十分高速です。
"""