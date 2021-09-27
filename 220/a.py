a, b, c = map(int, input().split())
flg = 0
for i in range(1, 1001):
    tmp = i*c
    if a <= tmp and tmp <= b:
        flg = 1
        print(tmp)
        break
if flg == 0:
    print(-1)
