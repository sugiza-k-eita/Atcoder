import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N,M = MI()
A = [[None] for i in range(N)]
B = [[None] for i in range(M)]
for i in range(N):
    ns = S()
    A[i] = ns

for i in range(M):
    ns = S()
    B[i] = ns
cnt = 0
flg = False
for i in range(N+1-M):
    for j in range(N+1-M):
        if A[i][j] == B[0][0]:
            for k in range(M):
                for l in range(M):
                    if A[i+k][j+l] == B[k][l]:
                        cnt += 1
                    else:
                        flg = True
                        break

                    if cnt == M*M:
                        print("Yes")
                        exit()
                if flg:
                    # print(i+k,j+l,k,l)
                    flg = False
                    cnt =0
                    break
        else:
            continue


print("No")