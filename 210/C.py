from collections import Counter

N, K = map(int, input().split())
ns = list(map(int, input().split()))
counter = Counter(ns[:K])  # 最初のK個 0から数えるから０番目からk-1番目までのk個
ans = len(counter)  # 最初のK個の種類数
for i in range(K, N):
    left = ns[i - K]  # 1回目が K - K = 0（一番左）になるように
    right = ns[i]
    counter[left] -= 1
    counter[right] += 1
    if counter[left] == 0:
        del counter[left]  # 0個でもlenで数えられてしまうので、delで消す
    ans = max(ans, len(counter))  # 現在の種類数で答えを更新
print(ans)

"""
#自作コード　TLE

import itertools

n, k = map(int, input().split())
ns = list(map(int, input().split()))
table = []
max = 0
for i in range(n-k+1):
    table.append(ns[i:i+k])
    tmp = list(itertools.chain.from_iterable(table))
    # 2重配列をなくしている
    unique_table = set(tmp)
    # 被りを除去
    leng = len(unique_table)
    if leng > max:
        max = leng
    table = []
    # tableの初期化
print(max)
"""
