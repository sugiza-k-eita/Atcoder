import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

s = S()
t = S()
lens =len(s)
lent = len(t)

a = s[::-1]
b = t[::-1]
boxs = []
boxt = []
for x in a:
    boxs.append(x)
for x in b:
    boxt.append(x)

cnt = 0
for i in range(lens-lent+1):
    cnt = 0
    for j in range(lent):
        if boxs[i+j] == boxt[j] or boxs[i+j] == "?":
            cnt += 1
    
            if cnt == lent:
                for x in range(lent):
                    boxs[i+x] = boxt[x]
                boxs.reverse()
                for i in range(lens):
                    if boxs[i] == "?":
                        boxs[i] = "a"
                print(*boxs, sep="")
                exit()
        else:
            break
print("UNRESTORABLE")