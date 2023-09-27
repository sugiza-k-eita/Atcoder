#転倒数　
N = int(input())

if N == 1:
    print(0)
    exit()

lr = [list(map(int, input().split())) for _ in range(N)]  # [l, r]のペアを格納
ans = 0

for i in range(N):
    for j in range(i+1, N):
        l1, r1 = lr[i]
        l2, r2 = lr[j]

        all_cnt = (r1 - l1 + 1) * (r2 - l2 + 1)
        cnt = 0

        for val in range(l1, r1 + 1):
            cnt += max(0, min(r2, val - 1) - l2 + 1)  # valより小さい数の個数を足す

        ans += cnt / all_cnt  # 期待値を足す

print(ans)


# #問題文 数列屋の高橋くんは長さ N の数列 a を作っています。数列 a の i 番目の要素 a i ​ の値は、 L i ​ 以上 R i ​ 以下の 整数 から一様ランダムに選ぶことで決定されます。 このようにしてできた数列 a の転倒数の期待値を求めてください。 なお、長さ m の数列 x の「転倒数」とは、 i<j かつ x i ​ >x j ​ であるような (i,j) (1≤i,j≤m) の個数のことです。

# N = int(input())

# L = []
# R = []

# if N == 1:
#     print(0)
#     exit()

# for i in range(N):
#     l,r = map(int, input().split())
#     L.append(l)
#     R.append(r)


# ans = 0
# for i in range(N-1):
#     for j in range(i+1,N):
#         all_cnt = (R[i]-L[i]+1) * (R[j]-L[j]+1)# iとjの時の組み合わせの合計
#         cnt = 0
#         for i_val in range(L[i],R[i]+1):
            
#             if L[j] >= i_val:#
#                 cnt += 0
            
#             elif i_val > R[j]:
#                 cnt += R[j]-L[j]+1
            
#             else:
#                 cnt += R[j]-i_val+1
#         ans += (cnt/all_cnt)

# print(ans)







