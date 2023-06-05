from collections import defaultdict
items = defaultdict(int)

N,M,H,K = map(int, input().split())
s = input()
box = []
for i in range(M):
    x,y = map(int, input().split())
    items[(x, y)] += 1
directions = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

hp = H
x,y = 0,0
for i in range(N):
    dx, dy = directions[s[i]]
    x += dx
    y += dy
    hp -= 1
    if hp < 0:
        print('No')
        exit()
    
    if (x, y) in items and hp < K:
        hp = K
        items.pop((x,y))
    

print("Yes")