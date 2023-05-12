import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = II()
letter = S()

cnt = 0
for i in range(N):
    if letter[i] == "|":
        cnt += 1
    if letter[i] == "*" and cnt == 0:
        print("out")
        exit()
    elif letter[i] == "*" and cnt == 2:
        print("out")
        exit()
print("in")
