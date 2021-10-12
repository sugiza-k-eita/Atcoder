import itertools


N, M = map(int, input().split())
hands = []
for i in range(2*N):
    S = input()
    hands.append(S)

rank = [[1000, 0] for i in range(N*2)]
# 1000はrate, 0はplayerのID
for i in range(N*2):
    rank[i][1] = i
# print(rank)


def judge(a, b):
    # 引き分けなら0,前者勝ちなら1,後者勝ちなら-1
    if a == b:
        return 0
    if a == 'G' and b == 'C':
        return 1
    if a == 'C' and b == 'P':
        return 1
    if a == 'P' and b == 'G':
        return 1
    else:
        return -1


for j in range(M):
    for i in range(N):
        player1 = rank[2*i][1]
        player2 = rank[2*i+1][1]
        # player番号を付与
        if judge(hands[player1][j], hands[player2][j]) == 1:
            # player1のj番目の手とplayer2のj番目の手
            # player1が勝ったら
            rank[2*i][0] -= 1
            # print(rank[2*i][1]+1)
            # rateが下がる　今回はrateが低いほど強い
        elif judge(hands[player1][j], hands[player2][j]) == -1:
            rank[2*i+1][0] -= 1
            # print(rank[2*i+1][1]+1)
    rank.sort()
# print(rank)
for i in range(2*N):
    print(rank[i][1]+1)
