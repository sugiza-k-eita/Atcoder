import itertools

N, M = map(int,input().split())
letter_list = []
for i in range(N):
    letter = input()
    letter_list.append(letter)



def check(l1,l2):
    cnt = 0
    for i in range(M):
        if l1[i] != l2[i]:
            cnt +=1
    if cnt == 1:
        return True
    else:
        return False

for p in itertools.permutations(range(N)):
    is_flg = True
    for i in range(N-1):
        if check(letter_list[p[i]],letter_list[p[i+1]]) == False:
            is_flg = False
            break
    if is_flg:
        print("Yes")
        exit()
print("No")


"""

1≤i≤N−1 を満たす全ての整数 
i に対して、Tiを 1文字だけ別の英小文字に変えて Ti+1にすることが出来る

解説方針
並び替えて
N<8より並び替えと通り数を全探索しても、8の階乗(40320)なので十分に間に合います。

では、どうやって判定できるか？
異なっている場所の個数を数える
(ちなみに、こうゆうハミング距離というらしいです)

pythonはpermutationを実装してくれるitertoolsがあるので、今回はitertoolsを用いて実施します。

"""