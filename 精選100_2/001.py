import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

#N == 300なので、for文は3周できる
#重複なしなので、i < j < k <= 300となるようにfor文を作成
while True:
    N,X = MI()
    if N == 0 and X == 0:
        exit()
    
    ans = 0
    #最終的にプリントする 条件を満たす数を記録する
    for i in range(1,N+1):
        for j in range(i+1, N+1):
            for k in range(j+1, N+1):
                if X == i + j + k:
                    ans += 1
    print(ans)
            
