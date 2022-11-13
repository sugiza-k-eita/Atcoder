import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N,M = MI()
A = LI()
B = []
sum_count = sum(A)#Aの合計値を取得
A.sort()

pre = 0
for i in range(N):
    if A[i] - A[i-1] > 1:#連続していない→切れ目の部分なら
        pre = i#切れ目として記憶
        break
minus = 0#場に捨てることのできる数字の和を記憶
tmp = 0#一時的に記憶させておくための変数
for i in range(N):
    now = (pre+i)%N#indexエラーにならないように
    if (A[now]-A[(now-1)]) % M > 1:#現在の数字が一つ前の数字と比べ、差が1以上なら
        minus = max(minus,tmp)#これ以上捨てれる区間は伸びないので、本区間で捨てた数字とこれまでの区間で捨てた最大値を取る
        tmp = 0#一次保存は最初から
    tmp += A[now]#現在の数字からまた捨てる区間を開始

minus = max(minus,tmp)#for文が終わったあとに、tmpとminusを比べ大きい方と取る、
print(sum_count - minus)#全体の合計から場に捨てることのできる最大の数値で引く