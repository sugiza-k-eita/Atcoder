N,A,B =map(int, input().split())
C = list(map(int, input().split()))

AB = A+B
for i in range(N):
    if AB == C[i]:
        print(i+1)#0-index→1-indexに直す

"""
AとBを足した変数を用意し、Cというリストを前から探索したときに一致したら、そのindex+1を出力します。
(問題は1-indexでpythonは0-indexなので、+1する必要があります)
"""