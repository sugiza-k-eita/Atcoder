import math
R, X, Y = map(int, input().split())
tmp_distance = X**2 + Y**2
distance = math.sqrt(tmp_distance)
if R > distance:
    print(2)
else:
    tmp = R
    count = 0
    while True:
        count += 1
        if distance <= R:
            break
        else:
            R += tmp

    print(count)
