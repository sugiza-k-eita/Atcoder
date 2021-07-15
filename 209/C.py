n = int(input())
ns = list(map(int, input().split()))
# 昇順にすると条件を満たすAの個数が(Ci-i+1)となる
# 条件をどの場所においても等しくできる
ns.sort()
ans = 1
# 今回は、10**5なのでfor文はネストしないなら利用できる
for i in range(n):
    ans = ans * max(0, ns[i]-i) % 1000000007
print(ans)
