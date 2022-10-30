from collections import defaultdict
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
import bisect

H,W = MI()

d = defaultdict(int)
for i in range(H):
    A = S()
    for a in A:
        d[a] += 1

box = []
for item in d:
    cnt = d[item]
    box.append(cnt)

box.sort()
four_letter_cnt = 0
two_letter_cnt = 0
one_letter_cnt = 0
if H%2 == 0 and W%2==0:
    four_letter_cnt = (H*W)//4
elif H%2 == 0:
    four_letter_cnt = (H*(W-1))//4
    two_letter_cnt = H//2
elif W%2 == 0:
    four_letter_cnt = (W*(H-1))//4
    two_letter_cnt = W//2
else:
    four_letter_cnt = (H-1)*(W-1)//4
    two_letter_cnt = (H+W-2)//2
    one_letter_cnt = 1



while four_letter_cnt != 0:
    ind = box.pop(-1)
    ind -= 4
    four_letter_cnt -= 1
    if ind < 0:
        print("No")
        exit()
    bisect.insort(box,ind)

while two_letter_cnt != 0:
    ind = box.pop(-1)
    ind -= 2
    two_letter_cnt -= 1
    if ind < 0:
        print("No")
        exit()
    bisect.insort(box,ind)

while one_letter_cnt != 0:
    ind = box.pop(-1)
    ind -= 1
    one_letter_cnt -= 1
    if ind < 0:
        print("No")
        exit()
    bisect.insort(box,ind)
print("Yes")

"""
1*Nのときの回文は
abccba　のようにすべての文字が2かいずつ使われるパターン
abcba　のように1つの文字以外が2かいずつ使われるパターンの2パターンがある
なぜこのような条件分岐が生まれるかとうと、Nの偶奇が原因である。
N % 2 == 0のときは、すべての文字の種類が偶数回しようされる
N % 2 == 1のときは、1種類の文字が奇数回使われ、それ以外は偶数回しようされる

では、2次元の場合は？

NもMの偶数の場合
abba
cddc
cddc
abba のようにすべての文字の種類が4の倍数回ずつ使用される

aba
cdc
aba のように1種類の文字が奇数回使用され、(N+M-2)//2の種類の文字が2の倍数回使用され、それ以外の文字が4の倍数回使用される

abba
cddc
abba のようにNとMのうち、偶数である数の1/2の種類の文字が2の倍数回使用され、それ以外の文字が4の倍数回使用される


そのため、上記の条件を満たす場合のみ、2次元の回文が作成でき、それ以外は作成できない

コード


"""