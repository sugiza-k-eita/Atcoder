"""
数字の暗号は数字としてではなく、str型にしたほうが
処理が楽になることが多い。
今回、0000-9999の1万通りだけ調査すれば良いので、計算量の問題はない
数学的に解くのではなく、余事象について考える必要がある
競技プロは数学的な思考だけだと処理が大変になることがある。
そのため、いかに少ない手順で行えるかが重要。
今回であれば、
xが含まれている時点で跳ねる
oが含まれていない時点で跳ねる

残ったのが、ansになるという。
人間にはできない全探索をしている
アルゴリズムで基本になる考えは、flgによって条件をつけれるか
"""


S = input()
S = str(S)
Yes = []
No = []

for i in range(len(S)):
    if S[i] == "x":
        No.append(i)
    elif S[i] == "o":
        Yes.append(i)

ans = 0

for i in range(10000):
    s = str(i).zfill(4)
    flg = 0
    for no in No:
        if str(no) in s:
            flg = 1
    for yes in Yes:
        if str(yes) not in s:
            flg = 1

    if flg == 0:
        ans += 1


print(ans)
