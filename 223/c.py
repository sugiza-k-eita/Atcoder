N = int(input())
leng1 = []
speed1 = []
time1 = []
for i in range(N):
    a, b = map(int, input().split())
    leng1.append(a)
    speed1.append(b)
    time1.append(a/b)

# print(leng1)
# print(time1)

cnt = sum(time1)/2
# print(cnt)
tmp = 0
time_via = 0
pre_via = 0
for i in range(N):
    tmp += time1[i]
    if tmp >= cnt:
        time_via = i
        break
    pre_via = tmp
ans = 0
rrr = cnt-pre_via
for i in range(time_via):
    ans += leng1[i]
# print(ans)
# print(rrr*speed1[time_via])
ans += rrr*speed1[time_via]
print(ans)
