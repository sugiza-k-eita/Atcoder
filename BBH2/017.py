import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
AB_cnt = 0
A_cnt = 0
B_cnt = 0
ans = 0
for i in range(N):
    letter = S()
    if letter[0] == "B" and letter[-1] == "A":#先頭がBかつ末尾がBの個数をカウント
        AB_cnt += 1
    if letter[-1] == "A":#先頭がB以外で、末尾がAをカウント
        A_cnt += 1
    if letter[0] == "B":#先頭がBで、末尾がA以外のをカウント
        B_cnt += 1
    
    for j in range(len(letter)-1):#CABDのように文字列の中にABが含まれるのをカウント
        if letter[j] == "A" and letter[j+1] == "B":
            ans += 1

if A_cnt == B_cnt == AB_cnt != 0:
    ans -= 1
    #もしすべてが"BA"などの先頭がB、末尾にAの文字列の場合、作成できるABの文字列は、N-1なので、-1
cnt = min(A_cnt,B_cnt)
print(ans+cnt)

"""
作った文字列に"AB" という部分文字列は2種類あります。
もともとの文字列に"AB" という部分文字列がある場合
ex) CABZ
末尾がAと先頭がBの文字列の2つの文字列がくっついてできる場合
ex) CA,BX
1パターン目は、与えられた複数の文字列に対し、1つずつ"AB"が何個含まれるかカウントすれば良いです。
2パターン目は、少し厄介で、末尾が"A"である文字列の個数と、先頭が"B"である文字列の個数と先頭が"B"かつ末尾が"A"の文字列の個数をカウントする必要があります。
なぜなら、"BCA"という文字列が合った場合、先頭が"B"である文字列でもあり、末尾が"A"である文字列でもあります。
しかし、BCAという文字列だけでは、"AB"の並びを作れないです。そのため、先頭が"B"である文字列と末尾が"A"である文字列をカウントする必要があります。
そして、末尾の"A"と先頭の"B"のうち、小さい数字だけ"AB"という文字を作れます。
"""