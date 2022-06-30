import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

s = S()
ans = [0]*len(s)
cnt = 0
gather_range = [0,0]
next_range = [len(s),len(s)]
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        cnt += 1
        
    elif s[i] == "R" and s[i+1] == "L":
        if i%2 == 0:
            even_gather_point = i
            odd_gather_point = i+1
            cnt += 1
        else:
            even_gather_point = i + 1
            odd_gather_point = i
            cnt += 1
    
    elif s[i] == "L" and s[i+1] == "R":
        gather_range[1] = i
        next_range[0] = i+1
        cnt += 1
        
        if cnt %2 == 0:
            ans[even_gather_point] =cnt//2
            ans[odd_gather_point] =cnt//2
        else:
            if gather_range[0] %2 == 0:
                ans[even_gather_point] =cnt//2+1
                ans[odd_gather_point] = cnt//2
            else:
                ans[even_gather_point] =cnt//2
                ans[odd_gather_point] = cnt//2 + 1
        
        gather_range[0] = next_range[0]
        cnt = 0


cnt +=1#末尾のLをカウント
if cnt %2 == 0:
    ans[even_gather_point] =cnt//2
    ans[odd_gather_point] =cnt//2
else:
    if gather_range[0] %2 == 0:
        ans[even_gather_point] =cnt//2+1
        ans[odd_gather_point] = cnt//2
    else:
        ans[even_gather_point] =cnt//2
        ans[odd_gather_point] = cnt//2 + 1
    



print(*ans, sep=" ")

"""
01010 101 01010101
RRRLL RLL RRRLLLLL
00320 210 00440000
"""