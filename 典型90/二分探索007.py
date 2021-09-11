import bisect

N = int(input())
rate_class = list(map(int, input().split()))
rate_class = sorted(list(set(rate_class)))


check = [[] for i in range(len(rate_class)-1)]
for i in range(len(rate_class)-1):
    check[i] = (rate_class[i] + rate_class[i+1])/2
# print(rate_class)
# print(check)
Q = int(input())
ans = []
for i in range(Q):
    b = int(input())
    index = bisect.bisect_left(check, b)
    # ans.append(abs(rate_class[index]-b))
    print(abs(rate_class[index]-b))
# for i in ans:
#     print(i)
