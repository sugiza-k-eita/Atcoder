N,S = map(int, input().split())

dp = [[False]*(S+1) for i in range(N)]

A_box = []
B_box = []
for i in range(N):
    A,B = map(int, input().split())
    A_box.append(A)
    B_box.append(B)


for i in range(N):
    A,B = A_box[i],B_box[i]
    if i == 0:
        dp[i][A] = True
        dp[i][B] = True
    else:
        for j in range(A,S+1):
            if dp[i-1][j-A] ==True:
                dp[i][j] = True
    
        for j in range(B,S+1):
            if dp[i-1][j-B] ==True:
                dp[i][j] = True

if dp[-1][-1] == False:
    print("Impossible")
    exit()

ans = []
now = S
# for x in dp:
#     # print(x)

for i in range(N-1,-1,-1):
    if now - A_box[i] >= 0 and dp[i-1][now - A_box[i]]:
        ans.append("A")
        now -= A_box[i]
    else:
        ans.append("B")
        now -= B_box[i]
    # print(now,i)
print(*ans[::-1],sep="")
"""
・問題文 
デパートの高橋屋では、 N 日にわたって初売りが行われます。 i ( 1≤i≤N) 日目には、 A_i 円の福袋 A と B_i円の福袋 B が売られます。 低橋くんは N 日間、毎日高橋屋に通って福袋 A または福袋 B のいずれかを購入します。（なにも購入しないことはできません。） N 日間で購入した N 個の福袋の総額がちょうど S 円になるように購入したいです。 低橋くんは計算が苦手なので、あなたが代わりに条件を満たす福袋の購入の計画を立ててください。 そのような購入の計画が存在しない場合は、それを報告してください。

・pythonコード
N,S = map(int, input().split())

dp = [[False]*(S+1) for i in range(N)]

A_box = []
B_box = []
for i in range(N):
    A,B = map(int, input().split())
    A_box.append(A)
    B_box.append(B)


for i in range(N):
    A,B = A_box[i],B_box[i]
    if i == 0:
        dp[i][A] = True
        dp[i][B] = True
    else:
        for j in range(A,S+1):
            if dp[i-1][j-A] ==True:
                dp[i][j] = True
    
        for j in range(B,S+1):
            if dp[i-1][j-B] ==True:
                dp[i][j] = True

if dp[-1][-1] == False:
    print("Impossible")
    exit()

ans = []
now = S
# for x in dp:
#     # print(x)

for i in range(N-1,-1,-1):
    if now - A_box[i] >= 0 and dp[i-1][now - A_box[i]]:
        ans.append("A")
        now -= A_box[i]
    else:
        ans.append("B")
        now -= B_box[i]
    # print(now,i)
print(*ans[::-1],sep="")

・盛り込みたい内容
動的計画法(DP)で解ける
その後、DP復元を行います。

手順
そもそもN日間でS円分の買い物できるかを検証
できるのなら、どうゆう順番で買えばいいか探索

まず1日目において、A1円の福袋とB2円の福袋が与えられるので、
dp[i][A1] = True
dp[i][B1] = True
となる。

2日目は、A1円の福袋とB2円の福袋が与えられるので、
dp[i][A1+A2] = True
dp[i][B1+B2] = True
です。
つまり、0からSまでのjにおいて、dp[i-1][j] == Trueであれば、
dp[i][j+A2]
dp[i][j+B2]
となり、漸化式で表現できます。

上記のようにN日間行い、結果的に
dp[N][S] == Trueであれば、N日目までにS円分の買い物ができたことになります。

できるのなら、どうゆう順番で買えばいいか探索
DP復元では、S日目から0日目まで遡りながら実装していけば大丈夫です。
dp[N][S] == Trueということは、
dp[N-1][S-An-1] == True or dp[N-1][S-Bn-1]ということです。
そして、
dp[N-1][S-An-1] ==True なら
dp[N-1][S-(An-1+An-2)] ==True or dp[N-1][S-(An-1+Bn-2)] ==Trueということになります。
つまり、こちらに関しても漸化式で表現できますので、逆順にdpを行えます。
"""