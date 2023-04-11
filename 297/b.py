s = input()

check =0#Bの偶奇をチェックする
for i in range(8):
    if s[i] == "B":
        check += i
if check %2 == 0:
    print("No")
    exit()

king = 100#後に更新される　適当な数字
R = []
for i in range(8):
    if s[i] == "K":
        king = i#Kの座標を取得
    if s[i] == "R":#Rの座標を取得
        R.append(i)

import bisect

a = bisect.bisect_left(R,king)#kingを挿入する際に何番目に挿入されるか
if a == 1:#挿入される場所が1なら
    print("Yes")
else:
    print("No")

"""
B - chess960
https://atcoder.jp/contests/abc297/tasks/abc297_b
入力
S : 長さ8の文字列

今回の問題では、
Bの偶奇が異なること
Kと2つのRの位置関係がRKRのようにKがRに挟まれていること
の2条件が挙げられます。

1つ目の条件については、2つのBの位置の和が奇数なら条件を満たします
(偶数+偶数=偶数,奇数+奇数=偶数のため)

2つ目の条件については、Kの座標をintで取得し、と2つのRの座標をリストで取得し、
Kを挿入する際のインデックスが1であることを確かめれば良いです。
ind   0 1 2
list [R K R]
"""