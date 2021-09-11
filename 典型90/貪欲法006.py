# 辞書的に早いというのは、最初の文字が一番大事
# azz と baaaだと　前者のほうが早い つまり前のほうが重要でそこを貪欲法で実装する

from collections import deque
n, k = map(int, input().split())
S = input()
ans = deque()
res = []

for i in range(n):
    while ans and S[i] < ans[-1]:
        # ansに要素があり、かつS[i]よりもans[-1]が大きいとき
        # s[i]よりもans[-1]のほうが辞書的に遅いとき
        ans.pop()
    ans.append(S[i])
    print(ans)
    if n-i <= k:
        print(1111)
        res.append(ans.popleft())
print(*res, sep="")
