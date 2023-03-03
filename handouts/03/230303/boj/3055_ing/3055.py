import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

def bfs(arr):
    qw=deque()
    qg=deque()
    for i in range(R):
        for j in range(C):
            if arr[i][j]=='S':
                qg.append((i,j))
                arr[i][j]=1
            elif arr[i][j]=='*':
                qw.append((i,j))
            elif arr[i][j]=='D':
                ci,cj=i,j
    cnt=0
    while qw or qg:
        if qg:
            gci,gcj=qg.popleft()
        if qw:
            wci,wcj=qw.popleft()

        for di,dj in [(0,-1), (0,1), (-1,0), (1,0)]:
            gni,gnj=gci+di, gcj+dj
            if 0<=gni<R and 0<=gnj<C and arr[gni][gnj]=='.' and arr[gni][gnj]!='X':
                qg.append((gni,gnj))
                arr[gni][gnj]=arr[gci][gcj]+1

        for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            wni, wnj = wci+di, wcj+dj
            if 0<=wni<R and 0<=wnj<C and arr[wni][wnj]=='.' and arr[wni][wnj]!='X' and (wni,wnj)!=(ci,cj):
                qw.append((wni, wnj))
                arr[wni][wnj] = '*'
    else:
        if (gci, gcj) == (ci, cj):
            return arr[gci][gcj]
        else:
            return 'KAKTUS'

R,C=map(int,input().split())
arr=[list(map(str, input())) for _ in range(R)]
# 비어있는 곳 '.'
# 물이 차있는 지역'*'
# 돌은 'x'
# 비버의 굴은 'D'
# 고슴도치의 위치는 'S'
# 물도 확산함
# 고슴도치가 안전하게 비버의 굴로 이동하기 위한 최소 시간
print(bfs(arr))