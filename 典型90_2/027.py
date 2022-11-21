import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
user_name_box = set()
for i in range(N):
    user_name = S()#文字列受け取り
    if user_name not in user_name_box:#既存のusernameでなければ
        print(i+1)#0はじまりなので、+1
        user_name_box.add(user_name)#既存のusernameboxにusernameを追加

"""
027 - Sign Up Requests （★2）
https://atcoder.jp/contests/typical90/tasks/typical90_aa
i日目現在、入力されたusernameが既存のusernameに含まれているかどうかを判別する必要があります。
しかし、毎回listの中に含まれているか判別すると、計算量がはO(N・N!)かかってしまいます。

Question ではどうするか？
これに関して、大事なのは既存のusernameには、順番や重複の情報を保つ必要がないということです。
そのため、setで既存のusername情報を管理し(user_name_box)、新規登録しようとしているusernameがuser_name_boxの中にあるかどうかで登録できるかを決めます。
"""