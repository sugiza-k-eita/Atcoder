# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_B&lang=ja
# 1 から n までの数の中から、重複無しで３つの数を選びそれらの合計が x となる組み合わせの数を求めるプログラムを作成して下さい。

# 例えば、1 から 5 までの数から３つを選んでそれらの合計が 9 となる組み合わせは、

# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# の２通りがあります。

while True:
    N, X = map(int, input().split())
    cnt = 0
    if N == 0 and X == 0:
        break
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            for k in range(j+1, N+1):
                if i+j+k == X:
                    cnt += 1
    print(cnt)
