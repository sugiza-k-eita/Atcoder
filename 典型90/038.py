from math import gcd
# 最小公倍数は両方の数をかけたものに対し、最大公約数で割ったもの
# /でも大丈夫だが、//にしないとWAになる→オーバーフロー？浮動？
# 計算の順番は極力割り算を先にやる
#　数が大きくなればなるほど計算時間がかかるため、割り算をして、桁数を減らしたい
A, B = map(int, input().split())
if A//gcd(A, B)*B > 10**18:
    print("Large")
else:
    print(A*B//gcd(A, B)*B)
