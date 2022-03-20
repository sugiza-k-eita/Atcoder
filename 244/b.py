import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
T = S()

x = 0
y = 0
flg = ["r","d","l","u"]
flg_cnt = 0

for i in range(N):
    if T[i] == "S":
        if flg_cnt % 4 == 0:
            x += 1
        elif flg_cnt % 4 == 1:
            y -= 1
        elif flg_cnt % 4 == 2:
            x -= 1
        elif flg_cnt % 4 == 3:
            y += 1
    else:
        flg_cnt += 1

print(x, y)