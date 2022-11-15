import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N,M = MI()
city_list = []#県の名前、市のできた年,indexを管理する、
for i in range(M):
    P,Y = MI()
    #Pが県の名前, Yが年,iがindex
    city_list.append([P,Y,i])
city_list.sort()
#県の名前が若い順→市のできた年が若い順にソート

pre = -1#一つ前の県の名前を記憶するためのflg　最初は-1
ans = []
for i in range(M):
    if pre != city_list[i][0]:#一つ前に取り出した県の名前と異なるのなら
        cnt = 1#上6桁が変化したので、下6桁は000001にリセット
        id = str(city_list[i][0]).zfill(6)+str(cnt).zfill(6)#zfillで6桁にして、上6桁と下6桁をくっつける
        index = city_list[i][2]
        ans.append([index,id])
        pre = city_list[i][0]#次に行く前に今の県の名前を一つ前の県の名前にする
    elif pre == city_list[i][0]:#一つ前の県の名前と同じなら
        cnt += 1#上6桁は変化しないが、下6桁の値は1増える
        id = str(city_list[i][0]).zfill(6)+str(cnt).zfill(6)#zfillで6桁にして、上6桁と下6桁をくっつける
        index = city_list[i][2]
        ans.append([index,id])#index→idの順で格納

ans.sort()#入力されたindex順にソート
for i in range(M):
    print(str(ans[i][1]))


"""
今回、すべての入力を受け取ってから出ないと、idを決めることができません。なぜならi番目の入力時点では最初であっても、それ以降の入力でもっと若い年に設立された市があるかもしれないからです。
なので、まず最初に全ての市の情報を受け取ります。この際に、何番目に入力されたかも後のち、出力する順番で必要になりますので、index情報も取得します。
全ての市の情報を[県の名前]→[できた年]→[index]の順でリスト格納したら、ソートします。
ソート関数は、1番目の要素が同じ場合二番目の要素が若い方を前に配置しますので、
これで、県の名前→設立された年にソートされたリストが完成します。

そこからは、for文で1リストごとに見ていき、
もし、一つ前の要素と県の名前が異なるなら、上6桁を変化させ、下6桁を1にリセット
もそ、一つ前の要素と県の名前が同じなら、上6桁は変化させずに、下6桁を+1する

その後、出力するためにindex順にソートし直して出力すれば良いです。
"""