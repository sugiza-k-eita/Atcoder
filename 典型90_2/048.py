N,K = map(int, input().split())

box = []
boxa = []
for i in range(N):
    A,B = map(int, input().split())
    sabun = A-B
    box.append(B)
    box.append(sabun)

box.sort(reverse=True)

print(sum(box[:K]))

"""

"""