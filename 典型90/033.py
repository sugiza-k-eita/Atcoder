H, W = map(int, input().split())
tate = (H+1)//2
yoko = (W+1)//2
if H == 1 or W == 1:
    print(max(H, W))
else:
    print(tate*yoko)
