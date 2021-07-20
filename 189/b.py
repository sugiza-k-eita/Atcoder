n, x = map(int, input().split())
alcohol_list = []
for i in range(n):
    a, b = map(int, input().split())
    alcohol = a*b
    alcohol_list.append(alcohol)
count = 0
flg = 0
x *= 100
for i in alcohol_list:
    if x >= 0:
        count += 1
        x -= i
        print(x)
    elif x < 0:
        break

if x < 0:
    print(count)
else:
    print(-1)
