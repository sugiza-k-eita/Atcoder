N = int(input())
s_time = list(map(int, input().split()))
t_time = list(map(int, input().split()))
count = 0

first_index = t_time.index(min(t_time))

maximun = float("inf")
ans = [maximun]*2*N
i = first_index
ans[i] = t_time[i]


for j in range(i):
    s_time.append(s_time[j])
    t_time.append(t_time[j])


while True:
    if i+1 == len(s_time):
        break
    ans[i+1] = min(ans[i]+s_time[i], t_time[i+1])
    i += 1


for p in range(N):
    display = min(ans[p], ans[p+N])
    print(display)
