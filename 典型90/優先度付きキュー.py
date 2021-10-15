# python標準ライブラリのheapqは大変使いづらいので、使いやすいようクラスにしておくと良いです
# なお、このクラスにバグがあっても責任は一切取りません、自分で書いてね
# https://qiita.com/u2dayo/items/6debaf81fd39f82a4280#d%E5%95%8F%E9%A1%8Cquerying-multiset-
# https://atcoder.jp/contests/abc212/tasks/abc212_d

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

    def push(self, x):
        self.heapq.heappush(self.__container, x)

    def sum(self):
        return sum(self.__container)

    def __len__(self):
        return len(self.__container)

    def __str__(self):
        return str(sorted(self.__container))

    def __repr__(self):
        return self.__str__()
