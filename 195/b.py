import math
A, B, W = map(int, input().split())

MAX = math.floor(W*1000/A)
MIN = math.ceil(W*1000/B)

if MAX < MIN:
    print("UNSATISFIABLE")
else:
    print(MIN, MAX)
