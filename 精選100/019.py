import bisect
N = int(input())
Upper = list(map(int, input().split()))
Middle = list(map(int, input().split()))
Lower = list(map(int, input().split()))
Upper.sort()
Middle.sort()
Lower.sort()
cnt = 0
for i in Middle:
    U_index = bisect.bisect_left(Upper, i)
    L_index = bisect.bisect_right(Lower, i)
    # L_indexよりも左にあるのが条件を満たしている数だから
    cnt += U_index*(N-L_index)
    # 使える個数はU_index*(N-L_index)

print(cnt)
