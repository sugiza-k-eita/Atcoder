N = int(input())
letter = input()

okcnt = 0
for i in range(N):
    if letter[i] == "o":
        okcnt += 1
    elif letter[i] == "x":
        print("No")
        exit()

if okcnt > 0:
    print("Yes")
else:
    print("No")
"""
A - Job Interview
https://atcoder.jp/contests/abc298/tasks/abc298_a

入力
N:文字列の長さ
S:文字列

今回条件はxがあった瞬間に一発アウトで、また合格するには文字列を最後まで見たときにoが一個以上ある必要があります


そのため、事前にoの数をカウントするflgを用意し、
文字列を0文字目から見ていったときに、
xがあった瞬間Noを出力しプログラムを週力
oがあれが+1
for文が終わったときに、oの数が1以上ならYes,oの数が0ならNoを出力します
"""