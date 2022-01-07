import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

H,W = MI()
Q = II()

box = []
for i in range(H):
    w = S()
    box.append(w)

J_box = [[0]*(W+1) for i in range(H+1)]
I_box = [[0]*(W+1) for i in range(H+1)]
O_box = [[0]*(W+1) for i in range(H+1)]
for i in range(1,H+1):
    for j in range(1,W+1):
        if box[i-1][j-1] == "J":
            J_box[i][j] = J_box[i][j-1]+1
            O_box[i][j] = O_box[i][j-1]
            I_box[i][j] = I_box[i][j-1]
        elif box[i-1][j-1] == "O":
            O_box[i][j] = O_box[i][j-1]+1
            J_box[i][j] = J_box[i][j-1]
            I_box[i][j] = I_box[i][j-1]
        elif box[i-1][j-1] == "I":
            I_box[i][j] = I_box[i][j-1]+1
            O_box[i][j] = O_box[i][j-1]
            J_box[i][j] = J_box[i][j-1]
        

for w in range(1,W+1):
    for h in range(1,H+1):
        J_box[h][w] += J_box[h-1][w]
        I_box[h][w] += I_box[h-1][w]
        O_box[h][w] += O_box[h-1][w]

for i in range(Q):
    a,b,c,d = MI()
    a -= 1
    b -= 1
    J_ans  = J_box[a][b] + J_box[c][d] - J_box[a][d] - J_box[c][b]
    I_ans  = I_box[a][b] + I_box[c][d] - I_box[a][d] - I_box[c][b]
    O_ans  = O_box[a][b] + O_box[c][d] - O_box[a][d] - O_box[c][b]
    print(J_ans,O_ans,I_ans)

