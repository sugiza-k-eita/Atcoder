import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
letter = S()
dp = [[0]*7 for i in range(N)]
sample = "atcoder"

if letter[0] == "a":
    dp[0][0] = 1

for i in range(N):
    if letter[i] == "a":
        dp[i][0] = dp[i-1][0]+1
    else:
        dp[i][0]= dp[i-1][0]

mod = 10**9+7
for i  in range(1,N):
    for j in range(1,7):
        if letter[i] == sample[j]:
            dp[i][j] = dp[i-1][j]+dp[i][j-1]
        else:
            dp[i][j] = dp[i-1][j]
        dp[i][j] %= mod
# for x in dp:
#     print(x)
print(dp[-1][-1])

"""
atcoderとなるような文字列を作成するには・・・
i-1番目までに「atcode」 という文字列が作成可能である場合、i番目の文字列が「r」だと作成できる

では、atcodeという文字列を作成するには・・・
i-1番目までに「atcod」 という文字列が作成可能である場合、i番目の文字列が「e」だと作成できる

では、atcodという文字列を作成するには・・・
となります。

このことから何が言えるかと言うと、
文字列Sのi文字目がatcoderという文字列のj文字目の場合
j文字目まで完成している通り数 = j-1文字目まで完成している通り数
となります。

今回の問題のように、前の状態によって今の状態が決まる問題の多くは動的計画法で実装できます。

今回管理しなきゃいけないのは、
文字列S*7(len(atcoder))のdpを管理しなければなりません。

もし、文字列Sのi文字目がatcoderという文字列のj番目の場合
dp[i][j] += dp[i-1][j-1]となり、
そうではない場合は、
dp[i][j] += dp[i-1][j]+1 となる
(今回は貰う方のdpで実装してますが、E869120さんは配るdpで解説してます)

"""