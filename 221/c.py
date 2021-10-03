import itertools
N = str(input())
box = []
for i in N:
    box.append(i)

p = itertools.permutations(box, len(N))
Ans = 0
for i in p:
    for j in range(len(N)-1):
        a = i[:j+1]
        b = i[j+1:]
        a = list(a)
        b = list(b)
        A = "".join(a)
        B = "".join(b)
        A = int(A)
        B = int(B)
        ans = A*B
        Ans = max(Ans, ans)

print(Ans)
