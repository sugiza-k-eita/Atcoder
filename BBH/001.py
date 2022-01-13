import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

box = S()
index = [0,]
check = []
ans = [0 for i in range(len(box))]
Even_cnt = 0
Odd_cnt = 0
gather = 0


for i in range(len(box)-1):
    if box[i] == box[i+1]:
        if i%2 == 0:
            Even_cnt += 1
        else:
            Odd_cnt += 1
    elif box[i] == "R" and box[i+1] == "L":
        gather = i
        if i%2 == 0:
            Even_cnt += 1
            flg = True
        else:
            Odd_cnt += 1
            flg = False
    
    elif box[i] == "L" and box[i+1] == "R":
        if i%2 == 0:
            Even_cnt += 1
        else:
            Odd_cnt += 1
        
        if flg:
            ans[gather] = Even_cnt
            ans[gather+1] = Odd_cnt
        else:
            ans[gather] = Odd_cnt
            ans[gather+1] = Even_cnt
        
        Odd_cnt = 0
        Even_cnt = 0

if (len(box)-1) %2 == 0:
    Even_cnt += 1
else:
    Odd_cnt += 1

if flg:
    ans[gather] = Even_cnt
    ans[gather+1] = Odd_cnt
else:
    ans[gather] = Odd_cnt
    ans[gather+1] = Even_cnt

print(*ans,sep = " ")
