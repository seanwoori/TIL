T = int(input())
for tc in range(1, 1+T):
    n = int(input())
    ham = list(map(int, input().split()))
    # 망치 위치,
    # 세로 : ham[0],
    # 가로 : ham[1]
    lst = [list(map(int, input().split())) for _ in range(n)]
    # lst[m][0] = a 세로,
    # lst[m][1] = b 가로,
    # lst[m][2] = k 시간.

    # 망치 위치를 구해야함.
    # 만약 k가 두더지 위치까지 가는 거리보다 크다면, 망치 위치=두더지 위치
    # 그렇지 않다면, 망치위치를 구해야함. 가로가 우선, 세로가 나중.
    # 망치 위치를 구한 이후, 똑같은 것을 n번 반복함.
    ans = 0 # 출력할 답. 망치가 두더지와 마주친 횟수.

    for m in range(n):
        if ham[0]==lst[m][0] and ham[1]==lst[m][1]: # 만약 초기 망치 위치와 두더지 위치가 같다면, ans +=1 및 다음 두더지 위치로 continue.
            ans += 1
            continue
        if lst[m][2] >= abs(ham[0]-lst[m][0])+abs(ham[1]-lst[m][1]): # k값이 가야할 위치보다 크다면, 망치 위치를 두더지 위치로 갱신 및 ans +=1. 이후 다음 두더지 위치로 continue.
            ham[0], ham[1] = lst[m][0], lst[m][1]
            ans += 1
            continue
        else:
            for _ in range(lst[m][2]): # 가야할 k값에 대하여 loop
                if ham[1] != lst[m][1]: # 가로 우선. 망치 가로값이 두더지 가로값과 다르다면,
                    ham[1] += (lst[m][1]-ham[1])//abs(lst[m][1]-ham[1]) # 가야할 방향(+1 or -1) 만큼 망치의 가로를 이동.
                    continue
                else:
                    ham[0] += (lst[m][0]-ham[0])//abs(lst[m][0]-ham[0]) # 가로가 같다면 실행. 세로 또한 가야할 방향(+1 or -1) 만큼 망치의 세로를 이동.

    print(f'#{tc} {ans}')