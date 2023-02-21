import sys
sys.stdin = open('input.txt', 'r')

def bfs(s, e):
    si,sj=s
    ei,ej=e
    q=[(si,sj)]
    v=[[0]*N for _ in range(N)]
    v[si][sj]=1
    while q:
        ci,cj=q.pop(0)
        if (ci,cj)==(ei,ej):
            return 1
        for di,dj in [(0,1), (0,-1), (1,0), (-1,0)]:
            ni,nj=ci+di,cj+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj]!=1 and v[ni][nj]==0:
                v[ni][nj]=1
                q.append((ni,nj))

    return 0

T = 10
for tc in range(1, 1+T):
    _ = int(input())
    N = 16
    arr=[list(map(int, input())) for _ in range(N)]


    for i in range(N):
        for j in range(N):
            if arr[i][j]==2:
                si,sj=i,j
            elif arr[i][j]==3:
                ei,ej=i,j

    ans=bfs((si,sj), (ei,ej))
    print(f'#{tc} {ans}')
