import itertools
S,K = input().split()
K = int(K)
box = []
for i in range(len(S)):
    box.append(S[i])
box.sort()
#print(box)

a = list(itertools.permutations(box))
table = list(set(a))
table.sort()

print(*table[K-1], sep="")


