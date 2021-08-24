five_hundred = int(input())
one_hundred = int(input())
fifty = int(input())
account = int(input())

five_hundred_box = []
one_hundred_box = []
fifty_box = []

for i in range(five_hundred+1):
  tmp = i*500
  five_hundred_box.append(tmp)

for i in range(one_hundred+1):
  tmp = i*100
  one_hundred_box.append(tmp)
  
for i in range(fifty+1):
  tmp = i*50
  fifty_box.append(tmp)

ans = 0
for a in five_hundred_box:
    for b in one_hundred_box:
        for c in fifty_box:
            if a+b+c == account:
                ans += 1
print(ans)