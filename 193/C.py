N = int(input())
Settable = set()
# 2<a<10**5, 2<b<34なので
for a in range(2, 10**5 + 1):
    for b in range(2, 34):
        if a**b <= N:

            Settable.add(a**b)
amount = N-len(Settable)
print(amount)
"""
ABCの制限時間は2秒のため の場合N≦10**7 が限度と考えた方がいいです。
"""
