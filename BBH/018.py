import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

sx,sy,tx,ty = MI()
tate = ty-sy
yoko = tx -sx

one = ["U"*tate, "R"*yoko]
two = ["D"*tate, "L"*yoko]
three = ["L", "U"*(tate+1),"R"*(yoko+1),"D"]
four = ["R","D"*(tate+1),"L"*(yoko+1),"U"]

ans = one+two+three + four
print(*ans,sep="")
