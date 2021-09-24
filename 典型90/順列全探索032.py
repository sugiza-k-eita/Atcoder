from itertools import permutations
import sys
sys.setrecursionlimit(10**7)
N = int(input())

speed = [list(map(int, input().split())) for i in range(N)]

M = int(input())
monkey_dog = [[[0] for i in range(N)] for i in range(N)]


for i in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    monkey_dog[a][b] = 1
    monkey_dog[b][a] = 1

ans = 10**7

for i in permutations(range(N)):
    # 誰がどの区間を走るか をlistで返す
    # 10!
    time = 0
    flg = True
    for j in range(N-1):
        # そのlistでj番目に走る人とj+1に走る人がタスキを渡せるか
        if monkey_dog[i[j]][i[j+1]] == 1:
            flg = False
            break
        time += speed[i[j]][j]
    time += speed[i[N-1]][N-1]
    if flg:
        ans = min(ans, time)

if ans == 10**7:
    print(-1)
else:
    print(ans)
