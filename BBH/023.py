import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

s = S()
box = ["dream", "dreamer", "erase", "eraser"]
r_box = []
for i in box:
    a = i[::-1]
    r_box.append(a)
# print(r_box)

s = s[::-1]
cnt = 0
# print(s)
while True:
    if cnt == len(s):
        break
    flg = 0
    # print(flg,cnt)
    for j in r_box:
        leng = len(j)
        if s[cnt:cnt+leng] == j:
            cnt += leng
            break
        else:
            flg += 1
        if flg == 4:
            print("NO")
            exit()
print("YES")