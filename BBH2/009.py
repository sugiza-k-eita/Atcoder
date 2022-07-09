import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N,M = MI()
A = []
B = []
for i in range(N):
    a = S()
    A.append(a)

for j in range(M):
    b = S()
    B.append(b)
    

for i in range(N):
    for j in range(N):
        cnt = 0
        for p in range(M):
            for q in range(M):
                if i+p >= N or j+q >= N:
                    break
                
                if A[i+p][j+q] == B[p][q]:
                    cnt += 1
        if cnt == M*M:
            print("Yes")
            exit()
print("No")
                    
                
        



"""
B - Template Matching 
https://atcoder.jp/contests/abc054/tasks/abc054_b

今回は、M <= N <= 50なので、
A絵画の縦と横、B絵画の縦と横について全探索することが可能です
O(50^4)
なので、全探索します。
まずはじめにA絵画とB絵画の右上を揃えます。i,j
そこから、B絵画の要素がA絵画要素と同じか確認します(p,q)

イメージ
A[i][j]にBの絵画の左上を揃える
そこから、Bの絵画は、右にp,下にqの要素についてみる
その際、Aの絵画もBが移動した分だけ見る場所をかえるから、A[i+p][j+q]の要素をみる
"""