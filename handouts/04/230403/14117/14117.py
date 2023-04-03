import sys
sys.stdin = open('input.txt', 'r')

def bfs(si, sj, ei, ej):
    INF=10*N*N

    q = []
    v = [[INF]*N for _ in range(N)]

    q.append((si,sj))
    v[si][sj]=arr[si][sj]
    
    while q:
        ci,cj=q.pop(0)
        # 목적지라고 여기서 리턴하면 안됨
        
        # 4방향, 범위 내, 이동할 위치 누적값보다 더 작은 값
        for di,dj in [(-1,0), (0,1), (0,-1), (0,1)]:
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]>v[ci][cj]+arr[ni][nj]:
                q.append((ni,nj))
                v[ni][nj]=v[ci][cj] + arr[ni][nj]

    return v[ei][ej]

T = int(input())
for tc in range(1,1+T):
    N=int(input())
    arr=[list(map(int,input())) for _ in range(N)]

    ans = bfs(0,0,N-1,N-1)
    print(f'#{tc} {ans}')