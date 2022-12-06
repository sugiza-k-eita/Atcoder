import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

letter_s= S()
letter_t = S()

for i in range(len(letter_s)):
    if letter_s[i] == letter_t[i]:
        continue
    else:
        print(i+1)
        exit()
print(len(letter_t))