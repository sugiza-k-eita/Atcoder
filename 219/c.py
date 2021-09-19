X = input()
dic = {}
cnt = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(X)):
    dic[X[i]] = cnt[i]
N = int(input())
box = []
dic2 = {}
for i in range(N):
    i = input()
    num = ""
    for j in i:
        num += str(dic[j])
    dic2[num] = i
    box.append(num)
box.sort()


for i in box:
    print(dic2[i])
