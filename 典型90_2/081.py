N,K = map(int, input().split())

leng = 5001
two_dimension_arr = [[0]*(leng+1) for i in range(leng+1)]
#基準必要？
#それとも列挙で大丈夫？
for i in range(N):
    A,B = map(int, input().split())
    mx_x,mx_y = min(leng,A+K+1),min(leng,B+K+1)
    # print(111111111,mx_x,mx_y)
    two_dimension_arr[A][B] += 1
    two_dimension_arr[mx_x][B] -= 1
    two_dimension_arr[A][mx_y] -= 1
    two_dimension_arr[mx_x][mx_y] += 1

#いもす法じゃないとできないわ

#横方向への累積
for i in range(1,leng+1):
    for j in range(1,leng+1):
        two_dimension_arr[i][j] += two_dimension_arr[i][j-1]

#縦方向への累積
for j in range(1,leng+1):
    for i in range(1,leng+1):
        two_dimension_arr[i][j] += two_dimension_arr[i-1][j]

# for x in two_dimension_arr:
#     print(x)

maxv = 0
for i in range(leng):
    for j in range(leng):
        maxv = max(maxv,two_dimension_arr[i][j])
        
print(maxv)