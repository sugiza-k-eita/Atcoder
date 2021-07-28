from operator import mul
from functools import reduce


def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


n = int(input())
ns = list(map(int, input().split()))
remainder = []
for i in ns:
    remainder.append(i % 200)
ans = 0
cnt = [0] * 200

for j in remainder:
    cnt[j] += 1
for j in cnt:
    if j > 1:
        ans += cmb(j, 2)


"""
nC2　=　n(n-1)/2　と同じ結果が得られる
そのため、jまでのnC2について知りたかったら、
これまで出てきた0~j-1のデータを足せば良い

for j in remainder:
    ans += cnt[j]
    # cnt[j]は0~j-1までに出てきた回数を足している
    # cnt[j]は0~j-1のデータを保持
    cnt[j] += 1
    # ansにcnt[j]の情報を足したあとに、cnt[j]に今回分を足す
    # これでcnt[j]は0~jまでのデータを保持している
"""
print(ans)
