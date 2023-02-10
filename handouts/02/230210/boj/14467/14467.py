import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
lst = [input().split() for _ in range(n)]
a = [''] * 100

for i in range(len(lst)):
    a[int(lst[i][0])] += lst[i][1]

cnt = 0

for char in a:
    if len(char) <= 1:
        continue
    else:
        for j in range(len(char)-1):
            if char[j:j+2] == '10' or char[j:j+2] == '01':
                cnt +=1
print(cnt)