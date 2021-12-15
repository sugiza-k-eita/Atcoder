#サンプルデータではあっていたが、テストデータはMLE
#メモリーエラーで通らない

import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()


box = []
Odd_box = []
for i in range(1,181):
    flg = i*(i+1)*(i+2)//6
    box.append(flg)
    if flg %2 == 1:
        Odd_box.append(flg)
# print(box[:5])
# print(Odd_box[:5])
while True:
    N = II()
    if N == 0:
        break
    dp= [[0]*(N+1) for i in range(len(box))]
    Odd_dp= [[0]*(N+1) for i in range(len(Odd_box))]


    for j in range(N+1):
        dp[0][j]=j
        Odd_dp[0][j] = j

    for i in range(1,len(box)):
        for j in range(1,N+1):
            if box[i] <= j:
                dp[i][j] = dp[i][j-box[i]]+1
            else:
                dp[i][j] = dp[i-1][j]


    for i in range(1,len(Odd_box)):
        for j in range(1,N+1):
            if Odd_box[i] <= j:
                Odd_dp[i][j] = Odd_dp[i][j-Odd_box[i]]+1
            else:
                Odd_dp[i][j] = Odd_dp[i-1][j]

    # for xxx in Odd_dp:
    #     print(xxx)

    ans = N
    for xx in dp:
        ans = min(xx[-1],ans)
    Odd_ans = N
    for odd in Odd_dp:
        Odd_ans = min(odd[-1],Odd_ans)
    print(ans, Odd_ans)
