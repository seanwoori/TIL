import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def bfs(i,j):
    q = deque()
    q.append((i,j))
    V[i][j]=arr[i][j]

    while q:
        ci,cj = q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N:
                if V[ni][nj] > V[ci][cj] + arr[ni][nj]:
                    V[ni][nj] = V[ci][cj] + arr[ni][nj]
                    q.append((ni,nj))
tc = 1
while True:
    N = int(input())
    
    if N == 0:
        break
        
    arr = [list(map(int, input().split())) for _ in range(N)]
    INF = 1e9
    V = [[INF]*N for _ in range(N)]
    bfs(0,0)
    ans = V[N-1][N-1]
    print(f'Problem {tc}: {ans}')
    tc += 1