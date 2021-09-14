N = int(input())
students = list(map(int, input().split()))
schools = list(map(int, input().split()))
students.sort()
schools.sort()
cnt = 0
for i in range(N):
    cnt += abs(schools[i]-students[i])
print(cnt)
