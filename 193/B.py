N = int(input())
count = 0
amountOfMoney = []
for i in range(N):
    a, p, x = map(int, input().split())
    if a < x:
        count += 1
        amountOfMoney.append(p)

if count == 0:
    print(-1)
else:
    print(min(amountOfMoney))
