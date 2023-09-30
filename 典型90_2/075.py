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
prime_cnt = len(tameshi(n))

cnt = 0
while True:
    if 2**(cnt) >= prime_cnt:
        print(cnt)
        break
    else:
        cnt += 1