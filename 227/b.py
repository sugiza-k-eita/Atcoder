import sys
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())


N = II()
people = LI()
cnt = 0
for i in range(N):
    flg = 0
    for a in range(1, 143):
        for b in range(1, 143):
            tmp_ans1 = 4*a*b
            tmp_ans2 = 3*(a+b)
            ans = tmp_ans1+tmp_ans2
            if ans == people[i]:
                cnt += 1
                flg = 1
                break
        if flg == 1:
            break
print(len(people)-cnt)
