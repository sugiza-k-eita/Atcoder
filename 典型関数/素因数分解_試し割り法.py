#計算量は√n
#入力値が10**9以上ならロー法を使用する
def tameshi(n):
  ret = []
  for i in range(2, int(n ** (1 / 2)) + 1):
    if i > n:break
    while n % i == 0:
      n //= i
      ret.append(i)
  if n != 1:
    ret.append(n)
  return ret

n = int(input())
print(str(n)+": ",end="")
print(*tameshi(n))

#N = A*Bとなるような　A*Bの列挙
def koukan(n):
    ret = []
    for i in range(1, int(n ** (1 / 2)) + 1):
        if n%i ==0:
            ret.append((i,n//i))
            flg = n//i
        if flg <= i:
            break
    return ret