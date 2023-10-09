#問題文 何も書かれていない黒板があります。 x=L, L+1, …, R の順に、以下の操作を行います。 黒板に、整数 x を x 回書く。 全ての操作が終了した後、黒板に書かれている文字の個数を 10 9 +7 で割った余りを求めてください。 ただし、数えるのは整数ではなく文字である事に注意してください。例えば、整数 15 は 2 個の文字として数えます。

#1,2,3,4,5,6,7,8,9 = n(n-1)//2
#10,11,12,13,・・・,98,99 = 99-10+1(個数) *(99+10)//2

L,R = map(int, input().split())

mod = 10**9+7
min_len = len(str(L))
max_len = len(str(R))

ans = 0

for dig in range(min_len,max_len+1):
    t_left = max(10**(dig-1),L)
    t_right = min(10**dig-1, R)
    between_num = t_right-t_left + 1
    ans += between_num*(t_left+t_right)//2 * dig
    ans %= mod
print(ans)
