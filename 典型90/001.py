N, L = map(int, input().split())
K = int(input())
ns = list(map(int, input().split()))


def check(x):
    num = 0
    # 何個に切れたか
    pre = 0
    # 前回の切れ目の位置
    for i in range(N):
        if ns[i] - pre >= x:
            # 前回の切れ目の位置からぜんざいの切れ目の位置の長さがx以上なら
            num += 1
            pre = ns[i]
    # 最後のピースがx以上なら加算
    # これがK+1の+1の部分
    if L - pre >= x:
        num += 1

    return (num >= K + 1)
    # 分割した個数がK+1(切った回数+1)になったらreturn


# 2分探索
left, right = -1, L+1

while right - left > 1:
    # right は今回　L+1 でleftがLのときは
    # L+1 -L = 1になるからその時にbreakが起きるようになっている？
    mid = (left + right)//2
    # 真ん中を調べる
    if check(mid):
        # すべてのようかんをmid以上の長さにできるのなら
        left = mid
    else:
        right = mid
print(left)
