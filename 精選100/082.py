import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
m=24*60*60
while True:
    N = II()
    box = [0]*(m+1)
    if N == 0:
        break
    for i in range(N):
        a,d=input().split()
        a,b,c=map(int,a.split(':'))
        d,e,f=map(int,d.split(':'))
        box[a*3600+b*60+c]+=1
        box[d*3600+e*60+f]-=1
    for i in range(m):
        box[i+1]+=box[i]
    print(max(box))