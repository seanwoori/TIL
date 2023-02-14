import sys
sys.stdin = open('input.txt', 'r')

c, r = map(int, input().split()) # c:가로, r:세로
k = int(input())                 # k:k번째 사람

arr = list([0]*c for _ in range(r))

di = [-1,0,+1,0]
dj = [0,1,0,-1]
dr=j=0
i=r
cnt=0
while True:
    ni,nj = i+di[dr], j+dj[dr]
    if 0<=ni<r and 0<=ni<c and arr[ni][nj]==0:
        cnt+=1
        if cnt>c*r:
            break
        i,j = ni,nj
        arr[i][j] = cnt
    else:
        dr=(dr+1)%4


