import sys
from collections import deque
import copy

sys.stdin = open('input.txt', 'r')
input=sys.stdin.readline
def bfs(arr):
    qw=deque()
    qg=deque()
    warr = copy.deepcopy(arr)
    garr = copy.deepcopy(arr)

    for i in range(R):
        for j in range(C):
            if arr[i][j]=='S':
                qg.append((i,j))
                garr[i][j]=1
                warr[i][j]='.'
            elif arr[i][j]=='*':
                qw.append((i,j))
                warr[i][j]=1
                garr[i][j]='.'
            elif arr[i][j]=='D':
                ci,cj=i,j

    while qw:
        if qw:
            wci,wcj=qw.popleft()

        for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            wni, wnj = wci+di, wcj+dj
            if 0<=wni<R and 0<=wnj<C and warr[wni][wnj]=='.':
                qw.append([wni,wnj])
                warr[wni][wnj]=warr[wci][wcj]+1

    while qg:
        if qg:
            gci,gcj=qg.popleft()

        for di,dj in [(0,-1), (0,1), (-1,0), (1,0)]:
            gni,gnj=gci+di, gcj+dj
            if 0<=gni<R and 0<=gnj<C and garr[gni][gnj]=='.':
                qg.append([gni,gnj])
                garr[gni][gnj]=garr[gci][gcj]+1

    temp=[]
    for di, dj in [(0,-1), (0,1), (-1,0), (1,0)]:
        ni,nj=ci+di, cj+dj
        if 0<=ni<R and 0<=nj<C:
            if not type(warr[ni][nj])==int:
                if type(garr[ni][nj])==int:
                    temp.append(garr[ni][nj])
            else:
                if type(garr[ni][nj])==int and warr[ni][nj]>garr[ni][nj]:
                    temp.append(garr[ni][nj])
    else:
        if temp:
            return min(temp)
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