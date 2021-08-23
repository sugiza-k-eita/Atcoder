N = int(input())
count = 0
while True:
    if N == 1:
        break
    N = N//2
    count += 1
    
print(count)