N = int(input())
a, b, c = map(int, input().split())
cnt = 9999+1

for i in range(cnt):
    x = c*i
    if x > N:
        break
    for j in range(cnt-i):
        y = b*j
        if x + y > N:
            break
        if (N - y-x) % a == 0:
            k = (N - y-x)/a
            tmp_Cnt = i+j+k
            cnt = min(cnt, int(tmp_Cnt))
print(cnt)
