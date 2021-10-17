from collections import deque


N = int(input())
ns = list(map(int, input().split()))

survive = deque(range(0, 2**N))

for i in range(N-1):
    winner = deque()
    # print(winner)
    while survive:
        player1 = survive.popleft()
        player2 = survive.popleft()
        if ns[player1] > ns[player2]:
            winner.append(player1)
        else:
            winner.append(player2)
    survive = winner

player1 = survive.popleft()
player2 = survive.popleft()

if ns[player1] > ns[player2]:
    print(player2+1)
else:
    print(player1+1)
