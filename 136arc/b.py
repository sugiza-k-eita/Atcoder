import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
A = LI()
B = LI()

"""
そもそも出てくる数字の数が違ったら無理、
どちらかを固定して、片方の銭湯の数から順に合わせていく
そして、最後のN-2までやって最後の2が揃うかで判断する

その場所が0,1,2のどれかによって変わる

現在の位置から2こずつ前に行く
↓
0の場合、はそのまま
1の場合、入れ替えが起きる
"""
cnt = N
for i in range(N-3):
    for j in range(len(B)):
        if A[0] == B[j]:
            if j >= 2:
                if j %2 == 0:
                    B.pop(j)
                    A.pop(0)
                    break
                else:
                    B[0],B[1] = B[1],B[0]
                    B.pop(j)
                    A.pop(0)
                    break
            
            elif j == 0:
                    B.pop(0)
                    A.pop(0)
                    break
            elif j == 1:
                    B.pop(1)
                    A.pop(0)
                    B[0],B[1] = B[1],B[0]
                    break



    cnt -= 1
    # print(cnt,A,B)

if A == B:
    print("Yes")
elif A[0] == B[1] and A[1] == B[2] and A[2] == B[0]:
    print("Yes")
elif A[0] == B[2] and A[1] == B[0] and A[2] == B[1]:
    print("Yes")
else:
    print("No")
    
