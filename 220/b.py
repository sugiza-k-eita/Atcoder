K = int(input())
a, b = map(str, input().split())
a = list(reversed(a))
b = list(reversed(b))
ansA = 0
ansB = 0
for i in range(len(a)):
    tmp = K**i
    ansA += int(a[i])*tmp

for i in range(len(b)):
    tmp = K**i
    ansB += int(b[i])*tmp


print(ansA*ansB)
