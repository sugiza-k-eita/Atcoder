from collections import Counter
N = int(input())
C = Counter()

for i in range(N):
    a, b = map(int, input().split())
    C[a] += 1
    C[a+b] -= 1

#
ans = [0] * (N+1)

sort_days = sorted(C.keys())
# 日付順に並んだ状態

pre_day = 0
cnt = 0

for today in sort_days:
    ans[cnt] += today-pre_day
    # 現在ログインしている人数は(今回人数が変わった日)−（前回人数が変わった日）
    cnt += C[today]
    pre_day = today

print(*ans[1:])
