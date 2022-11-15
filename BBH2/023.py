import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

letter = S()
reverse_letter = letter[::-1]
# print(reverse_letter)
reverse_list = ["maerd", "remaerd", "esare", "resare"]
cnt = 0
flg = 0
while cnt < len(reverse_letter):
    for reverse_keyword in reverse_list:
        flg += 1
        if reverse_letter[cnt:cnt+len(reverse_keyword)] == reverse_keyword:
            cnt += len(reverse_keyword)
            flg = 0
            break
    if flg == 4:
        print("NO")
        exit()
print("YES")

"""
dream dreamer erase eraser

面倒なのは、「dreamer」という文字列があったときに、選択肢として
dream+erase
dream+eraser
dreamer
の3つがあることです。

この場合分けをするのは、かなり面倒です。なので、どうにか場合分け市内で済む方法をかんがえます。

文字列を全て反転させて考える。
dream dreamer erase eraser
入力Sも反転させ
追加できる文字列も
[maerd, remaerd, esare, resare]
にして進めます。

"""