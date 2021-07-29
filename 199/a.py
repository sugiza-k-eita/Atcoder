a, b, c = map(int, input().split())
A = a**2
B = b**2
C = c**2

if A+B < C:
    print("Yes")
else:
    print("No")
