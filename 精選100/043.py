import sys
import collections
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()


N = II()
flag =[[0]*5 for i in range(N)]
for i in range(5):
    colors = S()
    for j in range(N):
        flag[j][i] = colors[j]

INF = float("inf")
dp= [[INF]*3 for i in range(N)]


count = collections.Counter(flag[0])
color_variation = [[0,"R"], [1,"B"], [2,"W"]]

for num_color in color_variation:
    num,color=num_color[0], num_color[1]
    drow = 5 - count[color]
    dp[0][num] = drow


for i in range(1,N):
    count = count = collections.Counter(flag[i])
    for num_color in color_variation:
        numbers = [0,1,2]
        num,color=num_color[0], num_color[1]
        drow = 5 - count[color]
        numbers.pop(num)
        for k in numbers:
            dp[i][num] = min(dp[i][num], dp[i-1][k]+drow)

# for xx in dp:
#     print(xx)

print(min(dp[-1]))