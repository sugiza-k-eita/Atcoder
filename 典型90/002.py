from itertools import product, repeat

N = int(input())

for bit in product((0, 1), repeat=N):
    check = 0  # 同じ個数あるか確認します
    flg = 0
    ans = []

    for i in bit:
        if i == 0:
            check += 1
        else:
            check -= 1

        if check < 0:
            flg = 1
            break

    if flg == 0:
        if (sum(bit)) == N/2:
            for j in bit:
                if j == 0:
                    j = "("
                    ans.append(j)
                else:
                    j = ")"
                    ans.append(j)
        print(*ans, sep="")
