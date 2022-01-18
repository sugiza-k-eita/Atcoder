"""
https://qiita.com/drken/items/ecd1a472d3a0e7db8dce
しゃくとり法は、以下の形式の問題を解くときに使える可能性のあるテクニックです:

長さ nn の数列 a1,a2,…,ana1,a2,…,an において
「条件」を満たす区間 (連続する部分列) を数え上げよ
 →syakutori1
「条件」を満たす区間 (連続する部分列) のうち、最小の長さを求めよ
「条件」を満たす区間 (連続する部分列) のうち、最大の長さを求めよ
 →syakutori2
"""

"""
https://atcoder.jp/contests/abc130/tasks/abc130_d
"""
#数列Aに対して、何番目から何番目の累積和がK以上か
def syakutori1(N,K,A):
    left = 0
    x = 0
    #xは一時的な累積和
    cnt = 0
    #最初は左端からはじめて
    for right in range(N):
        x += A[right]
        while x >= K:
            #超えたら、回数をカウント
            #↓現在地はrであとN-r回移動できる　現在Kを超えていてN-r回移動しても大きくなるだけ
            #つまり現在地からN-r回はKよりも大きい累積和がある
            cnt += N-right
            #超えたらl（左端）が一つ右にずれる
            x -=A[left]
            left += 1
    return cnt


"""
https://atcoder.jp/contests/abc032/tasks/abc032_c
"""
#数列Aに対して、累積がK以下で最長の部分列はいくつか？
from collections import deque
def syakutori2(N,K,A):
    # もし　0が入っていた場合は、掛け算は0になるため最長はN
    if 0 in A:
        print(N)
        exit()
    
    ans = 0
    q = deque()
    p = 1  ## 今、見ている区間の要素の積をpで管理する。
    for c in A:
        q.append(c)  ## dequeの"右端"に要素を一つ追加する。
        p *= c

        while q and p > K: ## 要素の積がKを超えているか？
            rm = q.popleft() ## 条件を満たさないのでdequeの"左端"から要素を取り除く
            p //= rm ## 取り除いた値に応じて要素の積を更新する

        ans = max(ans, len(q)) ## dequeに入っている要素の積がK以下になるまで区間を縮めた。
    return ans
