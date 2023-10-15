"""
D - Square Permutation
https://atcoder.jp/contests/abc324/tasks/abc324_d


問題文 
数字のみからなる、長さ N の文字列 S が与えられます。 S を並べ替えてできる文字列を十進法の整数として解釈したもののうち、平方数であるようなものがいくつあるか求めてください。 より厳密には、次のようになります。 S の先頭から i 番目 (1≤i≤N) の数字に対応する数を s i ​ とします。 (1,…,N) の順列 P=(p 1 ​ ,p 2 ​ ,…,p N ​ ) によって i=1 ∑ N ​ s p i ​ ​ 10 N−i と書ける整数のうち、平方数であるようなものがいくつあるか求めてください。
"""

from collections import Counter


N = int(input())
s = input()

numbox = []
for i in range(N):
    numbox.append(s[i])
sorted_s = sorted(s, reverse=True)
max_val = int("".join(sorted_s))
sqrt_limit = int(max_val ** 0.5)

s_count = Counter(s)

ans = 0
for i in range(sqrt_limit+1):
    square_str = str(i*i)
    squared_count = Counter(str(square_str))
    cnt = 0
    n_cnt = 0
    
    for num in ["0","1","2","3","4","5","6","7","8","9"]:
        if num=="0":
            if squared_count[num] > s_count[num]:
                break
        elif num != "0":
            if squared_count[num] != s_count[num]:
                break
    
    else:ans += 1

print(ans)

"""
探索範囲
1≤N≤13より
Sの並び替えは13!で> 10**8でTLEしてしまう(pythonでちゃんと無理だった・・・)

そこで、考え方を変える
今回は、ありうる最大の平方数は、Sを並び替えてできる最大値の平方数
Sを並び替えてできる最大値はすべての数字が「9」の時の
9999999999999で
この数の平方数xは10**7以下になります(9999999999999 < 10**14より√10**14 = 10**7)

そのため今回1からあり得る平方数の最大値まで全探索することが可能。


平方数の探索とカウント
コードは、1からsqrt_limit（max_valの平方根）までの各整数iについて、その平方数（i*i）が条件を満たすかどうかをチェックしています。このチェックは、for i in range(sqrt_limit+1):ループ内で行われています。

for i in range(sqrt_limit+1):
    square_str = str(i*i)
    squared_count = Counter(str(square_str))
    cnt = 0
    n_cnt = 0
    
    for num in ["0","1","2","3","4","5","6","7","8","9"]:
        if num=="0":
            if squared_count[num] > s_count[num]:
                break
        elif num != "0":
            if squared_count[num] != s_count[num]:
                break
    
    else:ans += 1


ここで、square_strはi*iの文字列形式であり、squared_countはその各数字の出現回数をカウントしたものです。次に、for num in ["0","1","2","3","4","5","6","7","8","9"]:ループで、各数字について以下のチェックを行います。

num == "0"の場合、squared_count[num]がs_count[num]よりも大きいならば、breakでループを抜けます。これは、sの中にある0の数よりも、平方数の中に0が多い場合、その平方数は条件を満たさないためです。
なぜ0の個数に関してはsquared_count[num]がs_count[num]よりも小さくても良いのでしょうか。それは、数値の先頭にある0は無視されるためです。例えば、001は1として扱われます。したがって、sの中にある0の数が多くても、平方数の中に0が少なくても、その平方数はsから作成可能であると考えられます。

具体的な例として、s = "100"とした場合、squared_count["0"] = 2となります。一方で、平方数i*i = 1の場合、squared_count["0"] = 0です。この場合、sから平方数を作成することは可能です。なぜなら、100を並び替えて001とし、先頭の0を無視すれば、1となり、平方数と一致するから

num != "0"の場合、squared_count[num]がs_count[num]と等しくない場合、breakでループを抜けます。これは、sの中の非ゼロ数字の出現回数と、平方数の中の非ゼロ数字の出現回数が一致しない場合、その平方数は条件を満たさないためです。

else: ans += 1は、forループがbreakなしで正常に終了した場合（すなわち、全ての数字について条件を満たした場合）に実行されます。この場合、答えとなるカウントansを1増やします。
"""