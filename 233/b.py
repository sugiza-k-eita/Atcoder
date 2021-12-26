import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

L,R = MI()
s = S()

L -= 1
R -= 1

head = s[:L]
reverse = s[L:R+1]
reverse = reverse[::-1]
tail = s[R+1:]

print(head+reverse+tail)

