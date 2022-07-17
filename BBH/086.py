import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


N = II()
S1 = S()
S2 = S()
if len(S1) ==1:
    print(3)
    exit()

a = ""

cnt = 0
while cnt < N-1:
    if S1[cnt] == S1[cnt+1]:
        a += "#"
        cnt +=1
    else:
        a += "."
    cnt += 1

if cnt != N:
    if S1[-1] == S1[-2]:#横
        a += "#"
    else:#縦
        a += "."
        cnt = 1

if a[0] == "#":
    ans = 6
else:
    ans = 3

# print(a)
for i in range(1,len(a)):
    if a[i] == a[i-1]:
        if a[i] == "#":
            ans *= 3
            ans %= 1000000007
        else:
            ans *= 2
            ans %= 1000000007
    
    else:
        if a[i] == "#":
            ans *= 2
            ans %= 1000000007
        else:
            ans *= 1
            ans %= 1000000007
print(ans)

"""
方針
左から順に色分けをしていきます。


場合分けの問題
今回、入力されるドミノのパターンは2通り
zz
xx のように横に長いのが2つ積み重なっているパターン

z
z   のように縦に長いのが1つだけあるパターン

この2通りしかないです。

今回、色分けするする際に重要なのは、自分の左隣にあるドミノの色分けです。なぜならi番目のドミノはi-1番目のドミノの色分けの影響のみを受け、それ以外のドミノの色分けの影響を受けないためです。
なので、i番目のドミノのパターンとi-1番目のドミノのパターンについて考えていきます。

注意X,Y はi-1番目のドミノとし、色は一意に定まっているものとしています。

XXcc
YYdd のように横に長いのが、2回連続で続く場合
→ccがbbと同じ色の場合は、ddは2通り+ccがbbと異なる色の場合はddは1通り
なので、横に長いのが、2回連続で続く場合の通り数は3通りです。

Xaa
Xbb のように縦に長いのが1つ、横に長いのが1つの場合
aaはXと異なる色の2通りで、bbはXとaaと異なる色なので1通り
なので、2*1 = 2通り

XXa
YYa のように横に長いのが1つ、縦に長いのが、続く場合
aは、XとYと異なる色なので1通り

Xa
Xa のように縦に長いのが、2回連続で続く場合
aはXと異なる色なので2通り


以上が今回実装するべき場合分けの通り数です。なのでこれから実装していきます。

まず最初に、横に長いのか、縦に長いのか入力状態だけだと分かりづらいので、
横に長いドミノは"#", 縦に長いのドミノは"."に変換してから場合分けを実装します。

次に、初期値を設定します。
aa
bb の場合は、色の塗り分けが6通りありますが、

a
a の場合は色の塗り分けは3通りです。
"""