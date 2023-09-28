N = int(input())

X = []
Y = []
for i in range(N):
    x,y = map(int, input().split())
    X.append(x)
    Y.append(y)

X.sort()
Y.sort()

x = X[N//2]
y = Y[N//2]

ans = 0
for i in range(N):
    ans += abs(x-X[i]) + abs(y-Y[i])
print(ans)