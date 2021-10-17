from itertools import product, repeat


N, M = map(int, input().split())
box = []
for i in range(M):
    a, b = map(int, input().split())
    box.append([a, b])
K = int(input())

people = []
for i in range(K):
    c, d = map(int, input().split())
    people.append([c, d])

for bit in product((0, 1), repeat=K):
    # K個の場所を0,1のbit探索よって計算量はK^^2乗
    cnt = [0]*(N)
    for i in range(K):
        ball = people[i][bit[i]]
