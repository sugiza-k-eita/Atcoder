import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()


letter = "abcdefghijklmnopqrstuvwxyz"
d = dict()
for i in range(26):
    d[letter[i]] =i
s = S()
t = S()

s_box = [[] for i in range(26)]
t_box = [[] for i in range(26)]
for i in range(len(s)):
    s_num = d[s[i]]
    t_num = d[t[i]]
    s_box[s_num].append(t_num)
    t_box[t_num].append(s_num)
    s_box[s_num] = list(set(s_box[s_num]))
    t_box[t_num] = list(set(t_box[t_num]))
    if len(s_box[s_num]) != 1 or len(t_box[t_num]) != 1:
        print("No")
        exit()
print("Yes")