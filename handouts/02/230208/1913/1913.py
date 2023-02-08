import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
x = int(input())    

arr = [[0]*n for _ in range(n)]

di = [1, 0, -1, 0] 
dj = [0, 1, 0, -1] # 하 우 상 좌 위치 지정

cnt = n**2
dr=i=j=0

for _ in range(n**2):
    arr[i][j] = cnt
    ni, nj = i+di[dr], j+dj[dr]
    cnt -= 1
    if 0<=ni<n and 0<=nj<n and arr[ni][nj] == 0:
        i, j = ni, nj
    else:
        dr = (dr+1)%4
        i, j = i+di[dr], j+dj[dr]

for k, lst in enumerate(arr):
    for l, num in enumerate(lst):
        if x == num:
            ans = (k+1, l+1)
for lt in arr:
    print(*lt)
print(*ans)