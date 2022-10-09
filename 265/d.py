import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N,P,Q,R = MI()
A = LI()
cnt  =  P+Q+R
ruiseki = [0]

for i in A:
    ruiseki.append(ruiseki[-1]+i)


def syakutori1(K,A,left,right):
    box = []
    #Nが繰り返す回数
    #Kがcnt or P or Q or R
    # left,rightは累積和の計算をする範囲
    #最初は左端からはじめて
    while right < len(ruiseki)-1:
        if K == ruiseki[right] - ruiseki[left]:
            box.append([left,right])
            left += 1
            right += 1

        elif K > ruiseki[right] - ruiseki[left]:
            right += 1
        elif K < ruiseki[right] - ruiseki[left]:
            left += 1
    return -1,-1

l = 0
r = 1
while r < len(ruiseki)-1:
    l2,r2 = syakutori1(P,A,l,r)
    r += 1
    if l2 != -1:
        l3,r3 = syakutori1(Q,A,r2,r2+1)
        if l3 != -1:
            l4,r4 = syakutori1(R,A,r3,r3+1)
            if l4 != -1:
                print("Yes")
                exit()
            else:
                continue
        else:
            continue
    else:
        continue

print("No")
