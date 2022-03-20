import sys
def LI(): return list(map(str,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

s = S()
t = S()
letter = ["R G B","R B G","B R G", "B G R", "G B R","G R B"]
s_ind = letter.index(s)
t_ind = letter.index(t)

box = [[1,3,5],[0,2,4],[1,3,5],[2,4,0],[3,5,1],[4,0,2]]
if t_ind in box[s_ind]:
    print("No")
else:
    print("Yes")