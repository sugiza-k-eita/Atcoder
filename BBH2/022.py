import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
from collections import defaultdict

s_letter = S()
t_letter = S()

#ord("a")=97
s_box = [[] for i in range(26)]
t_box = [[] for i in range(26)]

for i in range(len(s_letter)):
    s_box[ord(s_letter[i])-97].append(i)
    t_box[ord(t_letter[i])-97].append(i)

s_box.sort()
t_box.sort()

if s_box == t_box:
    print("Yes")
else:
    print("No")
"""
操作: 2つの異なる英小文字 c1, c2を選び、S に含まれる全ての c1をc2に、c2をc1に置き換える
そのため、英小文字のa~zのうち、それぞれの文字が何文字目に出てきたかを覚えておきます。
(名称として、Sの英小文字リストとTの英小文字リストとします)
例えばaabという文字列があったときに、
a=[0,1],b=[2]のように記憶しておきます。
そして入れ替える操作は
b = [0,1], a = [2]のように考えれば良いです。

では、どのようにすれば、一致するかどうかがわかるのでしょうか？
→それは、Sの英小文字リストとTの英小文字リストで、双方を並び替えて一致したら良いです。
なぜなら操作で、2つの異なる英小文字 c1, c2を選び、S に含まれる全ての c1をc2に、c2をc1に置き換える事ができるので、並び替えても問題がないためです。
そこで、Sの英小文字リストとTの英小文字リストをソートした結果、リストの並びが一致したら"Yes"を、異なったら"No"を出力します
(Sの文字列を入れ替えてTと一致するか→SとTの文字列を入れ替えて一致させることはできるかと考えます)

手順
a~zのうち、それぞれの文字が何文字目に出てきたかを覚えておきます
それらをソートして、一致したらYes,しないのならNo
"""