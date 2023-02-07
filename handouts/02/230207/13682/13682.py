import sys
sys.stdin = open('input.txt', 'r')

T = 3
for tc in range(1, 1+T):
    x = int(input()) # 필요없는 테스트케이스 받는 변수

    arr = [] # arr 저장
    n = 100 # 100x100

    di = [1, 0, 0] # 하 좌 우 방향 설정
    dj = [0, -1, 1]

    for _ in range(n):
        lst = list(map(int, input().split()))
        arr.append(lst)

    if tc == 1:
        pass
    else:
        continue

    dr=i=j=0 # 초기 변수 설정
    ans = [] # 답 받는 변수
    flag = False # 2중 루프를 빠져나오기 위한 flag

    for j in range(100): # x 좌표를 돌며 처음 시작점을 확인하고 싶음.
        if arr[i][j] == 1: # 만약 x 좌표가 1이면,
            temp = j # 출발점의 x좌표를 temp에 저장하자
            while True: # 방향 탐색
                ni, nj = i+di[dr], j+dj[dr] # next 좌표, 임시 저장하여 탐색.
                if 0<=ni<n and 0<=nj<n and arr[ni][nj] == 1: # arr의 값이 1이면 
                    i, j = ni, nj # i, j 업데이트
                else:
                    dr = (dr+1)%3 # dr 업데이트
                if i == 99 and arr[i][j] == 2: # 만약 y좌표가 끝에 도달하고 원하는 대상값이라면
                    ans = temp # 정답저장
                    flag = True # flag on
                    break # while loop 빠져나오자
                elif i >= 99:
                    break

        else: # x 좌표가 1이 아니면,
            i=0 # y좌표 초기화하고 j = j+1
            continue

        if flag == True:
            break

    print(f'#{tc} {ans}')