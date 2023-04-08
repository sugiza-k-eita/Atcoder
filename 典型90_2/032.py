import itertools

N = int(input())
A = []#i番目に入力された人のj区目を走るときのタイムを記憶
for i in range(N):
    a = list(map(int, input().split()))
    A.append(a)

M = int(input())
bad_friends = [[] for i in range(N)]#i番目のリストにi番目の人と不仲の人を格納
for j in range(M):
    x,y = map(int, input().split())
    x -= 1#0-indexにするため-1
    y -= 1#0-indexにするため-1

    bad_friends[x].append(y)#x番目のリストに、不仲の人yを格納
    bad_friends[y].append(x)#y番目のリストに、不仲の人xを格納

ans = 10**18#初期値
number = [i for i in range(N)]#ランナーの人数

for p in itertools.permutations(number):#走る順番の並び替えを作る
    runner_time = 0#タイムを記憶
    cnt = 0#何人走ったかをカウント
    for i in range(N-1):#たすきを渡す回数
        runner = p[i]#i区目を走る人
        nxt_runner =p[i+1]#i+1区を走る人
        runner_time += A[runner][i]#i区目を走る人のタイム
        if nxt_runner not in bad_friends[runner]:#もしi+1区目を走る人が、i区目を走る人の不仲リストに入ってなければ
            cnt += 1#たすきを繋ぐ事ができる
    if cnt == N-1:#最後の走者までたすきをつなげたら
        runner_time += A[p[N-1]][N-1]#最後の走者のタイムを足す
        ans = min(ans,runner_time)#完走したときのタイムの最小値を記憶

if ans == 10**18:
    print(-1)#初期値が変わらない=どの並び替えでも完走できなかったのなら
else:#一回でも完走できたなら
    print(ans)


"""
032 - AtCoder Ekiden（★3）
https://atcoder.jp/contests/typical90/tasks/typical90_af

今回 Nが10以下です。そのため、N人の走順の並び替えをすべて試しても、十分に間に合います
※最大で10!(=3628800)で、10^7以下のため

そのため、ありうる走順をすべて試し、i番目に走る人とi+1番目に走る人の不仲なら、そのループをブレイク(破棄)すれば良いです
そして、N人走る切ることのできた走順の中で最小のもとを出力します。
"""