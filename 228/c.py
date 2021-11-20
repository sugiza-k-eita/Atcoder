import sys
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()


N, K = MI()
box = [LI() for _ in [None]*(N)]
# for i in range(N):
#     print(box[i])
tmp_point = [0]*N
for i in range(N):
    tmp_point[i] = sum(box[i])
# print(tmp_point)

check = [[0, 0] for _ in range(N)]
# print(check)
# print(check[0])

for j in range(N):
    check[j][0] = tmp_point[j]
    check[j][1] = j

check.sort()
check.reverse()
ans = [False]*N

# print(check)

for i in range(N):
    if check[i][0] + 300 >= check[K-1][0]:
        ans[check[i][1]] = True

for i in range(N):
    if ans[i]:
        print("Yes")
    else:
        print("No")
