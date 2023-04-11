H,W = map(int, input().split())
box = []#最後に答えを出力する空のリスト
cnt = 0
for i in range(H):
    s = input()#文字列を受け取る
    s_l = list(s)#文字列だと操作しづらいのでリストに変換
    for j in range(W-1):
        if s_l[j]== s_l[j+1] == "T":#もし、j番目もj+1番目もTだったら
            s_l[j] = "P"#j番目をPに
            s_l[j+1] ="C"#j+1番目をCへ
    
    ans = ""#答えを出力する空の文字列
    for j in range(W):#先程変更した文字列を
        ans += s_l[j]#順に連結(足して)
    box.append(ans)#最終的な答えのリストに格納

for i in range(H):
    print(box[i])

"""
C - PC on the Table
https://atcoder.jp/contests/abc297/tasks/abc297_c

入力
今回重要なのは、
操作は行方向に行っていく
任意のx行目に操作を行っても、別の行には影響は出ない

そのため、1行目からH行目まで独立して操作を行う事ができます。
また今回は、制約がH,W < 100なので、全探索することが可能です

よって具体的な操作としては、任意の行(x行目)の1-W列目において
もし、自分(j)がTで、自分の右隣(j+1)もTであれば、自分と右隣をそれぞれP,Cに変更し
その結果を出力することで答えにたどり着けます。


"""