from collections import Counter
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

#できるときではなく、できないときを尺取法で取る
N,K = MI()
ns = LI()

#数列Aに対して、何番目から何番目の累積和がK以上か
def syakutori1(N,K,A):
    left = 0
    x = 0
    #xは一時的な累積和
    cnt = 0
    #最初は左端からはじめて
    for right in range(N):
        x += A[right]
        while x >= K:
            #超えたら、回数をカウント
            #↓現在地はrであとN-r回移動できる　現在Kを超えていてN-r回移動しても大きくなるだけ
            #つまり現在地からN-r回はKよりも大きい累積和がある
            cnt += N-right
            #超えたらl（左端）が一つ右にずれる
            x -=A[left]
            left += 1
    return cnt
ans=syakutori1(N,K,ns)