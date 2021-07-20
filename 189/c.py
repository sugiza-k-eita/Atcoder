n = int(input())
ns = list(map(int, input().split()))
# 食べれるみかんの量は区間の長さ×区間内の最小値
ans = 0
for l in range(n):
    m = 10 ** 6  # 適当な10 ** 5より大きい数で初期化←区間内の最小値を求めるため
    for r in range(l, n):
        d = r - l + 1  # 区間の幅
        m = min(m, ns[r])
        # 区間の最小を更新　２回め以降は、lからr-1までの最小値と新しく加えたns[r]を比較して最小値を求めている
        score = m * d  # 食べたみかん
        ans = max(ans, score)
"""
for i in range(n):
  for j in range(i,n)

  の計算量は　1からnの総和　で少しだけ計算量を落とせる
"""
print(ans)
