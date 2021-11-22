# ThreeDimensionalDistance
import math
A = [0, 1, 0]
B = [1, 0, 0]


class TDD:
    def leng(self, a, b):
        xy_leng = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
        three_leng = math.sqrt(xy_leng**2 + (a[2]-b[2])**2)
        return three_leng

    def degree(self, a, b):
        xy_leng = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
        angle = math.atan2((a[2]-b[2])**2, xy_leng)
        return math.degrees(angle)


leng_ans = TDD()
print(leng_ans.degree(A, B))
print(leng_ans.leng(A, B))
