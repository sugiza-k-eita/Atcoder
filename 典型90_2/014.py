import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
A = LI()
B = LI()
A.sort()
B.sort()

ans = 0
for i in range(N):
    ans += abs(A[i]-B[i])
print(ans)

"""
014 - We Used to Sing a Song Together（★3）
https://atcoder.jp/contests/typical90/tasks/typical90_n


今回は、小学校と小学生の数が同じなので、1小学校に1人の生徒を割り当てる必要があります。
そして、その総和を最小にする問題です。

そのため、誰か1人の不便さを最小にするよりも全体の不便さを下げるためにはどうしたら良いかを考えます。
それは、それぞれをソートして、i番目の生徒をi番目の小学校に割り当てれば良いです。


解説が解説になってない気もするけど、、、ごめんちゃい
"""