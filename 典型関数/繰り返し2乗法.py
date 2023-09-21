# 繰り返し二乗法で (K - 2) ** (N - 3) を mod で割った余りを計算
def mod_pow(x, n, mod):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = result * x % mod
        x = x * x % mod
        n //= 2
    return result


# #問題文 N 個のブロックが横一列に並んでおり、左から順に 1 から N までの番号が付けられています。 これらのブロックそれぞれを、 K 種類の色のうちいずれか一色で塗ることを考えます。ここで、次の条件を満たすように塗らなければなりません。 1≤∣i−j∣≤2 ならば、ブロック i とブロック j に塗られている色は異なる。 ただし、使わない色があってもよい。 このようなブロックの塗り方が何通りあるかを、 10 9 +7 で割った余りを出力してください。ただし、 2 つのブロックの列の塗り方が異なるとは、ある 1 以上 N 以下の整数 i が存在して、ブロック i について異なる色で塗られていることとします。

# N,K = map(int, input().split())
# mod = 10**9 + 7

# if N == 1:
#     print(K)
#     exit()

# if K == 1:
#     print(0)
#     exit()

# if N == 2:
#     print(K*(K-1))
#     exit()

# if K == 2:
#     print(0)
#     exit()

# # 繰り返し二乗法で (K - 2) ** (N - 3) を mod で割った余りを計算
# def mod_pow(x, n, mod):
#     result = 1
#     while n > 0:
#         if n % 2 == 1:
#             result = result * x % mod
#         x = x * x % mod
#         n //= 2
#     return result

# # 本体の計算
# ans = mod_pow(K - 2, N - 3, mod)
# for i in range(3):
#     ans = ans * (K - i) % mod


# print(ans)