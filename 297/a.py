N,D = map(int, input().split())
T = list(map(int, input().split()))

for i in range(1,N):#2回目からN回目の操作において
    if T[i]-T[i-1] <=D:#i回目とi-1回目の時間の差がD以下であれば
        print(T[i])
        exit()
print(-1)#ダブルクリックが一度も行われていなければ

"""
A - Double Click
https://atcoder.jp/contests/abc297/tasks/abc297_a
入力
N : クリック回数
D : ダブルクリックが成功したかの基準の時間
A[i] : i回目にクリックした時刻

N回の操作のうち、i回目のタイムとi-1回目のタイムの差がT秒以下だったら試行i回目のタイムを出力すれば良いです
そのため、2回目からN回目の操作において、現在の時刻と1つ前の時刻の差分を取り、Dと比べれることで答えにたどり着けます
"""