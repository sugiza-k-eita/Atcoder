import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

import bisect
N,M = MI()
A = LI()


"""
貪欲法
現段階での最大値を求める
→priority queueを使う
priority queueは、最小値を取り出すのが最も早い(今回は最大値をpopしたいので、適宜-1をかけます)
今回は、最大値をpopして、//2した値をpushする動作を繰り返します


sortしてから、一番大きいのをpop,bisectで挿入をくりかえす
"""

# A.sort()
# for i in range(M):
#     tmp = A.pop()
#     new_tmp = tmp//2
#     bisect.insort(A,new_tmp)
# #     print(A)
# # print(A)
# print(sum(A))

class PriorityQueue:
    def __init__(self, a=None):
        import heapq
        self.heapq = heapq
        self.__container = []
        if a:
            self.__container = a[:]
        self.heapq.heapify(self.__container)

    @property
    def is_empty(self):
        return not self.__container

    def pop(self):
        #最小値を取り出す
        return self.heapq.heappop(self.__container)
    
        
    def push(self, x):
        #xをheapにpush
        self.heapq.heappush(self.__container, x)

    def sum(self):
        #合計値を出力
        return sum(self.__container)

    def __len__(self):
        return len(self.__container)

    def __str__(self):
        return str(sorted(self.__container))

    def __repr__(self):
        return self.__str__()

B = []
for i in range(N):
    B.append(A[i]*-1)
    #PriorityQueueは最小値のpopしかできないので、-1をかけておきます
    
PQ = PriorityQueue(B)

for m in range(M):
    a = PQ.pop()
    #最小値(本来は最大値だったもの)をaに代入
    x = (a*-1)//2
    #aを正の数にした後、//2してxに代入
    PQ.push(x*-1)
    #先程正の数にしたので、再度-1をかけてpush
    
print(PQ.sum()*-1)


#最大値の出力においては、適宜-1をかけるひつようがあるので、少し不便ですが使いこなせるようになりましょう！！