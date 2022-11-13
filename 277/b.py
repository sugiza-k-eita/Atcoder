import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
first_list= ["H","D","C","S"]
second_list = ["A" , "2" , "3" , "4" , "5" ,"6" , "7" , "8" , "9" , "T" , "J" , "Q" , "K"]
box = []
for i in range(N):
    s = S()
    box.append(s)

for i in range(N):
    first = box[i][0]
    second = box[i][1]
    if first not in first_list:#文字列の1文字目がH,D,C,Sのどれかか
        print("No")
        exit()
    if str(second) not in  second_list:#文字列の2文字目がA~Kのどれかか
        print("No")
        exit()
    box.append(s)

if len(set(box)) == N:#入力されたときと長さが同じなら、すべての文字列に重複はない
    print("Yes")
else:#文字列の量が変化した場合は、重複があったと判断
    print("No")