import bisect
N, M, D = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
max_sum = -1
for i in range(N):
    j = bisect.bisect_right(B, A[i]+D)
    if j == 0:
        if abs(A[i] - B[j]) <=D:
            max_sum = max(max_sum, A[i] + B[j+1])

    if j >= M-1:
        if abs(A[i] - B[j-1]) <=D:
            max_sum = max(max_sum, A[i] + B[j-1])
    else:
        if abs(A[i] - B[j-1]) <=D:
            max_sum = max(max_sum, A[i] + B[j-1])
        if abs(A[i] - B[j]) <=D:
            max_sum = max(max_sum, A[i] + B[j])

print(max_sum)

"""
AとBについて全探索しては計算量O(NM)でだめ

なので、計算量を落とす工夫が必要

そこで、事前にソートしておき、片方について全探索し、二分探索をして
差がD以下にできるBの最大値を求める
これは、A[i]+Dよりも小さい数の最大値になる


"""