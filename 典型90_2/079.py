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
図


そのため、右や下から編集しても、左のセルを変更する際に影響が出てしまう。
図
図

そこで、左上から順に更新をかけることにする。
これにより、一度操作したセルは、以降、値の変更は行われない
図

手順
左上から順に揃える
もし、A[i][j] == B[i][j]ならそのセルには操作をしない
(重要なのは、一度通り過ぎたセルには以降値の変更を行わない)
"""




