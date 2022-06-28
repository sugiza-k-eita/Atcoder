import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

s = S()
box = ["A","C","G","T"]
ans = 0
#最終的にプリントする
cnt = 0
#何回 A C G T が続いたかcountする

for i in range(len(s)):
    if s[i] in box:
        cnt += 1
    else:
        ans = max(ans,cnt)
        #ACGTではない場合は、これまでの最大値(ans)と今の値(cnt)を比較して大きい方を採用
        cnt = 0
        #cnt =0として再スタート

#最後のcntとansどちらが大きいか比較
ans = max(ans,cnt)
print(ans)
        
