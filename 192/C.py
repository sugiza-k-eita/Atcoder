def g1(N):
    N = str(N)
    N = sorted(N, reverse=True)
    res = "".join(N)
    res = int(res)
    return res
    # 文字列にすることで数字を1文字ずつに分ける
    # その後、ソートして、もう一度int型に変換する


def g2(N):
    N = str(N)
    N = sorted(N)
    res = "".join(N)
    res = int(res)
    return res


N, K = map(int, input().split())

table = [0] * (K + 1)
# i回目に実行したfの結果をtable[i]に格納する
table[0] = N
for i in range(1, K+1):
    table[i] = g1(table[i-1]) - g2(table[i-1])
    if i == K:
        print(table[i])
if K == 0:
    print(table[0])
