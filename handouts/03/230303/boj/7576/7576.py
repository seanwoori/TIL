import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input=sys.stdin.readline

def bfs(arr):
    q=deque()
    for si in range(N):
        for sj in range(M):
            if arr[si][sj]==1:
                q.append((si,sj))
    while q:
        ci,cj=q.popleft()
        for di,dj in [(0,1), (1,0), (-1,0), (0,-1)]:
            ni,nj=ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0:
                q.append((ni,nj))
                arr[ni][nj]=arr[ci][cj]+1
    mx=0
    for si in range(N):
        for sj in range(M):
            if arr[si][sj]==0:
                return -1
            else:
                if arr[si][sj]>mx:
                    mx=arr[si][sj]
    return mx-1

# M:가로, N:세로, H:높이
M,N=map(int, input().split())
# 1:익은 토마토
# 0:익지 않은 토마토
# -1: 토마토가 들어있지 않은 칸
arr=[list(map(int, input().split())) for _ in range(N)]
v=[[0]*M for _ in range(N)]
# 출력
# 모두 익을 때까지 걸리는 시간
# 만약 모두 익지 못하는 상황이면 -1

print(bfs(arr))