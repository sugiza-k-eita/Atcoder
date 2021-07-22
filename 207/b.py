a, b, c, d = map(int, input().split())
box1 = a
box2 = 0
count = 0
while True:
    if b >= d*c:
        count = -1
        break
    elif box1 > box2*d:
        box1 += b
        box2 += c
        count += 1
    else:
        break

print(count)
