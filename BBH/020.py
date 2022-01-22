import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N,M = MI()

cities = [[] for i in range(N)]

for j in range(M):
    p,x = MI()
    p -= 1
    cities[p].append([x,j])

for xx in cities:
    xx.sort()

# for xx in cities:
#     print(xx)
ans = []
for i in range(N):
    for j in range(len(cities[i])):
        # print(cities[i][j][1])
        ans.append([cities[i][j][1],i+1,j+1])

ans.sort()
for i in range(len(ans)):
    town,year=str(ans[i][1]),str(ans[i][2])
    town_num = town.zfill(6)
    year_num = year.zfill(6)
    print(town_num+year_num)

