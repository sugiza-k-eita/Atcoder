from collections import Counter

s = input()
t = input()

alha = [chr(ord("a")+i) for i in range(26)]#アルファベット列挙

#文字列sとtに含まれる各文字の出現回数をカウント
cnt_S = Counter(s)
cnt_T = Counter(t)


for i in range(26):#すべてのアルファベットについて探索
    letter = alha[i]
    if cnt_S[letter] == cnt_T[letter]:#sとtで出現するi番目のアルファベットの数が等しいなら
        continue
    elif cnt_S[letter] > cnt_T[letter]:
        if letter == "a" or letter == "t" or letter == "c" or letter == "o"or letter == "d" or letter == "e" or letter == "r":
            #atcoder のどれかで
            if cnt_T["@"] >= cnt_S[letter] - cnt_T[letter]:#@の数が0以上なら
                cnt_T["@"] -= cnt_S[letter] - cnt_T[letter]#不足分を補完して、その分@のカウントをへらす
                continue
            else:
                print("No")
                exit()
        else:
            print("No")
            exit()

    elif cnt_S[letter] < cnt_T[letter]:
        if letter == "a" or letter == "t" or letter == "c" or letter == "o"or letter == "d" or letter == "e" or letter == "r":
            if cnt_S["@"] >= cnt_T[letter] - cnt_S[letter]:
                cnt_S["@"] -= cnt_T[letter] - cnt_S[letter]
                continue
            else:
                print("No")
                exit()
        else:
            print("No")
            exit()
    
    else:
        print("No")
        exit()

print("Yes")