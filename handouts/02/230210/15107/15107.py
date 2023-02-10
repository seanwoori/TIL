import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1, 1+T):
    _ = int(input())
    arr = [[0]+list(map(int, input().split()))+[0] for _ in range(100)]
    mn = 100*100

    for sj in range(1, 101):
        # [1] 시작지점 찾기
        si = 0
        if arr[si][sj] != 1:
            continue  # 시작 인덱스 저장
        cnt, dj = 0, 0
        ci, cj = si, sj
        while ci<99:
            cnt += 1
            if dj==0:
                if arr[ci][cj-1]==1:
                    dj = -1
                    cj -= 1
                elif arr[ci][cj+1]==1:
                    dj=1
                    cj+=1
                else:
                    ci+=1
            else:
                if arr[ci][cj+dj]==1:
                    cj+=dj
                else: # 진행방향이 막힌경우 아래로
                    dj=0
                    ci+=1
        if mn>=cnt:
            mn, ans = cnt, sj-1

    print(f'#{tc} {ans}')



