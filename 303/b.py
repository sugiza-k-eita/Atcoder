N,M = map(int, input().split())
box = []

friends =  [set() for i in range(N)]
for i in range(M):
    a = list(map(int, input().split()))
    for i in range(N-1):
        fre1 = a[i]
        fre2 = a[i+1]
        fre1 -= 1
        fre2 -= 1
        friends[fre1].add(fre2)
        friends[fre2].add(fre1)

cnt = 0
for i in range(N):
    cnt += len(friends[i])
max_freind = N*(N-1)
print((max-cnt)//2)

