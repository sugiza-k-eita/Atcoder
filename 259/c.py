import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

s = S()
T = S()
cnt = 0
len_T =len(T)


letter = "@"
for i in range(len_T):  
    if i-cnt < len(s):        
        if T[i] == s[i-cnt]:
            continue
        else:
            if s[i-cnt-2] ==s[i-cnt -1]:
                letter = s[i-cnt-2]
            
            if letter == T[i]:
                cnt += 1
            
            else:
                print("No")
                exit()
    else:
        if s[-2] == s[-1]:
            letter = s[-1]
        else:
            print("No")
            exit()
            
        if T[i] == letter:
            continue
        else:
            print("No")
            exit()

print("Yes")