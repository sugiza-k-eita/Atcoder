from itertools import permutations
import math
N = int(input())
box = []
for i in range(N):
    x, y = map(int, input().split())
    box.append([x, y])
ans = 0
for per in permutations(range(N)):
    for i in range(N-1):
        x = box[per[i]][0] - box[per[i+1]][0]
        y = box[per[i]][1] - box[per[i+1]][1]
        x_leng = x**2
        y_leng = y**2
        dist = x_leng+y_leng
        ans += math.sqrt(dist)
aa = math.factorial(N)
print(ans/aa)
