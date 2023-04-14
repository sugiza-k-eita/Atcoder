import math
A,B = map(int, input().split())

common= math.gcd(A,B)#2数の共通する因数、すなわち最大公約数を求める
eA = A//common#Aだけがもつ因数を求める
eB = B//common#Bだけがもつ因数を求める
ans = eA*eB*common
if ans > 10**18:
    print("Large")
else:
    print(ans)

"""
最小公倍数=2数の共通する因数*Aのみがもつ因数*Bだけがもつ因数
2数の共通する因数は、最大公約数です。
そのため、
Aだけがもつ因数= A//最大公約数で求められます
Bだけがもつ因数も同様です。

そのため、手順として
最大公約数を求める
最大公約数でA,Bを割る
それらをかけて、10^18を超えたらLarge,それ以外は数値を出力
"""