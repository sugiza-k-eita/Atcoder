import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N,K = MI()
A = LI()
cnt = 0
ruiseki= [0]#0番目に0を入れておく
for i in range(N):
    num = ruiseki[-1] + A[i]#一つ前の累積和+今回の足した数
    ruiseki.append(num)



l = 0#始点
r = 0#終点

cnt = [0]* (N+1)
#そこが終点になったことによって、部分数列の和がKを初めて超えた回数

while r < N+1:
    if ruiseki[r] -ruiseki[l] >= K:#累積和がK以上になったら
        cnt[r] += 1
        l += 1
        #始点を右に動かし、部分数列の範囲を広げる
    else:#累積和がK未満になったら
        r += 1
        #終点を右に動かし、部分数列の範囲を広げる
    if r > N:
        break
    

for i in range(1,N+1):
    cnt[i] += cnt[i-1]
print(sum(cnt))