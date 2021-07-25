n, k = map(int, input().split())
number_list = []
for i in range(1, n+1):
    for j in range(1, k+1):
        number = i*100 + j
        number_list.append(number)
print(sum(number_list))
