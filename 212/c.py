import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
ans = 10**9
for i in A:
    j = bisect.bisect_left(B, i)
    # iという要素は、Bというリストの何番目の要素になるか
    if 0 <= j - 1 < M:
        # i-1がBのリスト外にならないようにする処理
        b1 = B[j - 1]
        ans = min(ans, abs(i - b1))
    if 0 <= j < M:
        # j==Mは範囲外→indexは0から振られているから
        b2 = B[j]
        ans = min(ans, abs(i - b2))
print(ans)
