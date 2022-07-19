import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N,X,Y,Z = LI()


A = LI()
B = LI()

math = []
eng = []
goukei = []
for i in range(N):
    math.append([A[i]*-1,i+1])
    eng.append([B[i]*-1,i+1])
    goukei.append([(A[i]+B[i])*-1,i+1])

math.sort()
eng.sort()
goukei.sort()
# print(math)
# print(eng)
# print(goukei)
ok = []
cnt = 0

while cnt < X:
    seito = math.pop(0)
    if seito[1] not in ok:
        cnt += 1
        ok.append(seito[1])

cnt = 0
while cnt < Y:
    seito = eng.pop(0)
    if seito[1] not in ok:
        cnt += 1
        ok.append(seito[1])

cnt = 0
while cnt < Z:
    seito = goukei.pop(0)
    if seito[1] not in ok:
        cnt += 1
        ok.append(seito[1])

ok.sort()


for x in ok:
    print(x)