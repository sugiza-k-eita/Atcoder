mod = 1000000007
l = input().split()
m = int(l[0])
n = int(l[1])


def power(x, y,mod = 10**9 +7):
    if y == 0:
        return 1
    elif y == 1:
        return x % mod
    elif y % 2 == 0:
        return power(x, y/2)**2 % mod
    else:
        return power(x, int(y/2))**2 * x % mod


ans = power(m, n)
#mのn乗を出力
print(ans)
