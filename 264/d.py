import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

letter = S()
arr =[]
for i in range(len(letter)):
    if letter[i] == "a":
        arr.append(0)
    elif letter[i] == "t":
        arr.append(1)
    elif letter[i] == "c":
        arr.append(2)
    elif letter[i] == "o":
        arr.append(3)
    elif letter[i] == "d":
        arr.append(4)
    elif letter[i] == "e":
        arr.append(5)
    elif letter[i] == "r":
        arr.append(6)

# print(arr)
n = len(arr)
i = 0          
cnt = 0

for i in range(6):
    for j in range(i+1,7):
        if arr[i] > arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
            cnt += 1
# print(arr)
print(cnt)