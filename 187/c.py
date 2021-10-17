N = int(input())
box = set()
for i in range(N):
    s = str(input())
    box.add(s)

for T in box:
    if "!"+T in box:
        print(T)
        exit()
print("satisfiable")
