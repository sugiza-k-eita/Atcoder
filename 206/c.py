from collections import Counter
N = int(input())
ns = list(map(int, input().split()))
count = Counter()
# 空のカウントを作成,12行目でcountの辞書にindex ns[i]の値を+1している
ans = 0
for i in range(N):
    ans += i - count[ns[i]]
    # 全部違う数なら出てきた回数は、整数組はi個
    # しかし被りがあるからそれを除去　除去する量はi番目と同じ数字が何回出てきたらで決まる
    # i番目までに同じ数が出てきていたら、その分count[ns[i]]で引いている。
    count[ns[i]] += 1
    # ここでcountの辞書にindex ns[i]の値を+1している
print(ans)
