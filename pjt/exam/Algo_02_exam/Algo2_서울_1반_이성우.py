'''
로봇이 N X N 격자를 탐사하는 문제
격자의 원소에 따라 로봇이 갈 수 있는 방향이 다름.
방향은 우 하 좌 상

<중요>
항상 왼쪽 맨 윗칸에서 출발, 출발좌표 ci=cj=0
N X N 구역 벗어날 수 없음
지나간 구역을 다시 지나가지 않는다 !!!
출력값은 연속적으로 중복된 값을 삭제하여 출력
'''

T = int(input())
for tc in range(1, 1+T):
    N=int(input())
    arr=[list(map(int, input().split())) for _ in range(N)]
    # 2차원 visited 배열 설정 
    v=[[0]*N for _ in range(N)]
    
    # 방향 원소 0, 1, 2, 3 => 우 하 좌 상 
    di=[0, 1, 0, -1]
    dj=[1, 0, -1, 0]
    
    # 정답 저장할 리스트 및 초기 시작점 ci cj 선언
    alst=[]
    ci, cj = 0, 0

    # visited 배열에 ci cj 위치 1로 갱신 및 정답 리스트에 방향 push.
    v[ci][cj]=1
    alst.append(arr[ci][cj])

    while True:
        # 후보좌표 ni, nj = (현재좌표+방향원소)
        ni, nj = ci+di[arr[ci][cj]], cj+dj[arr[ci][cj]]
        
        # 만약 ni가 배열 범위 안에 존재하고, 방문되지 않았다면
        # [1] 현재좌표를 후보좌표로 갱신
        # [2] visited 배열에 방문표시
        
        if 0<=ni<N and 0<=nj<N and v[ni][nj]==0:
            ci,cj=ni,nj
            v[ci][cj]=1

            # alst에 중복원소 push를 막기위해, 
            # alst 가장 마지막 원소가 push 예정원소와 다르면 push 
            if alst[-1]!=arr[ci][cj]:
                alst.append(arr[ci][cj])
        
        # 가능한 좌표들이 visited 배열에 모두 표시되었거나, 배열범위를 벗어났으면 break 
        else:
            break

    # 출력
    print(f'#{tc}', *alst)