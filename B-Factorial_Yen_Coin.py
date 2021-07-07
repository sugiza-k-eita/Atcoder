P = int(input())
coin_list = [3628800, 362880, 40320, 5040, 720, 120, 24, 6, 2, 1]
count = 0
while True:
    if P == 0:
        break
    for i in coin_list:
        if P >= i:
            P = P-i
            count += 1
            break
print(count)
