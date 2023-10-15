import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N,T = sys.stdin.readline().rstrip().split()
N = int(N)
ans = []

for i in range(N):
    letter = S()
    if len(letter) == len(T):
        if letter == T:#1
            # print(letter,i+1)
            ans.append(i+1)
    
        else:
            diff_count = sum([s != t for s, t in zip(letter, T)])
            if diff_count == 1:#4
                # print(letter,i+1)
                ans.append(i+1)


    elif len(letter) - len(T) == 1:
            if letter[:-1] == T:
                ans.append(i+1)
                continue

            for j in range(len(T)):
                if letter[j] != T[j]:
                    if letter[j+1:] == T[j:]:
                        ans.append(i+1)
                    break
    elif len(T) -len(letter) == 1:
            
            if T[:-1] == letter:
                ans.append(i+1)
                continue
            
            for j in range(len(letter)):
                if T[j] != letter[j]:
                    if T[j+1:] == letter[j:]:
                        ans.append(i+1)
                    break

print(len(ans))
ans.sort()
print(*ans, sep=" ")
