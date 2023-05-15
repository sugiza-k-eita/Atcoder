s = input()
N = int(input())
a = bin(N)#2進数に変換
two_N = a[2:]#b0はいらないので、取り除く
cnt_ind = []
for i in range(len(s)):#?の場所を記憶しておく
    if s[i] == "?":
        cnt_ind.append(i)

#？→0にしてもNよりも大きかったら、-1
min_num = s.replace("?", "0")
if int(min_num,2) > N:
    print(-1)
    exit()

cnt = ""#答えとなる値を2進数で記憶
for i in range(len(s)):
    #シフト演算がよくわからなかったので、文字列として記憶して、結合→int変換しています・・・
    if i in cnt_ind and int((cnt + "1")+min_num[i+1:],2) <= N:
        #もしi番目が?→0に変換した場所でかつ、?→1に変換した場合でもN以下なら
        cnt += "1"
    else:#それ以外
        cnt += min_num[i]
print(int(cnt,2))