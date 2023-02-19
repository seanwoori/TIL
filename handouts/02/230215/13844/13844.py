import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def dfs(si, sj):
    stk=[]
    ci,cj=si,sj
    while True:
        for di,dj in [(0,1), (1,0), (-1,0), (0,-1)]:
            ni,nj=ci+di,cj+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj]!='1':
                stk.append((ci,cj))
                ci,cj=ni,nj
                arr[ci][cj]='1'
                break
        else:
            if stk:
                ci,cj=stk.pop()
            else:
                break


for tc in range(1, 1+T):
    N=int(input())
    arr=[list(map(str, input())) for _ in range(N)]
    ans='1'
    for i in range(N):
        for j in range(N):
            if arr[i][j]=='3':
                ei,ej=i,j
            elif arr[i][j]=='2':
                si,sj=i,j


    dfs(si,sj)
    if arr[ei][ej]!='1':
        ans='0'
    print(f'#{tc} {ans}')