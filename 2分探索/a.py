# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_a

import bisect
"""
sortされている配列に対し、2分探索である数字の場所を探索する
"""
N, K = map(int, input().split())
ns = list(map(int, input().split()))

min_index = bisect.bisect_left(ns, K)
"""
nsという配列に対し、Kという値が左から何番目に出てくるかをindex
に格納している
"""

if min_index == N:
    print(-1)
else:
    print(min_index)
