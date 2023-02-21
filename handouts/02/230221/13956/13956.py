import sys
sys.stdin = open('input.txt', 'r')

def bfs(arr, si, sj):
    v=set()
    que = [(si, sj)]
    arr[si][sj]=1
    while que:
        ci,cj=que.pop(0)
        for di,dj in [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (-1,1), (1,-1)]:
            ni,nj=ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj]!=1:
                que.append((ni,nj))
                arr[ni][nj]=1
    if arr[ei][ej]==1:
        return 1
    return 0

T = int(input())
for tc in range(1, 1+T):
    N=int(input())
    arr=[list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j]==2:
                si,sj=i,j
            elif arr[i][j]==3:
                ei,ej=i,j

    ans=bfs(arr,si,sj)
    print(f'#{tc} {ans}')