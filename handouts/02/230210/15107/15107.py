import sys
sys.stdin = open('input.txt', 'r')





T = 10
for tc in range(1, 1+T):
    n = 100
    di = [1, 0, 0]
    dj = [0, -1, 1] # 하 좌 우 좌표 설정

    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    alt = [] # 횟수 저장 리스트
    sidx = [] # 시작 인덱스 저장 리스트
    dr=i=j=0
    for k in range(n):
        cnt=0 # cnt 가로에 맞춰서 갱신
        if arr[0][k] == 1:
            sidx.append(k)  # 시작 인덱스 저장
            while i < n:
                ni,nj = i+di[dr], j+dj[dr]
                if arr[ni][nj]==1 and 0<=ni<n and 0<=nj<n:
                    i, j = ni, nj
                    if dr != 0: # 아래로 내려가는 경우 걸러야함.
                        cnt +=1
                else:
                    dr=(1+dr)%3
            alt.append(cnt)

    print(alt, sidx)



