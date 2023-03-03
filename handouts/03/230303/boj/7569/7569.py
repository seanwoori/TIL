import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input=sys.stdin.readline

def bfs(arr):
    q=deque()
    for sh in range(H):
        for si in range(N):
            for sj in range(M):
                if arr[sh][si][sj]==1:
                    q.append((sh,si,sj))
    while q:
        ch,ci,cj=q.popleft()
        for di,dj,dh in [(0,1,0), (1,0,0), (-1,0,0), (0,-1,0), (0,0,1), (0,0,-1)]:
            ni,nj,nh=ci+di, cj+dj, ch+dh
            if 0<=ni<N and 0<=nj<M and 0<=nh<H and arr[nh][ni][nj]==0:
                q.append((nh,ni,nj))
                arr[nh][ni][nj]=arr[ch][ci][cj]+1
    mx=0
    for sh in range(H):
        for si in range(N):
            for sj in range(M):
                if arr[sh][si][sj]==0:
                    return -1
                else:
                    if arr[sh][si][sj]>mx:
                        mx=arr[sh][si][sj]
    return mx-1

# M:가로, N:세로, H:높이
M,N,H=map(int, input().split())
# 1:익은 토마토
# 0:익지 않은 토마토
# -1: 토마토가 들어있지 않은 칸
arr=[[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
v=[[[0]*M for _ in range(N)] for _ in range(H)]
# 출력
# 모두 익을 때까지 걸리는 시간
# 만약 모두 익지 못하는 상황이면 -1

print(bfs(arr))