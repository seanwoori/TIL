T = int(input()) # test case 갯수를 받음
for tc in range(1, 1+T): # test case 갯수에 따라 for loop 실행
    n, m = map(int, input().split()) # n : 도화지의 크기 (nxn), m : 도장을 찍은 횟수
    arr = [[0]*n for _ in range(n)] # 0으로 초기화된 nxn array를 저장
    lst = [list(map(int, input().split())) for _ in range(m)]
    # lst[i] i번째 도장의 정보.
    # lst[i][0], lst[i][1] : 초기 세로 및 가로의 위치.
    # lst[i][2] 가로너비, lst[i][3] 세로높이.
    ans = 0

    for m in range(len(lst)): # 찍은 도장의 갯수 m에 대하여,
        for i in range(lst[m][2]): # lst[m] 도장의 가로와
            for j in range(lst[m][3]): # lst[m] 도장의 세로에 대하여 loop
                arr[lst[m][0]+j][lst[m][1]+i] = 1 # 해당하는 인덱스의 array 값을 1로 저장

    for k in range(len(arr)): # 이후 모든 array 값에 대하여 합을 구함.
        ans += sum(arr[k])
    print(f'#{tc} {ans}')
