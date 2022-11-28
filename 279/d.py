import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

A,B = MI()

def check(c1,c2):
    c1_time = A/((c1+1)**0.5) + B*(c1)#c1回操作をしたときの到着時間
    c2_time = A/((c2+1)**0.5) + B*(c2)#c2回操作をしたときの到着時間
    if c1_time - c2_time > 0:#f(c1) > f(c2)の場合は
        return True
    elif c2_time - c1_time >= 0:#f(c2) > f(c1)の場合は
        return False
        
    
#操作回数(x)の最小の操作回数は0回、最大で10**18回
left, right = 0, 10**18

while right - left > 3:#三分探索法の場合、範囲が3以上じゃないと三分割できないので、範囲が3よりも大きければ
    c1 = (left*2 + right)//3#三分割するためのc1
    c2 = (left+right*2)//3#三分割するためのc2
    
    if check(c1,c2):#f(c1) > f(c2)の場合
        left = c1
    else:#f(c1) < f(c2)の場合
        right = c2

ans = 10**18
for i in range(left,right+1):#leftからrightの範囲が3以下になったら、leftからrightの範囲を全探索
    arrive_time = A/((i+1)**0.5) + B*(i)
    ans = min(arrive_time,ans)
print(ans)

"""

今回の問題は三分探索法を使う問題です。
Q 三分探索法とは？
凸型の関数の最小値を求める際に使用できる解法です。
※f(x)というxの取りうる範囲を[left,right]とした場合の凸型の関数において、最小値をとるf(m)までに
leftからmにかけて単調減少し、mからrightまで単調増加する場合のみ使用できる。

なので、極値を持つ3次関数や、f(x)の傾きが0となる点が最小値以外にあると使えない

三分探索法のアルゴリズム
1
f(x)という関数のうち、xの取りうる範囲を[left,right]とした場合、
l→rの範囲を三分割するような、c1,c2という値を取ります。
c1 = (left*2 + right)//3
c2 = (left+right*2)//3

2
f(c1)とf(c2)の大小関係を比べ、
もし、f(c1)の方が大きければlの値をc1に変更し
もし、f(c2)の方が大きければlの値をc2に変更します

なぜ、これで良いかというと、lとrは、そこが最小値でない限り、
f(left)>f(c1), f(right) > f(c2)が必ず成り立ちます。
そこで、f(c1)> f(c2)の場合
f(left)>f(c1)>f(c2)となりますので、
lからc1の間には最小値が存在しないことがわかります。
同様に、f(c1) < f(c2)の場合は
f(right)>f(c2)>f(c1)となり、rからc2の間には最小値が存在しないことがわかります。
s
これにより、1会の操作で最小値の範囲を、2/3倍にすることができます。
これにより、10**18であっても探索できます。
"""