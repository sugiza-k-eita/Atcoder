import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

#t文字目からk番目の文字を出力
"""
方針
1, S**tのk番目とは、S**0の何文字目が派生した形か考察する(is_where)
2, 3回派生したら、元のアルファベットになるので、何回派生したかを考える(t=派生回数)
3, t回派生するときに、+1 or +2 のどちらかの選択肢を何回行ったかを考察する (popcount)
"""
def popcount(n):
    ans = 0
    while n:
        ans += n % 2
        n //= 2
    return ans

abc = "ABC"
s = S()
num = []
for i in s:
    if i == "A":
        num.append(0)
    elif i == "B":
        num.append(1)
    else:
        num.append(2)

Q = II()
print(s,num)
for i in range(Q):
    t,k = MI()
    k -= 1
    is_where = k // pow(2,min(t,60))
    #s[is_where] はsという文字列のiswhere番目がt回派生するとk番目が出る

    #求めたい文字が何回左にいき、何回右に行ったか
    r = popcount(k)
    #右に移動した回数
    l = t - r
    #左に移動した回数
    x = r*2 + l
    print("l",l,"r",r,"x",x)
    ori = num[is_where]
    print(s[is_where],s[(ori+x)%3])
#     #xは移動した矢印の重み？みたいなもの
#     index = s[(s[is_where]+x)%3]
#     print(abc[index])



    #どのような変化をたどったか


