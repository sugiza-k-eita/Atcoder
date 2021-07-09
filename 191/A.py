v, t, s, d = map(int, input().split())
del_from = v*t
del_to = v*s

if del_from <= d and d <= del_to:
    print("No")
else:
    print("Yes")
