S = str(input())
letter = S+S

box = letter[0]
min_ans = "z"*len(S)
max_ans = "a"*len(S)


for i in range(0, len(S)):
    tmp = letter[i:i+len(S)]
    min_ans = min(min_ans, tmp)
print(min_ans)

for i in range(0, len(S)):
    tmp = letter[i:i+len(S)]
    max_ans = max(max_ans, tmp)
print(max_ans)
