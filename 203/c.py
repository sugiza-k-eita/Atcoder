n, k = map(int, input().split())
freind_table = []
for i in range(n):
    a, b = map(int, input().split())
    freind_table.append((a, b))
freind_table.sort()
now = k

"""
k円あれば、k回村を移動できる
k回移動する過程で、友達がいたら、その分お金を追加
大事なのは、移動するたびにif文を回すのではなく、k円分移動したあとに、
それまでの過程に友達がいたかif文するところ
毎回回していたら、Aのオーダー文かかってしまい、TLEになる
"""
for i in range(n):
    a, b = freind_table[i]
    if now >= a:
        now += b
    else:
        break
print(now)
