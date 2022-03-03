def comb(n, r, mod=10**9 + 7):
    """
    nCr を modを法として求める
    計算量はO(r)
    modがNoneの場合は modを取らない結果を返す
    mod はNoneか素数であることを仮定する
    """
    p = 1
    for i in range(r):
        p *= (n - i) * pow(i + 1, mod-2, mod)
        p = p % mod
 
    return p


def comb(n, r, m):
  X, Y = 1, 1
  for i in range(r):
    X *= n-i
    Y *= i+1
    X %= m
    Y %= m
  return int(X * pow(Y, m-2, m))