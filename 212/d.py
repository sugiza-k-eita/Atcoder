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
        return self.heapq.heappop(self.__container)
        # 最小の値を削除

    def push(self, x):
        self.heapq.heappush(self.__container, x)
        # self.__containerにxを追加

    def sum(self):
        return sum(self.__container)

    def __len__(self):
        return len(self.__container)

    def __str__(self):
        return str(sorted(self.__container))

    def __repr__(self):
        return self.__str__()


Q = int(input())
pq = PriorityQueue()
num = 0
# 袋全体に足すnum
# 操作 2が来たとき、優先度キュー内の要素は一切変更せず、
# 代わりに全体に足された値を変数 SS​​​ で管理する
for i in range(Q):
    ns = list(map(int, input().split()))
    if ns[0] == 1:
        pq.push(ns[1]-num)
        # ns[0] == 3のときにnumを足すため、あらかじめnum分を引いている
        # print(pq)
        # ns[1] + num -num = ns[1]
        # ns[1]を追加してしまうと、袋(pq)にns[1]+numが追加されてしまうから
        # numを引く
    elif ns[0] == 2:
        # p=2のときにsumにxを足し合わせて累積和をとります。
        num += ns[1]
        # print(pq)

    elif ns[0] == 3:
        y = pq.pop()
        print(y + num)
