import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

s = S()
T = S()

reversed_s = s[::-1]
reversed_t = T[::-1]
cnt = 0
#何文字一致したかをカウントする
for i in range(len(reversed_s)-len(reversed_t)+1):
    for j in range(len(reversed_t)):
        #反転させたs'が ? or 反転させたTの文字列が一致したら
        if reversed_s[i+j] == '?' or reversed_s[i+j] == reversed_t[j]:
            #一致した文字列をカウントを+1する
            cnt += 1   
            
            if cnt == len(reversed_t):
                #一致した文字列がTの文字列分になったら
                ans = reversed_s[:i] + reversed_t + reversed_s[i+len(reversed_t):]
                # 答えとなる文字列を作成
                ans = ans[::-1]
                # 文字列を反転
                print(ans.replace('?', 'a'))
                exit()
        else:
            ##一致しなかったら何文字一致したかのカウントをリセットする
            cnt = 0
            break
print("UNRESTORABLE")

"""
https://atcoder.jp/contests/abc076/tasks/abc076_c
C - Dubious Document 2 


"""