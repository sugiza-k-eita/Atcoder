A, B, C, X, Y = map(int, input().split())
ans = 10**9
upper_limit = max(X, Y)
for i in range(0, upper_limit+1):
    A_amount = (X-i)
    A_amount = max(A_amount, 0)
    B_amount = (Y - i)
    B_amount = max(B_amount, 0)
    A_price = A_amount*A
    B_price = B_amount*B
    C_price = C*i*2
    total = A_price+B_price+C_price
    ans = min(ans, total)
print(ans)
