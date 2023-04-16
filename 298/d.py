MOD = 998244353 
Q = int(input())
num = 1
for i in range(Q):
    a = list(map(int, input().split()))
    if a[0] == 1:
        num = str(num)
        num += str(a[1])
        num = int(num)
    elif a[0] == 2:
        num= str(num)
        num = num[1:]#1:以降のものを1つずつコピーして渡すので、計算量はO(len(num-1))
        num = int(num)
    elif a[0] == 3:
        print(num%MOD)


from collections import deque

S = deque([1])
Q = int(input().strip())
MOD = 998244353
ans = 1

for _ in range(Q):
    q = list(map(int, input().strip().split()))
    if q[0] == 1:
        S.append(q[1])
        ans = (ans * 10 + q[1])#
        ans %=MOD
    elif q[0] == 2:
        x = S.popleft()
        ans -= pow(10, len(S), MOD) * x#繰り返し二乗法によってlogNで計算できる
    elif q[0] == 3:
        print(ans%MOD)


"""
D - Writing a Numeral 時間内に解けなかった・・・
https://atcoder.jp/contests/abc298/tasks/abc298_d

入力
Q:クエリの数
query:3つの処理内容

今回の問題、一見すぐ溶けそうですが、Qの制約が6x10^5であるため、クエリ1回にかかる時間を最低でもO(log(N))で行う必要があります。
クエリ1は元の数字を10倍し、新しく入力された値を足せばO(1)で計算でき、
クエリ3はMODで割るだけなので、O(1)でできます。
しかしクエリ2の処理で、文字列として考え先頭の文字を消したり、[:1]などで転記してしまうとTLEになってしまいます。
letter = letter[:1]の処理は1以降のものを1つずつコピーして渡すので、計算量はO(len(num-1))

TLEにしてしまったコード


そのため、どうにかしてクエリ2の処理を抑える必要があります。
ここで先頭の数字を消すという動作を言い換えて考えてみます。
先頭の数字を消す→現在の数列-現在の桁数×先頭の数字
ex)3141592 
3141592 - 30000000=141592
となり、先頭の数字を消すことに成功します。

今回、クエリ1,2の特徴は以下の通りなので
取り出しは先頭の数字
追加は末尾
dequeを用いることができます。これで先頭の数字を取り出すのをO(1)で行うことができます。
先頭の数字を取り出すことができたら、取り出す前の桁数にするように10を何回か書けたいのですが、その際に繰り返し二乗法(pow)を使用します。
繰り返し二乗法の詳しい説明は省きますが簡単に言うと、べき乗の計算をlog(N)で行うことができる計算方法です

これにより、10を(元の数列の桁数)回かけることができます
その後、元の数列-現在の桁数×先頭の数字を行うことで、実質的に先頭の数字を消すことができます
"""