n, a, x, y = map(int, input().split())
if n <= a:
    sum = n*x
else:
    normal_quantity = a
    discount_quantity = n-a
    normal_price = normal_quantity*x
    discount_price = discount_quantity*y
    sum = normal_price+discount_price

print(sum)
