import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N = II()
s = S()
left_cnt = 0
right_cnt = 0

ans = []
for i in range(N):
    if s[i] == "(":
        left_cnt += 1
        ans.append("(")
    else:
        right_cnt += 1
        ans.append(")")
        if right_cnt > left_cnt:
            while True:
                if right_cnt == left_cnt:
                    right_cnt = 0
                    left_cnt = 0
                    break
                ans.insert(0,"(")
                left_cnt += 1
if left_cnt > right_cnt:
    for i in range(left_cnt-right_cnt):
        ans.append(")")
print(*ans, sep = "")

            