import sys
sys.stdin = open('input.txt', 'r')

def bfs(arr, si, sj):
    v = [[0] * N for _ in range(N)]
    que = [(si, sj)]
    v[si][sj]=-1
    while que:
        ci,cj=que.pop(0)
        if (ci,cj)==(ei,ej):
            break
        for di,dj in [(0,1), (0,-1), (1,0), (-1,0)]:
            ni,nj=ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj]!=1 and v[ni][nj]==0:
                que.append((ni,nj))
                v[ni][nj]=v[ci][cj]+1
    return v

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
    v = [[0] * N for _ in range(N)]

    v=bfs(arr, si, sj)
    ans=v[ei][ej]

    print(f'#{tc} {ans}')