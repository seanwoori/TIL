import sys
sys.stdin = open('input.txt', 'r')

ei, ej = map(int, input().split())
si, sj = map(int, input().split())
t = int(input())

di = [1, -1,-1, 1]
dj = [1, 1, -1, -1]
dr=k=0
i, j = si, sj

while True:
    ni, nj = i+di[dr], j+dj[dr]
    if 0<=ni<=ei and 0<=nj<=ej:
        i, j = ni, nj
        k+=1
    else:
        dr=(dr+1)%4

        if i==si and j==sj and dr==0 and k>2:
            t=t%k # 만약 k번 이동했는데 시작점이라면,
            k=0

    if k>=t:
        break



print(f'{i} {j}')