from collections import deque,defaultdict
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


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

N = II()

box = []
dd = defaultdict(int)
pq = PriorityQueue()
unique_num = set()
ans = 0
for i in range(N):
    s,c = map(int, input().split())
    dd[s] += c
    pq.push(s)
    unique_num.add(s)



while len(pq) > 0:
    key = pq.pop()
    kosuu = dd.pop(key)
    if kosuu == 1:
        ans += 1
        continue


    if kosuu %2 == 1:
        ans += 1
        kosuu -= 1
    
    n_kosuu = kosuu//2
    n_key = key*2
    dd[n_key] += n_kosuu
    if n_key in unique_num:
        continue
    
    unique_num.add(n_key)
    pq.push(n_key)

print(ans)
