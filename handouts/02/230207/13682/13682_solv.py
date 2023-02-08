import sys
sys.stdin = open('input.txt', 'r')

# 반대로 접근하면 더욱 쉽게 풀리구나.
# 반대로 접근하면 쉽게 풀리는 문제가 많음. 이 문제 같은 경우도 반대로 접근하면 고려해야할 경우의 수가 매우 감소.
# 목적지(2)에서 시작
# 1순위) 좌/우 길이 있는 경우, 우선순위
# 2순위) 아닌 경우, 위로. 길이 끊겨있는 경우는 없음.
# 따라서 dr을 가지고 풀 수도 있지만, 없으면 무조건 위로가는 경우를 확인할 수 있음.
# out of index를 방지하기 위해, 좌우에 0 padding
# 0을 padding하면 많은 문제가 쉽게 풀림. 이런 padding 기술 꼭 익히자료
# 재방문을 막기 위해 visited[] 배열 사용. 지금은 방문했던 좌표를 0으로 바꾸면 된다.
# [1] 2 위치찾기, i:행 ~ i=y, j:열 ~ j=x => ci, cj 시작좌표 / ci = N-1
# [2] while ci > 0: # 0행에 도착시 종료
# [3] arr[ci][cj] <- 0 # 재방문 방지
# [4] 좌우 길이 있는 경우 거기로 이동

T = 3
for tc in range(1, T+1):
    _ = input()
    N = 100
    # 좌우 양쪽을 0으로 padding한 array 입력
    arr = [[0]+list(map(int, input().split()))+[0] for _ in range(N)]

    # [1] 시작위치 찾기
    ci = N-1
    for j in range(N):
        if arr[ci][j]==2:
            cj = j
            break
    
    # [2] N-1행 시작위치에서 위쪽으로 사다리 이동
    # 핵심코드는 단순한 구조로 작성하는게 중요함.
    while ci>0:
        arr[ci][cj] = 0     # 재방문 방지
        if arr[ci][cj-1]:   # 왼쪽으로 이동
            cj -= 1
        elif arr[ci][cj+1]: # 오른쪽으로 이동
            cj += 1
        else:
            ci -= 1         # 위쪽으로 이동
        

    print(f'#{tc} {cj-1}')