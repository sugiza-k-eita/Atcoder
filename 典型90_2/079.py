"""
問題文 H×W の 2 次元配列 A が与えられます。あなたは以下の 2 種類の操作を好きな順番で何度でも行うことが出来ます。 整数 x,y (1≤x<H,1≤y<W) を選び、 A x,y ​ ,A x+1,y ​ ,A x,y+1 ​ ,A x+1,y+1 ​ の値をそれぞれ 1 ずつ増やす。 整数 x,y (1≤x<H,1≤y<W) を選び、 A x,y ​ ,A x+1,y ​ ,A x,y+1 ​ ,A x+1,y+1 ​ の値をそれぞれ 1 ずつ減らす。 操作を 0 回以上行うことで A を B に一致させることは可能でしょうか。 もし可能ならば、最小の操作回数も答えてください。
"""

H,W = map(int, input().split())

A = []
B = []
for i in range(H):
    w = list(map(int, input().split()))
    A.append(w)

for i in range(H):
    w = list(map(int, input().split()))
    B.append(w)

cnt = 0
for i in range(H-1):
    for j in range(W-1):
        if A[i][j] == B[i][j]:
            continue
        
        elif A[i][j] > B[i][j]:
            diff = A[i][j] - B[i][j]
            for k in range(2):
                for l in range(2):
                    A[i+k][j+l] -= diff
            cnt += abs(diff)
        
        elif A[i][j] < B[i][j]:
            diff = A[i][j] - B[i][j]
            for k in range(2):
                for l in range(2):
                    A[i+k][j+l] -= diff
            cnt += abs(diff)


if A == B:
    print("Yes")
    print(cnt)
else:
    print("No")


"""

今回、一つのセルを更新したいときに影響が出るセルはそのセルを左上とした時、右上、左下、右下の3つ
xx1
xx1
111


そのため、右や下から編集しても、左のセルを変更する際に影響が出てしまう。
[3,3]を更新
111
1xx
1xx
↓
[3,2]を更新
1xx



そこで、左上から順に更新をかけることにする。
これにより、一度操作したセルは、以降、値の変更は行われない
図

手順
左上から順に揃える
もし、A[i][j] == B[i][j]ならそのセルには操作をしない
(重要なのは、一度通り過ぎたセルには以降値の変更を行わない)
"""




