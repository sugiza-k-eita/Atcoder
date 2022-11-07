import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
A = LI()

def two_by_three(x):
    two_cnt = 0
    three_cnt = 0
    while x%2==0 or x%3 == 0:
        if x%2 == 0:
            x//=2
            two_cnt += 1
        if x%3 == 0:
            x//=3
            three_cnt += 1
    return x,two_cnt,three_cnt

box = []
two_box = []
three_box = []
ans = 0
for i in range(N):
    x,two,three = two_by_three(A[i])
    box.append(x)
    two_box.append(two)
    three_box.append(three)
    ans += two
    ans += three

if len(set(box)) != 1:
    print(-1)
    exit()

two_box.sort()
min_two = two_box[0]
three_box.sort()
min_three = three_box[0]
print(ans - min_two*N -min_three*N)