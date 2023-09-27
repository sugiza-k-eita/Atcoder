class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, x):
        i += 1  # 1-indexed
        while i <= self.n:
            self.bit[i] = max(self.bit[i], x)
            i += i & -i

    def query(self, i):
        i += 1  # 1-indexed
        res = 0
        while i > 0:
            res = max(res, self.bit[i])
            i -= i & -i
        return res
# LIS

N = int(input())
A = list(map(int, input().split()))

# upの計算
box = []
for i in range(N):
    val = A[i]
    box.append([val, N - i])
box.sort()

up = [0] * N
bit = BIT(N)
for i in range(N):
    ind = N - box[i][1]
    up[ind] = bit.query(ind) + 1
    bit.add(ind, up[ind])

# downの計算
box = []
for i in range(N):
    val = A[i]
    box.append([val, i])
box.sort()

down = [0] * N
bit = BIT(N)
for i in range(N):
    ind = box[i][1]
    down[ind] = bit.query(N - ind - 1) + 1
    bit.add(N - ind - 1, down[ind])

# 最終結果の計算
ans = 0
for u, d in zip(up, down):
    ans = max(ans, u + d - 1)

print(ans)


"""
問題文 
長さ N の数列 A=(A 1 ​ ,A 2 ​ ,⋯,A N ​ ) が与えられます。 A の（連続とは限らない）部分列 B=(B 1 ​ ,B 2 ​ ,⋯,B M ​ ) であって、次の条件を満たすものを考えます。 条件　ある整数 K(1≤K≤M) が存在して、以下の条件をともに満たす 1≤j<K を満たす全ての j に対し、 B j ​ <B j+1 ​ が成立する K≤j<M を満たす全ての j に対し、 B j ​ >B j+1 ​ が成立する B の要素数 M として考えられる最大値を求めてください。


盛り込みたい内容
単調増加
単調減少

自分よりも左でかつ未満の数の個数


最長増加部分列(LIS)を求めるアルゴリズム

TLEなるコード

今回は、計算量がシビアなので、前計算が必要
具体的にどこを高速化するか？

"""