import sys

def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()


s = S()

l, r = 0, len(s)-1
ans = 0

while l < r:
    if s[l] == s[r]:
        l += 1
        r -= 1
        continue
    
    ans += 1
    if s[l] == 'x':
        l += 1
    elif s[r] == 'x':
        r -= 1
    else:
        print(-1)
        exit()

print(ans)