import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
import copy
N = II()
P = LI()

for i in range(N-1,-1,-1):
    if P[i] < P[i-1]:
        ans = P[:i-1]# 先頭からi-1桁目までは変化なし
        flg = P[i-1:]#i桁目からN桁目までは変化する
        break

flg_copy = copy.copy(flg)#変化する数列
flg_copy.sort()#小さい順に並び替え
ind = flg_copy.index(flg[0])#i桁目の数字が何番目に小さいか調べる
head = [flg_copy[ind-1]]#i桁目の数字より辞書順が1小さい数字(head)を取る
flg_copy.pop(ind-1)
flg_copy.sort(reverse=True)#headを除いた、 i~N番目の項を辞書順最大にする
ans1 = head + flg_copy
final_ans  = ans+ans1# くっつけて出力
print(*final_ans, sep=" ")

