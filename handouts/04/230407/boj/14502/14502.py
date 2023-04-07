from itertools import combinations
from copy import deepcopy
from collections import deque
import sys
sys.stdin = open('input.txt', "r")

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

candidates=[]
virus=[]

for i in range(N):
    for j in range(M):
        if not arr[i][j]:
            candidates.append((i,j))
        elif arr[1][j]==2:
            virus.append((i,j))

tmp_walls = combinations(candidates, 3)

ans=0
for tmp_wall in tmp_walls:
    grid = deepcopy(arr)
    for i, j in tmp_wall:
        grid[i][j] = 1
    
    now_virus = deque(virus)
    while now_virus:
        ci,cj = now_virus.popleft()
        for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and grid[ni][nj]==0:
                now_virus.append((ni,nj))
                grid[ni][nj]=2

    sm=0
    for lst in grid:
        sm+=lst.count(0)
    if ans<sm:
        ans=sm
print(ans)