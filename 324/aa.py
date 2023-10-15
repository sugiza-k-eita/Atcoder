"""
https://atcoder.jp/contests/abc324/tasks/abc324_a
A - Same

問題文 
N 個の整数 A 1 ​ ,A 2 ​ ,…,A N ​ が与えられます。 これらの値がすべて等しいならば Yes 、そうでなければ No と出力してください。
"""

N = int(input())
A = list(map(int, input().split()))

for i in range(1,N):
    if A[0]!=A[i]:
        print("No")
        exit()
print("Yes")

"""

"""
