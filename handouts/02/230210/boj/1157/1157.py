import sys
sys.stdin = open('input.txt', 'r')

st = input().lower()
idx = [0]*200
ans = ''

for char in st:
    idx[(ord(char))] += 1

a = 0
ans_lst = []
for id,cnt in enumerate(idx):
    if cnt == max(idx):
        ans_lst.append(chr(id))
if len(ans_lst)>1:
    ans = '?'
else:
    ans = ans_lst[0].upper()
print(ans)

