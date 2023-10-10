import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)



MOD = 10**9 + 7

N, Q = MI()
query = [LI() for _ in range(Q)]

ans = 1
for i in range(60):
    cnt = 0
    for bit in range(2**N):
        # bit_str = bin(bit)[2:].zfill(60)
        # bit_str = bit_str[::-1]
        for x, y, z, w in query:
            x -= 1
            y -= 1
            z -= 1
            # w_str = bin(w)[2:].zfill(60)
            # w_str = w_str[::-1]
            if ((bit>>x)&1) | ((bit>>y)&1) | ((bit>>z)&1) != ((w>>i)&1):
                break
        else:
            cnt += 1
    ans *= cnt
    ans %= MOD

print(ans)

"""
考えはあってるけどTLE
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)



MOD = 10**9 + 7

N, Q = MI()
query = [LI() for _ in range(Q)]

ans = 1
for i in range(60):
    cnt = 0
    for bit in range(2**N):
        bit_str = bin(bit)[2:].zfill(60)
        bit_str = bit_str[::-1]
        for x, y, z, w in query:
            x -= 1
            y -= 1
            z -= 1
            w_str = bin(w)[2:].zfill(60)
            w_str = w_str[::-1]
            if (int(bit_str[x])&1) | (int(bit_str[y])&1) | (int(bit_str[z])&1) != (int(w_str[i])&1):
                break
        else:
            cnt += 1
    ans *= cnt
    ans %= MOD

print(ans)

"""


"""
このコードはビット演算を使用して、特定の条件を満たす数列 \(A\) の組み合わせを数え上げています。具体的には、入力として以下の値が与えられます：

- \(N\): 数列 \(A\) の長さ
- \(Q\): クエリの数
- \(req\): \(Q\) 個のクエリ。各クエリは四つの整数 \(x\), \(y\), \(z\), \(w\) からなります。

以下、コードの各部分の詳細な説明です：

### 1. 入力取得

```python
N, Q = map(int, readline().split())
req = [tuple(map(int, readline().split())) for _ in [0] * Q]
```
- `N` と `Q` を読み込みます。
- `req` は \(Q\) 個のクエリを格納するタプルのリストです。リスト内包表記と `map` 関数を使用して整数に変換し、クエリをタプルとして格納します。

### 2. 初期化

```python
MOD = 10**9 + 7
ans = 1
```
- `MOD` はモジュロ演算の基数です。
- `ans` は答えを保持する変数です。最初に1で初期化されています。

### 3. 主要なループ（ビット演算の部分）

```python
for i in range(60):
```
数列 \(A\) の要素は \(0 \leq A_j < 2^{60}\) であるため、60ビットで全ての情報を表現可能です。ここでは、各ビットについて、条件を満たすか確認しています。

### 4. ビット列の生成

```python
cnt = 0
for j in range(1 << N):
```
- `cnt` は、条件を満たす \(j\) のカウントを保持します。
- `j` は \(0\) から \(2^N - 1\) までの整数をビット列として扱います。

### 5. クエリの確認

```python
for x, y, z, w in req:
    x -= 1
    y -= 1
    z -= 1
    if (j >> x & 1) | (j >> y & 1) | (j >> z & 1) != (w >> i & 1):
        break
else:
    cnt += 1
```
- 各クエリ（`x`, `y`, `z`, `w`）について、`x`, `y`, `z` を1減らし、0インデックスでアクセスできるように調整します。
- ビット演算を使用して \(j\) の各ビットがクエリの条件を満たすかチェックします。
- `if` 文の条件が `False` である（つまり全てのクエリが条件を満たす）場合、`cnt` を1増やします。

### 6. 結果の更新

```python
ans *= cnt
ans %= MOD
```
- これまでの `ans` に、このビットでの `cnt` を掛け、`MOD` で割ります。

### 7. 出力

```python
print(ans)
```
- 最後に、答えを出力します。

### まとめ

このコードはビット演算とブルートフォース（全探索）を組み合わせて、すべての可能なビット列に対して、全てのクエリが条件を満たすかをチェックしています。それに基づいて、最終的な答えを計算し、出力します。




------------------






どのビットが1かを考えるだけでも2^(60*12)もあるので無理、2^60ですら無理なのに。あるクエリの条件を満たすと別のクエリの条件も満たす場合もあるしどうしたものか。

これはAの各要素を桁ごとにbit全探索して、条件1を満たしている場合の数を数える。

"""