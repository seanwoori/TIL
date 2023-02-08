import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = [[0]*100 for _ in range(100)]
a=0
for lst in arr:
    for i in range(10):
        for j in range(10):
            ans[lst[1]-1+j][lst[0]-1+i] = 1

for k in range(100):
    a += sum(ans[k])
print(a)
