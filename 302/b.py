H, W = map(int,input().split())
box = []
for i in range(H):
    letter = input()
    box.append(letter)

direction = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
word = "snuke"
for i in range(H):
    for j in range(W):
        if box[i][j] == "s":
            for d in range(8):
                move_i = i
                move_j = j
                ans = []
                for k in range(5):
                    if  0 <= move_i < H and 0 <= move_j < W and box[move_i][move_j] == word[k]:
                        ans.append([move_i,move_j])
                        move_i += direction[d][0]
                        move_j += direction[d][1]
                    else:
                        break
                
                if len(ans) == 5:
                    for l in range(5):
                        print(ans[l][0]+1, ans[l][1]+1)



"""
上下左右、斜めの合計8方向に探索する

"""