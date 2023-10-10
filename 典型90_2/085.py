K = int(input())

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

box = make_divisors(K)


ans=0

for i in range(len(box)):
    A = box[i]
    nK = K//A
    for j in range(i,len(box)):
        B = box[j]
        if nK%B== 0:
            C = nK//B
            if A<=B<=C:
                ans += 1




print(ans)