import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input=sys.stdin.readline
# 델타변환으로 도형 둘레구하기
# 하지만 도형 안에 있는 구멍은 체킹이 되지 않음.
# 구멍을 어떻게 처리하지??
# 그러면 겉부분을 전부 bfs로 마스킹을 해야겠다
# 그리고 마스킹 부분이 상하좌우 벽에 한부분이라도 닿으면 진짜 마스킹. 마스킹은 'a'로
# 안닿으면 되돌려. 그러면 다시 0으로

def start(arr):
    for i in range(M):
        for j in range(N):
            if arr[i][j]==0:
                return i,j
    else:
        return False

def bfs(arr):
    si,sj=start(arr)
    q=deque()
    q.append((si,sj))
    arr[si][sj]=-1
    while q:
        ci,cj=q.popleft()
        for di,dj in [(0,-1), (0,1), (1,0), (-1,0)]:
            ni,nj=ci+di, cj+dj
            if 0<=ni<M and 0<=nj<N and arr[ni][nj]==0:
                arr[ni][nj]=-1
                q.append((ni,nj))

    tarr=list(zip(*arr))
    temp=[tarr[0],tarr[-1],arr[0],arr[-1]]
    ans=0
    for lst in temp:
        for num in lst:
            if num==-1:
                ans=2
                break

    for i in range(M):
        for j in range(N):
            if arr[i][j]==-1:
                arr[i][j]=ans

def mask(arr):
    for ci in range(M):
        for cj in range(N):
            if arr[ci][cj]==2:
                for di,dj in [(0,-1), (0,1), (1,0),(-1,0)]:
                    ni,nj=ci+di,cj+dj
                    if 0<=ni<M and 0<=nj<N and arr[ni][nj]==1:
                        arr[ni][nj]='c'

def cnt_func(arr):
    c=0
    for i in range(M):
        for j in range(N):
            if arr[i][j]==1 or arr[i][j]=='c':
                c+=1
    return c

def delete(arr):
    for ci in range(M):
        for cj in range(N):
            if arr[ci][cj]=='c' or arr[ci][cj]==2:
                arr[ci][cj]=0

# M sero, N garo
M,N=map(int, input().split())
arr=[list(map(int, input().split())) for _ in range(M)]
cnt=0
a=0
while True:
    if not cnt_func(arr):
        break
    else:
        cnt+=1
        bfs(arr)
        mask(arr)
        a=cnt_func(arr)
        delete(arr)


print(cnt)
print(a)