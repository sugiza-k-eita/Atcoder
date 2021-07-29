n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

account = B[0] - A[-1] + 1
if account >= 0:
    print(account)
else:
    print(0)
