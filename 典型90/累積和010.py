N = int(input())
room1 = [[0, 0] for i in range(N+1)]
room2 = [[0, 0] for i in range(N+1)]
for i in range(1, N+1):
    c, p = map(int, input().split())
    if c == 1:
        room1[i][1] = p
        room1[i][0] = room1[i-1][0] + p
        room2[i][0] = room2[i-1][0]
    else:
        room2[i][1] = p
        room2[i][0] = room2[i-1][0] + p
        room1[i][0] = room1[i-1][0]

# print(room1)
# print(room2)
Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())
    l -= 1
    score1 = room1[r][0] - room1[l][0]
    score2 = room2[r][0] - room2[l][0]
    print(score1, score2)
