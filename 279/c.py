import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

H,W = MI()
s_box = []
t_box = []
for i in range(H):
    s = S()
    s_box.append(s)

for i in range(H):
    t = S()
    t_box.append(t)
    
l_2d_s = list(zip(*s_box))#転置された2次元配列s
l_2d_t = list(zip(*t_box))#転置された2次元配列t
l_2d_s.sort()
l_2d_t.sort()

for i in range(W):#転置後なので、行数はw
    if l_2d_t[i] != l_2d_s[i]:#行ごとに見ていき、一致していなかったら
        print("No")
        exit()
#すべて一致していたら
print("Yes")