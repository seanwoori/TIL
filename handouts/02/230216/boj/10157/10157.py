import sys
sys.stdin = open('input.txt', 'r')

c, r = map(int, input().split()) # c:가로, r:세로
k = int(input())                 # k:k번째 사람

arr = list([0]*c for _ in range(r))

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
dr=j=0
i=r-1
cnt=1
pij=False
flag=True
if k>c*r:
    flag = False

while flag:
    arr[i][j] = cnt
    if cnt == k:
        flag = False
        pij = True
        break
    ni,nj = i+di[dr], j+dj[dr]
    if 0<=ni<r and 0<=nj<c and arr[ni][nj]==0:
        cnt+=1
        i,j = ni,nj
        if cnt>c*r:
            break
    else:
        dr=(dr+1)%4


if pij:
    print(j+1, r-i)
else:
    print(0)
