N = int(input())
ns = list(map(int, input().split()))

sorted_ns = sorted(ns)
index = sorted_ns[-2]
ans = ns.index(index)+1
print(ans)
