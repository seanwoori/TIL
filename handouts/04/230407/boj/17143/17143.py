import sys
sys.stdin = open('input.txt', 'r')

dct = {1:2, 2:1, 3:4, 4:3}
di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, 1, -1]

R, C, M = map(int, input().split())
# r,c,s,d,z => (r,c,s,d,z) 위치, 속력, 이동방향, 크기
arr = [list(map(int, input().split())) for _ in range(M)]
fisherman = -1
for _ in range(M):
    fisherman+=1
    if fisherman==C:
        break
    # [1] 각 개체 1칸씩 이동후 경계인 경우 처리
    for i in range(len(arr)):
        arr[i][0] = arr[i][0]+di[dct[arr[i][3]]]
        arr[i][1] = arr[i][1]+dj[dct[arr[i][3]]]
        if arr[i][0]
    #위치 / 속력 / 이동방향 / 크기
    # 키 / [0         1        2]
    dct[(r,c)] = [s,d,z]
