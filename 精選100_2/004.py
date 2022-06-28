import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


from itertools import combinations
# 高校数学で習う　nCrをやってくれるライブラリ


N,M = MI()
box = []
#まずはじめに空の箱を作ります
#boxの中にAという1次元のリストをN個入れていくので、boxは二次元配列のリストになります
for i in range(N):
    A = LI()
    box.append(A)

#box[i][j] は　i番目の人がj番目の曲を歌ったときの点数です

total = 0
for j in combinations(range(M), 2):
    #M個の中から2個を選ぶ全パターンを探索
    t1,t2 = j[0],j[1]
    #t1,t2は曲番号です
    score = 0
    #今回の試行でN人の人が取る点数を0に初期化
    for i in range(N):
        score += max(box[i][t1], box[i][t2])
        #選ばれた2曲の内高い人をその人の点数
    total = max(total, score)

print(total)