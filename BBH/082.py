import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
"""
2人零和有限確定完全情報ゲーム
この手のゲームの最適解は
自分の利益と相手の損益の合計が最大となる手を打ち続けることです。
では、今回でいう「自分の利益」と「相手の損益」について考察をしていきます。

自分の利益
これは、皿の得点です。i番目のお皿を取ったときは、高橋さんの場合はAi、青木さんの場合は、Biです。

相手の損益
これは、「もし自分がその皿を取らなかったら、相手が得ることのできた利益」を指します。なので、i番目のお皿を取ったときは、高橋さんの場合はBi、青木さんの場合は、Aiが相手に与える損益となります。

よって、「自分の利益と相手の損益の合計が最大となる手」というのは、AiとBiの合計が最大となる手のことです。
"""
N = II()
dishes = []
for i in range(N):
    A,B = MI()
    dishes.append([A+B,A,B])
    
dishes.sort(reverse=True)

Takahashi = 0
Aoki = 0
# print(dishes)

for i in range(N):
    if i % 2 == 0:
        Takahashi += dishes[i][1]
    else:
        Aoki += dishes[i][2]

print(Takahashi-Aoki)