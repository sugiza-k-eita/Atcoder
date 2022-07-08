import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
if N%2 ==1:
    print(0)
    exit()


"""
末尾に0が何個つくか？
→10の倍数が何回かけられているか？
→x10 or x2 and x5　のとき10の倍数がかけられたと言える

n % 2 ==1:
奇数の場合、奇数は奇数×奇数のとき以外奇数にならないので、どのような奇数をとっても約数に偶数を持つことはない
つまり、偶数がかけられることがないので、絶対に10の倍数になることはないです。

n % 2 == 0:
偶数の場合、約数に奇数を持つことがあるので、2の倍数と5の倍数の数を数え上げ、その最小値が答えになります。
しかし、5の倍数のほうが少ないのは、自明です。なぜなら5の倍数が現れるのは、10の倍数のときのみですが、2の倍数は最小でn//2個出現するためです。

そのため、今回は5が何回かけられたかを数え上げています。
"""

a = 10
cnt = 0
while a <= N:
    tmp_cnt = N //a
    cnt += tmp_cnt
    a *= 5

print(cnt)
    

