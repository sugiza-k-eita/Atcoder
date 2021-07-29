n = int(input())
S = input()
Q = int(input())
head = list(S[:n])
tail = list(S[n:])
table = [head, tail]


def change(x):
    if x < n:
        return 0, x

    else:
        return 1, x-n


for i in range(Q):
    t, a, b = map(int, input().split())
    a -= 1
    b -= 1

    if t == 1:
        right1, right2 = change(a)
        left1, left2 = change(b)
        table[right1][right2], table[left1][left2] = table[left1][left2], table[right1][right2]
    else:
        table[0], table[1] = table[1], table[0]
    # print(table)
ans = "".join(table[0]) + "".join(table[1])
print(ans)
